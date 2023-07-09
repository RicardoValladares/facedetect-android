# Deteccion de Rostros (alpha)
Este proyecto depende del proyecto Rostro Biométrico(https://gitlab.com/RicardoValladares/facedetect), con este proyecto se pretende usar la interfaz grafica de android para disminuir el consumo de recursos que se tiene con la interfaz web. 

Este proyecto requiere que el servidor de Rostro Biométrico(https://gitlab.com/RicardoValladares/facedetect) este en ejecucion, asi como tambien tener instalado python y sus dependencias, para instalar las dependencias puedes usar el comando:

```bash
make dependens
```

Para ejecutar el proyecto sin usar emuladores android:

```bash
make run
```


Librerías usadas:
- OpenCV (https://docs.opencv.org/3.4/d5/d10/tutorial_js_root.html)
- Kivy (https://kivy.org/)

Servidor usado:
- Rostro Biométrico (https://gitlab.com/RicardoValladares/facedetect)


