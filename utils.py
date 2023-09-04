from PySimpleGUI import Popup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Utils:

    def _read_data(self, filename):
        """ _read_data: Funcion desarrollada para leer archivos csv utf-8 con ';' como delimitador.
            Input: Ruta del archivo
            Outpu: DataFrame
        """
        logger.info('Reading file: {}'.format(filename))
        df = pd.read_csv(filename, sep=';')
        return df

    def _fillna(self, df):
        """ _fillna: Funcion desarrollada para llenar valores faltantes con "NR".
            Input: DataFrame
            Output: DataFrame
        """
        logger.info('Filling NaN values')
        df = df.fillna("NR")
        return df

    def _save_data(self, df, filename):
        """ _save_data: Funcion Desarrollada para guardar archivos ".csv".
            Input: DataFrame
            Output: .csv file
        """
        logger.info('Saving data...')
        df.to_csv(filename + '.csv', index=False, header=True, sep=";", encoding='utf-8-sig')
        return filename


    def _successful_process(self, message):
        """ _save_data: Funcion Desarrollada para desplegar Popup de finalización de ejecución del algoritmo.
            Input: String
            Output: Popup
        """
        Popup(message, keep_on_top=True)
