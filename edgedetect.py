from kivy.clock import mainthread
from kivy.graphics import Color, Rectangle
from kivy.graphics.texture import Texture
import numpy as np
import cv2
from camera4kivy import Preview

class EdgeDetect(Preview):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.analyzed_texture = None
        self.detect = False
        self.name = ""
        self.image = None

    def detected(self):
        return self.detect
    
    def recognition(self, name):
        self.name = name

    def save(self):
        cv2.imwrite('rostro.jpg', self.image)

    def analyze_pixels_callback(self, pixels, image_size, image_pos, scale, mirror):
        rgba   = np.fromstring(pixels, np.uint8).reshape(image_size[1], image_size[0], 4)
        self.image = rgba.copy()
        gray_img = cv2.cvtColor(rgba, cv2.COLOR_BGR2GRAY)
        haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces_rect = haar_cascade.detectMultiScale(gray_img, 1.3, 5)
        self.detect = False
        for (x, y, w, h) in faces_rect:
            self.detect = True
            cv2.rectangle(rgba, (x, y), (x+w, y+h),(0,255,0),2)
            cv2.putText(rgba, self.name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (36,255,12), 2)
        pixels = rgba.tostring()
        self.make_thread_safe(pixels, image_size)


    @mainthread
    def make_thread_safe(self, pixels, size):
        if not self.analyzed_texture or self.analyzed_texture.size[0] != size[0] or self.analyzed_texture.size[1] != size[1]:
            self.analyzed_texture = Texture.create(size=size, colorfmt='rgba')
            self.analyzed_texture.flip_vertical()
            self.analyzed_texture.flip_horizontal()
        if self.camera_connected:
            self.analyzed_texture.blit_buffer(pixels, colorfmt='rgba') 
        else:
            self.analyzed_texture = None
            
    def canvas_instructions_callback(self, texture, tex_size, tex_pos):
        if self.analyzed_texture:
            Color(1,1,1,1)
            Rectangle(texture= self.analyzed_texture,size = tex_size, pos = tex_pos)










