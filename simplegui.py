from PySimpleGUI import Popup, SetOptions, PopupGetFile, theme
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Simplegui:

    def _dirfile(self, valid_format, title, file_type, file_format):

        VALID_FORMAT = valid_format
        TITLE = title
        FILE_TYPE = file_type
        FILE_FORMAT = file_format

        logger.info('Select a file...')

        theme('Dark')
        SetOptions(icon='app.ico', button_color=('#E9E9E9','#126B79'), background_color = '#E7E0E1',
                   border_width=2, text_element_background_color='#E7E0E1', text_color='Black', use_ttk_buttons=True,
                   font=('Segoe Ui',10))

        try:
            filename = PopupGetFile(TITLE,title='Data Scrubber', no_window = False, file_types=((FILE_TYPE,FILE_FORMAT), ))
        except:
            Popup('Something Went Wrong X__X', keep_on_top=True)

        if filename == None:
            Popup('No valid filename', keep_on_top=True)
            exit()
        elif (filename[-4:] == valid_format or filename[-4:] == valid_format.upper()):
            return filename
        else:
            Popup('Select a .csv file', keep_on_top=True)
            return exit()
