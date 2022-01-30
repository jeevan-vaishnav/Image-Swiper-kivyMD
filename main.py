from kivymd.app import MDApp
from kivy.lang import Builder


class ImageSwaper(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')


# IF name main
ImageSwaper().run()
