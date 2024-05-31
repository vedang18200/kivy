from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
class demoapp (MDApp):
    def build(self):
        label=MDLabel(text='Hello world',halign='center',theme_text_color='Custom',text_color=(0,0,1,1),font_style='H6')
        icon_label=MDIcon(icon='library-video',halign='center')
        return icon_label
    
    
demoapp().run()

