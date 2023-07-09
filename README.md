# Deteccion de Rostros (alpha)
Este proyecto depende del proyecto Rostro Biométrico(https://github.com/RicardoValladares/FaceDetect), con este proyecto se pretende usar la interfaz grafica de android para disminuir el consumo de recursos que se tiene con la interfaz web. 

Este proyecto requiere que el servidor de Rostro Biométrico(https://github.com/RicardoValladares/FaceDetect) este en ejecucion y que el cliente tenga la ip de dicho servidor registrado como el host "facedetect.com" aunque enrealidad el servicio se consume en el puerto "5001", tambien es necesario tener instalado python y sus dependencias, para instalar las dependencias puedes usar el comando:

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
- Rostro Biométrico (https://github.com/RicardoValladares/FaceDetect)

Herramientas usadas:
- Virtual Hosts https://github.com/x-falcon/Virtual-Hosts

