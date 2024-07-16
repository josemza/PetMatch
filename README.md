# PetMatch

Es un **prototipo web** que realiza la búsqueda de mascotas pérdidas mediante similitud de imágenes utilizando herramientas de *Deep Learning* como *Convolutional Neural Networks* (CNN), *Transfer Learning* y *Embeddings*. Este proyecto forma parte de la asignatura "*Data Analytics* para la toma de decisiones" que se imparte en la Maestría en *Computer Science* de la Escuela de Posgrado de la Universidad de Ingeniería y Tecnología (UTEC) cuyo docente es Germaín García, *Phd.* en *Computer Science*. 

Si bien este proyecto se encuentra en una etapa de MVP tiene como principal objetivo, en un horizonte de mediano y largo plazo, convertirse en el portal de búsqueda de mascotas perdidas más utilizado en Perú y Latinoamérica, respectivamente.

![Portada de PetMatch](Capturas/Portada%20%281%29.jpg)

## Cifras y trabajos previos

* Cada año en Perú, aproximadamente 420,000 mascotas, principalmente perros y gatos, se pierden debido a la falta de identificación. Solo una pequeña fracción es recuperada. Las principales causas de pérdida incluyen robos, mascotas dejadas solas, asustadas por ruidos fuertes o perdidas de vista por sus dueños. Se ha desarrollado un nuevo localizador con código QR para mejorar la identificación y recuperación. Este método permite acceder a una ficha virtual con información relevante y ubicación de la mascota cuando se escanea el código​ ([Andina](https://andina.pe/agencia/noticia-unas-420000-mascotas-se-pierden-cada-ano-peru-falta-identificacion-732435.aspx))​.

* En 2022, el proyecto "Alerta Me Perdí" reportó 1706 animales perdidos en Guayaquil, con un 79% de perros y un 21% de gatos. El 25% de los animales regresaron a sus hogares, una mejora respecto al 21% del primer semestre. Solo el 12% de los animales tenían collar y placa, y el 22% estaban esterilizados. La mayoría de los reportes provinieron de Guayas (89%) y Guayaquil (93%). Los sectores con más reportes fueron Suburbio (14%) y Sauces (9%) ([rescateanimal.org.ec](https://rescateanimal.org.ec/estadisticas2022/)).

* La aplicación móvil "Pata de Perro" fue creada por Jonet Lazo y Viviana Arce para ayudar a reducir el número de mascotas perdidas en Perú. Utiliza la geolocalización para facilitar el reencuentro de mascotas con sus dueños, permitiendo publicar avisos de mascotas perdidas y encontradas con detalles y datos de contacto. Una encuesta, realizada por dicho equipo, reveló que solo el 18% de los perros perdidos regresan a sus hogares y el 58% de las personas no saben qué hacer al encontrar un perro perdido. La app también ofrece placas con código QR para una identificación más segura ([El Comercio](https://elcomercio.pe/wuf/noticias/app-movil-busca-minimizar-numero-mascotas-perdidas-noticia-449449-noticia/?ref=ecr)).

## Nuestro equipo 
| [![Jose Zuniga](team/Jose_Zuniga_200.jpg)](ruta/a/la/foto1.jpg) | [![Jeyson Lino](team/Jeyson_Lino_200.jpg)](ruta/a/la/foto2.jpg) | [![Juan Herencia](team/Juan_Herencia_200.jpg)](ruta/a/la/foto3.jpg) | 
|:--:|:--:|:--:| 
| **José Zuñiga** | **Jeyson Lino** | **Juan Herencia** |
| Entusiasta tecnológico e ingeniero industrial con ocho años de experiencia en el sector público y privado. Cinco años de experiencia en temas vnculados con propiedad intelectual, innovación y patentes y tres años en temas vinculados con gestión de la información, dashboarding y explotación de datos. Cuenta con especializaciones en data analytics, machine learning y deep learning por diferentes instituciones. Al 2024, maestrando en computer science por la escuela de posgrado de UTEC. | Ingeniero de sistemas con más de 7 años de experiencia en analítica de datos. Sólidos conocimientos en herramientas de procesamiento, análisis y visualización de datos. Busco crear valor mediante el desarrollo de soluciones analíticas que permitan evidenciar la importancia de una toma de decisiones basada en datos. Data Scientist en progreso. | Profesional con experiencia en dirección y desarrollo de soluciones en tecnologías de la información para el sector público y privado. Con especialización en análisis de datos y uso de herramientas de Machine Learning, Deep Learning e IA. |

## Publico objetivo
Dueños de mascotas perdidas en territorio peruano. En esta primera etapa del proyecto solo se trabajará con perros, sin embargo, se planifica ampliar el espectro de mascotas buscadas a gatos, canarios y otros. Así mismo se tiene como objetivo ampliar el público a otros países de Latinoamérica.

## Funcionalidades MVP de PetMach
Actualmente el producto mínimo viable trabaja con dos funcionalidades principalmente: búsqueda de perros por similitud de imágenes y reporte de posible perro perdido.

### Búsqueda de perros por similitud de imágenes
Esta funcionalidad permite que el usuario cargue una imagen de su perro. El sistema realiza una búsqueda por similitud de imágenes en la base de datos de perros reportados como perdidos y devuelve las 6 imágenes que contienen los perros más parecidos en orden de similitud.

**Diagrama de flujo del proceso general para la búsqueda de un perro en PetMatch**
```mermaid
graph LR
A(Cargar la imagen) -- Se valida --> B{"¿hay perro?"}
B -- Sí --> C(Preparar la imagen)
C --> D(Realizar búsqueda)
B -- No --> F(Mensaje de error)
F -- Retorno a la pantalla inicio --> A
D --> E(Devolver resultados)
```

**Buscar a partir de una imagen con perro**
| [![Seccion busqueda](Capturas/Buscar_mascota.jpg)](Capturas/Buscar_mascota.jpg) | [![Seleccionar mascota](Capturas/seleccion_perro.jpg)](Capturas/seleccion_perro.jpg) | [![Resultados](Capturas/resultados_perros.jpg)](Capturas/resultados_perros.jpg) | 
|:--:|:--:|:--:| 

>El proceso detecta que hay un perro en la imagen y procede con la búsqueda en la base de datos.

Adicionalmente en la página de resultados cada imagen posee un enlace de geolocalización que redirige al usuario hacia google maps. En la ventana de google maps se encuentra un pin sobre la ubicación donde la foto fue tomada. Con esta funcionalidad se busca ayudar al usuario con la ubicación de la última vez que se vio a su mascota.

<div style="text-align: center;">
    <img src="Capturas/mapa_geolocalizacion.jpeg" alt="Geolocalizacion de la imagen" style="width: 600px; border-radius: 50%;">
</div>

**Buscar a partir de una imagen con un pato**
| [![Seccion busqueda](Capturas/Buscar_mascota.jpg)](Capturas/Buscar_mascota.jpg) | [![Seleccionar mascota](Capturas/seleccion_pato.jpg)](Capturas/seleccion_pato.jpg) | [![Resultados](Capturas/pantalla_no_perro.jpg)](Capturas/pantalla_no_perro.jpg) | 
|:--:|:--:|:--:| 

>El proceso detecta que no hay un perro en la imagen y envía un mensaje al usuario y no llama a la función de bpusqueda.

>**Nota importante:** En esta etapa del proyecto solo se permite que el usuario cargue una foto a la vez para realizar la búsqueda. En posteriores actualizaciones se planea permitir que el usuario pueda cargar varias fotos a la vez con la intención de obtener un mejor resultado.

### Reporte de posible perro perdido
Esta funcionalidad permite que el usuario pueda reportar a un perro que encontró perdido. Esta sección depende del apoyo de la comunidad por lo que es indispensable promover e incentivar la acción de reportar.

**Diagrama de flujo del proceso general del reporte de perro perdido**
```mermaid
graph LR
A(Cargar la imagen) --> B{"¿Hay perro?"}
B -- sí --> C(Transforma la imagen y la almacena)
B -- no --> D(Muestra mensaje de error)
D -- retorna a la pantalla inicial --> A
C --> E(Muestra mensaje de éxito)
```

**Reportar a partir de una imagen con perro**
| [![Seccion busqueda](Capturas/Buscar_mascota.jpg)](Capturas/Buscar_mascota.jpg) | [![Seleccionar mascota](Capturas/seleccion_perro_reporte.jpg)](Capturas/seleccion_perro_reporte.jpg) | [![Resultados](Capturas/mensaje_exito_reporte.jpg)](Capturas/mensaje_exito_reporte.jpg) | 
|:--:|:--:|:--:| 

>El proceso detecta que hay un perro en la imagen y procede con la preparación de la imagen para almacenarla en la base de datos.

## Sección de historias de éxito
En esta sección el usuario puede visualizar las historias de reencuentro gracias a la herramienta. Son historias cargadas por los usuarios. Actualmente no está disponible aún un formulario para cargar las historias directamente por el usuario por lo que la historia se recopila y carga directamente por el equipo de PetMatch.

![Historias de reencuentro](Capturas/Historias.jpg)

## Explicación del código




