from os import walk

def import_folder(path):
    for informarion in walk(path):
        print(informarion)

import_folder("../graphics/character/run")