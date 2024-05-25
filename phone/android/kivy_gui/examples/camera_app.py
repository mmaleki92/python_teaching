from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CameraApp(App):
    def build(self):
        self.camera_obj = Camera(play=True)
        self.camera_obj.resolution = (640, 480)  # Adjust resolution as needed

        # Button to capture the image
        capture_button = Button(text="Capture")
        capture_button.size_hint_y = 0.2
        capture_button.bind(on_press=self.capture)

        # Layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.camera_obj)
        layout.add_widget(capture_button)

        return layout

    def capture(self, *args):
        # Capturing and saving the current frame from the camera
        self.camera_obj.export_to_png('photo.png')
        print("Captured image saved as photo.png")

if __name__ == '__main__':
    CameraApp().run()
