Pour l'installer :

Renseigner la variable d'environnement PYTHONPATH avec le chemin d'installation du script.
Par exemple : C:\Users\<username>\Documents\maya\2019\scripts\controllerSelector

import sys
sys.path.append(r'C:\Users\sylva\Documents\maya\2019\scripts\controllerSelector')
import controllerSelector
reload(controllerSelector)
controllerSelector.main(r'C:\Users\sylva\Documents\maya\2019\scripts\controllerSelector\\')