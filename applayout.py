import requests
import threading
import time
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import platform
from edgedetect import EdgeDetect

class AppLayout(FloatLayout):
    edge_detect = ObjectProperty()
        
class ButtonsLayout(RelativeLayout):
    isrunning = False
    segundos = 0
    kwargs = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = kwargs
    
    def thread_function(self):
        while True:
            if self.parent.edge_detect.detected():
                if self.segundos>=3:
                    self.sendpost()
                else:
                    self.segundos = self.segundos + 1
                    self.ids.status.text = str(self.segundos)
                    self.parent.edge_detect.recognition(str(self.segundos))
            else:
                self.segundos = 0
                self.ids.status.text = str(self.segundos)
                self.parent.edge_detect.recognition(str(self.segundos))
            time.sleep(1)

    def sendpost(self):
        self.ids.identify.text = "IDENTIFICANDO"
        self.parent.edge_detect.recognition("IDENTIFICANDO")
        try:
            self.parent.edge_detect.save()
            multipart_form_data = (('image', ('rostro.jpg', open('rostro.jpg', 'rb'))),('action', (None, 'store')))
            response = requests.post(self.ids.input.text, files=multipart_form_data)
            self.ids.identify.text = str( response.content.decode('utf-8') )
            self.parent.edge_detect.recognition(str( response.content.decode('utf-8') ))
            time.sleep(5)
        except:
            self.ids.identify.text = "INCOMUNICADO"
            self.parent.edge_detect.recognition("INCOMUNICADO")
            time.sleep(3)
        self.segundos = 0
        self.ids.identify.text = "DESCONOCIDO"
        self.ids.status.text = str(self.segundos)
        self.parent.edge_detect.recognition(str(self.segundos))
    
    
    def on_size(self, layout, size):
        self.pos = (0 , 0)
        self.size_hint = (1 , 0.2)
        self.ids.status.pos_hint  = {'center_x':.05,'center_y':.5}
        self.ids.status.size_hint = (.2, None)
        self.ids.identify.pos_hint  = {'center_x':.5,'center_y':.5}
        self.ids.identify.size_hint = (.2, None)
        self.ids.other.pos_hint  = {'center_x':.9,'center_y':.5}
        self.ids.other.size_hint = (.2, None)
        self.ids.status.text = '0'
        if not self.isrunning:
            self.isrunning = True
            threading.Thread(target=self.thread_function, daemon=True).start()

    def select_camera(self, facing):
        self.parent.edge_detect.select_camera(facing)


Builder.load_string("""
<AppLayout>:
    edge_detect: self.ids.preview
    EdgeDetect:
        aspect_ratio: '16:9'
        id:preview
    ButtonsLayout:
        id:buttons
           
<ButtonsLayout>:
    GridLayout:
        rows: 2
        BoxLayout:
            size_hint_y: 0.2
            Button:
                id:status
                font_size: sp(20)
                height: pt(self.font_size)
                color: rgba("#43ff64d9")
                text: '0'
                background_color: 0, 0, 0, 0
            Button:
                id:identify
                font_size: sp(20)
                height: pt(self.font_size)
                color: rgba("#43ff64d9")
                text: 'DESCONOCIDO'
                background_color: 0, 0, 0, 0
            Button:
                id:other
                on_press: root.select_camera('toggle')
                height: self.width
                width: self.height
                background_normal: 'camera.png'
                background_down:   'camera.png'
        BoxLayout:
            size_hint_y: 0.12
            TextInput:
                id: input
                text: 'http://192.168.0.7:5001/identificar'
                font_size: sp(20)
                multiline: False
                height: pt(self.font_size)
""")
