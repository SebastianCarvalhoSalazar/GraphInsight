from PySimpleGUI import Popup, SetOptions, PopupGetFile, theme
import logging

from simplegui import Simplegui
from utils import Utils
from RSystem import RecomendationSystem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(filename):
    logger.info('_______START_______')
    df = utils._read_data(filename)
    G = recomendationsystem._buildGraph(df)
    df = recomendationsystem._predict(df, G)
    utils._save_data(df, 'output/Recommendations')
    utils._successful_process("¡PROCESS FINISHED SUCCESSFULLY!")
    print(df)
    return print('_______END_______')

if __name__ == '__main__':

    simplegui = Simplegui()
    utils = Utils()
    recomendationsystem = RecomendationSystem()

    filename = simplegui._dirfile('.csv','Import CSV UTF-8 File:','CVS Files','*.csv')
    main(filename)
