from PySimpleGUI import Popup, SetOptions, PopupGetFile, theme, Text, Button, Window

class Simplegui:
    def _dirfile(self, valid_format, title, file_type, file_format):
        VALID_FORMAT = valid_format
        TITLE = title
        FILE_TYPE = file_type
        FILE_FORMAT = file_format

        # Cambiar el tema y configurar los colores y estilos
        theme('DarkTeal4')  # Puedes elegir un tema que te guste

        SetOptions(
            icon='logo.ico',  # Cambiar 'icono.png' al nombre de tu archivo de icono
            button_color=('#ffffff', '#108F5C'),  # Color del texto y color del fondo del botón
            background_color='#162022',  # Color de fondo de la ventana
            text_element_background_color='#162022',  # Color de fondo del texto
            text_color='#ffffff',  # Color del texto
            element_padding=(10, 5),  # Espaciado del elemento
            border_width=2,
            font=('Montserrat', 12)  # Cambiar la fuente a Montserrat y el tamaño
        )

        layout = [
            [Text("Seleccione un archivo:", font=('Montserrat', 14))],  # Cambiar el tamaño de la fuente
            [Button("Examinar", size=(20, 1))],
            [Button("Salir", size=(20, 1))],
        ]

        window = Window("GraphInsight", layout, finalize=True)  # Cambiar el nombre de la ventana

        while True:
            event, values = window.read()

            if event is None or event == "Salir":
                break
            elif event == "Examinar":
                try:
                    filename = PopupGetFile(TITLE, title='GraphInsight', no_window=False,
                                            file_types=((FILE_TYPE, FILE_FORMAT),))
                    if filename and (filename[-4:] == valid_format or filename[-4:] == valid_format.upper()):
                        window.close()
                        return filename
                    else:
                        Popup('Seleccione un archivo .csv válido', keep_on_top=True)
                except Exception as e:
                    Popup(f'Algo salió mal: {str(e)}', keep_on_top=True)

        window.close()
