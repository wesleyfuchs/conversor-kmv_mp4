import subprocess
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

# define o tamanho mínimo da janela
Window.minimum_width, Window.minimum_height = 800, 600

from kivy.uix.gridlayout import GridLayout

class VideoConverter(BoxLayout):

    def __init__(self, **kwargs):
        super(VideoConverter, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.titulo_label = Label(text='Conversor mkv -> mp4', font_size=24, size_hint=(1, 0.2))
        self.add_widget(self.titulo_label)
        
        self.file_path_label = Label(text='', size_hint=(1, 0.2))
        self.add_widget(self.file_path_label)
        
        self.grid_layout = GridLayout(cols=2, size_hint=(1, 0.05))
        self.add_widget(self.grid_layout)
        
        self.choose_file_button = Button(text='Escolher arquivo', size_hint=(0.5, 1), font_size=16, background_color=[0, 1, 1, 1])
        self.choose_file_button.bind(on_press=self.show_file_chooser)
        self.grid_layout.add_widget(self.choose_file_button)
        
        self.convert_button = Button(text='Converter', size_hint=(0.5, 1), font_size=16, background_color=[0, 1, 1, 1])
        self.convert_button.bind(on_press=self.convert_video)
        self.grid_layout.add_widget(self.convert_button)
                
        self.source_file = ''  # Atributo para armazenar o caminho do arquivo selecionado

    
    def show_file_chooser(self, instance):
        self.file_chooser = FileChooserListView()
        self.file_chooser.filters = ['*.mkv'] # Adiciona filtros para mostrar apenas arquivos MP4 e MKV
        self.file_chooser.path = 'C:/Users/uesley/Documents' # Define o diretório inicial do FileChooser
        self.file_chooser.bind(selection=self.update_label)
        
        # Criação do popup
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(self.file_chooser)

        self.popup = Popup(title='Selecione o arquivo', content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()
        
        
    def update_label(self, instance, path):
        # Atualiza o texto do label com o diretório selecionado
        self.file_path_label.text = path[0]


    def convert_video(self, instance):
        source_file = self.file_chooser.selection[0]
        target_file = os.path.splitext(source_file)[0] + '_convertido.mp4'
        
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
