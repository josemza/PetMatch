from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from urllib.parse import quote
import uvicorn
import os
from model import find_similar_images, get_gps_coordinates, append_embedding, is_dog

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/data", StaticFiles(directory="D:/Maestria/semestre_3/DataAnalytics/PetMatch/Data"), name="data")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/uploadfile/")
# async def create_upload_file(request: Request, file: UploadFile = File(...)):
#     file_location = f"temp_images/{file.filename}"
#     with open(file_location, "wb+") as file_object:
#         file_object.write(file.file.read())
    
#     similar_images = find_similar_images(file_location)
#     similar_images_paths = ["/data/" + quote(os.path.relpath(img, "D:/Maestria/semestre_3/DataAnalytics/PetMatch/Data").replace("\\", "/")) for img in similar_images]
#     return templates.TemplateResponse("results.html", {"request": request, "similar_images": similar_images_paths})

@app.post("/uploadfile/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    file_location = f"temp_images/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    # Verificamos que la imagen contenga a un perro
    if not is_dog(file_location):
        message = "No se ha podido detectar un perro en la imagen"
        os.remove(file_location)

        return templates.TemplateResponse("message.html", {"request": request, "message": message})
        
    else:        
        similar_images = find_similar_images(file_location)
        similar_images_data = []

        for img_path in similar_images:
            img_relative_path = "/data/" + quote(os.path.relpath(img_path, "D:/Maestria/semestre_3/DataAnalytics/PetMatch/Data").replace("\\", "/"))
            gps_coordinates = get_gps_coordinates(img_path)
            if gps_coordinates:
                lat, lon = gps_coordinates
                maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
            else:
                maps_url = None
            similar_images_data.append({"path": img_relative_path, "maps_url": maps_url})

        return templates.TemplateResponse("results.html", {"request": request, "similar_images": similar_images_data})

@app.post("/uploadfile_report/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    file_location = f"data/pruebas/{file.filename}"
    img_data = file.file.read()
    with open(file_location, "wb+") as file_object:
        file_object.write(img_data)

    embeddings_file = 'embeddings.pkl'
    append_embedding(file_location, embeddings_file,file.filename)

    message = "Se cargó la imagen satisfactoriamente. ¡Gracias por tu apoyo!"
    return templates.TemplateResponse("message.html", {"request": request, "message": message})

if __name__ == "__main__":
    if not os.path.exists("temp_images"):
        os.makedirs("temp_images")
    uvicorn.run(app, host="127.0.0.1", port=8000)
