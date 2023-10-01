# PoseDigits-Game

![portada](https://github.com/PinMafer13/PoseDigits-Game/assets/110617942/1aadaba0-d6e5-4f78-9cc1-d101aefdcecf)

# Descripción📜
Juego interactivo que detecta poses humanas y desafía a las personas a simular números del 0 al 9. 
El programa recopila el video de la cámara web, detecta la pose humana en cada fotograma y clasifica la pose en función de los ángulos de las articulaciones con ayuda de librerias como mediapipe y cv2. Luego, en la parte superior izquierda de la imagen se muestran tres números aleatorios que deben ser simulados con las poses del cuerpo. El programa se detiene cuando se presiona la tecla 'a'.

Además, se tiene en cuenta que cuando ninguna pose coincide con las combinaciones previamente establecidas en el codigo aparece la leyenda "no pose detection".

![ejemplo](https://github.com/PinMafer13/PoseDigits-Game/assets/110617942/e47e3175-3760-4e24-8386-b577d68925d3)

# Herramientas🛠️
* Cámara web o cámara integrada en tu dispositivo.
* Computadora con Python instalado.
* Conexión a Internet (para instalar las bibliotecas necesarias).

# Librerías📚
Programa en Python que utiliza las bibliotecas:
* OpenCV (cv2)
* MediaPipe (mediapipe)
* NumPy
Los cuales son necesarios para realizar la detección y clasificación de gestos de poses humanas en tiempo real a través de una cámara web.

# Total Estimado💰
El proyecto tiene un costo relativamente bajo, puesto que solo se requiere de una computadora y una cámara web. Además, el software es de código abierto y gratuito.

# Uso🚀
1. Asegúrate de tener Python y las bibliotecas OpenCV, MediaPipe y NumPy instaladas.
2. Abre una terminal y ejecuta el programa Python.
3. Una ventana de video en tiempo real se abrirá. Asegúrate de tener una cámara web conectada.
4. Intenta realizar una pose humana con las articulaciones correctas.
5. El programa detectará tu pose y te desafiará a crear un número correspondiente a la pose. ¡Diviértete!

Acontinuación se muestran ejemplos de poses para simular los numeros del 0-9

![poses_ejemplos](https://github.com/PinMafer13/PoseDigits-Game/assets/110617942/a562b8a3-708c-466f-80dd-861d6b5204e7)

# Posibles mejoras:
Para mejorar el programa y evitar tener muchas condiciones para clasificar las poses, especialmente cuando el rango de numeros aumente, es recomendable utilizar técnicas de aprendizaje automático, como la clasificación basada en modelos de aprendizaje profundo. Para ello se puede considerar lo siguiente:

1. Recopilar un conjunto de datos etiquetados que contenga ejemplos de diferentes poses humanas etiquetados con los números correspondientes.
2. Entrenar un modelo de aprendizaje profundo, se requiere de conocimientos avanzados para el uso de paquetes como Tensorflow o PyTorch para entrenar un modelo de clasificación de poses. Puedes utilizar arquitecturas de redes neuronales convolucionales (CNN) o redes neuronales recurrentes (RNN) según el tipo de entrada (imágenes o secuencias de landmarks).
3. Validar y ajustar el conjunto de datos en conjuntos de entrenamiento y prueba para validar y ajustar el modelo.
4. Diseñar una mejor interfaz de usuario que brinde una retroalimentación y sea dinámica con el usuario, especialmente si el juego va dirigido a niños para estimular su actividad fisica.
Con todo lo mencionado anteriormente, el usuario tendrá mayor libertad de usar su imaginación para simular una variedad de poses en base a los numeros con un rango mayor del 0-9.

# Colaboradores👥

![colaboradores](https://github.com/PinMafer13/PoseDigits-Game/assets/110617942/f8a2ad8a-fb1b-4779-9aa5-eda3127d3983)
