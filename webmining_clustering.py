from sources.TextClastering import *
import sys
import pymorphy2
from sources.utils import *

morph = pymorphy2.MorphAnalyzer()
configurations = readConfigurationFile("configuration.cfg")

def main(param):
    # some filler code that uses the parsed args
    print("Success!")
    dialogConfigClastering = DialogClastering(param, morph, configurations, self)

if __name__ == '__main__':
    main(sys.argv[1])