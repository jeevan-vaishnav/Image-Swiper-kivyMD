from kivymd.app import MDApp
from kivy.lang import Builder


class ImageSwaper(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

    # Swipe Left
    def on_swipe_left(self):
        self.root.ids.toolbar.title = "Swipe Left"

    # Swipe Right

    def on_swipe_right(self):
        self.root.ids.toolbar.title = "Swipe Right"


        # IF name main
ImageSwaper().run()
