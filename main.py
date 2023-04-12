import subprocess
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
from kivy.uix.label import Label

class VideoConverter(BoxLayout):

    def __init__(self, **kwargs):
        super(VideoConverter, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        dir_padrao = os.path.expanduser("~") + '/Documents'
        self.file_chooser = FileChooserIconView(path=dir_padrao)
        self.file_chooser.dirselect = True
        self.add_widget(self.file_chooser)
        
        self.convert_button = Button(text='Convert')
        self.convert_button.bind(on_press=self.convert_video)
        self.add_widget(self.convert_button)
    
        # self.status_label = Label(text='')
        # self.add_widget(self.status_label)

    
    def convert_video(self, instance):
        source_file = self.file_chooser.selection[0]
        target_file = os.path.splitext(source_file)[0] + '.mp4'
        
        cmd = ['ffmpeg', '-i', source_file, '-codec', 'copy', '-map', '0', '-movflags', '+faststart', target_file]
        subprocess.call(cmd)
        
        # Altera o texto do botão para "Concluído"
        self.convert_button.text = "Concluído"
        # Desativa a função de clique do botão
        self.convert_button.disabled = True

class VideoConverterApp(App):

    def build(self):
        return VideoConverter()

if __name__ == '__main__':
    VideoConverterApp().run()
