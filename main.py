from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.clock import Clock
from applayout import AppLayout
from android_permissions import AndroidPermissions

if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android import mActivity
    View = autoclass('android.view.View')

    @run_on_ui_thread
    def hide_landscape_status_bar(instance, width, height):
        if Window.width > Window.height: 
            option = View.SYSTEM_UI_FLAG_FULLSCREEN
        else:
            option = View.SYSTEM_UI_FLAG_VISIBLE
        mActivity.getWindow().getDecorView().setSystemUiVisibility(option)
elif platform != 'ios':
    from kivy.config import Config 
    Config.set('input', 'mouse', 'mouse, disable_multitouch')

class MyApp(App):
    
    def build(self):
        self.layout = AppLayout()
        if platform == 'android':
            Window.bind(on_resize=hide_landscape_status_bar)
        return self.layout

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def start_app(self):
        self.dont_gc = None
        Clock.schedule_once(self.connect_camera)

    def connect_camera(self,dt):
        self.layout.edge_detect.connect_camera(analyze_pixels_resolution = 720,enable_analyze_pixels = True,enable_video = False)

    def on_stop(self):
        self.layout.edge_detect.disconnect_camera()

MyApp().run()

