import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_distances
from PIL import Image
import piexif
import os
import torch
from yolov5 import YOLOv5
import cv2

# Cargar el modelo ResNet50 preentrenado
base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

# Cargar el modelo YOLOv5 preentrenado
model_yolo = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def extract_embedding(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    
    embedding = model.predict(img_data)
    return embedding.flatten()

def find_similar_images(query_img_path, k=5):
    query_embedding = extract_embedding(query_img_path)
    
    with open('embeddings.pkl', 'rb') as f:
        embeddings, image_paths = pickle.load(f)
    
    distances = cosine_distances([query_embedding], embeddings)[0]
    nearest_indices = distances.argsort()[:k]
    
    similar_images = [image_paths[i] for i in nearest_indices]

    return similar_images

def get_gps_coordinates(image_path):
    try:
        image = Image.open(image_path)
        exif_dict = piexif.load(image.info.get("exif", b''))
        gps_info = exif_dict.get('GPS', {})

        if not gps_info:
            return None

        def convert_to_degrees(value):
            d = value[0][0] / value[0][1]
            m = value[1][0] / value[1][1]
            s = value[2][0] / value[2][1]
            return d + (m / 60.0) + (s / 3600.0)

        lat = convert_to_degrees(gps_info[piexif.GPSIFD.GPSLatitude])
        if gps_info[piexif.GPSIFD.GPSLatitudeRef] != 'N':
            lat = -lat

        lon = convert_to_degrees(gps_info[piexif.GPSIFD.GPSLongitude])
        if gps_info[piexif.GPSIFD.GPSLongitudeRef] != 'E':
            lon = -lon

        return (lat, lon)
    except Exception as e:
        print(f"Error extrayendo coordenadas GPS de {image_path}: {e}")
        return None

def append_embedding(img_data, embeddings_file, img_file):
    # Leer embeddings existentes
    if os.path.exists(embeddings_file):
        with open(embeddings_file, 'rb') as f:
            existing_embeddings, existing_image_paths = pickle.load(f)
    else:
        existing_embeddings, existing_image_paths = [], []

    # Obtener el embedding de la nueva imagen
    embedding = extract_embedding(img_data)
    
    # Simular un nombre de archivo para la nueva imagen
    dataset_path = 'D:\Maestria\semestre_3\DataAnalytics\PetMatch\Data\pruebas'
    # img_file = f"uploaded_image_{len(existing_image_paths) + 1}.jpg"
    img_path = os.path.join(dataset_path, img_file)
    
    # Anexar el nuevo embedding y la ruta de la imagen
    existing_embeddings.append(embedding)
    existing_image_paths.append(img_path)
    
    # Guardar los datos actualizados
    with open(embeddings_file, 'wb') as f:
        pickle.dump((existing_embeddings, existing_image_paths), f)

    # print(f"Embedding anexado y guardado en '{embeddings_file}'")

# Función para detectar si hay un perro en la imagen
def is_dog(imagen_path):    
    # Cargar la imagen
    img = cv2.imread(imagen_path)
    
    # Realizar la detección
    results = model_yolo(img)
    
    # Obtener las etiquetas de los resultados
    etiquetas = results.pred[0][:, -1].cpu().numpy()
    
    # Las etiquetas de COCO para YOLOv5, la etiqueta para 'perro' es 16
    return 16 in etiquetas