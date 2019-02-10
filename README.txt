########################################################
############# INSTALLATION ANIM PICKER #################
########################################################


1) Fermer Maya

2) Extraction de l'archive:
   - Dézipper l'archive animPicker dans un répertoire. Un bon choix est le répertoire de scripts de maya, dans "C:\Users\<username>\Documents\maya\2018\scripts\animPicker"
   - Attention à ne pas avoir deux dossiers animPicker imbriqués, du genre "C:\...\scripts\animPicker\animPicker"
   - Garder de côté le chemin du dossier animPicker, on en a besoin plus tard.
   
3) Modification du fichier animPicker.py (dans le dossier animPicker)
   - Editer le fichier animPicker.py (avec le bloc-note par exemple)
   - Tout en bas du fichier, modifier la ligne qui commence par "path =", en la complétant avec le chemin adéquat vers animPicker.
   - Enregistrer les changements

4) Configurer la variable d'environnement PYTHONPATH :
   - Depuis le menu démarrer, chercher "environnement" puis sélectionner "Modifier les variables d'environnement système"
   - Dans la fenêtre qui s'ouvre, cliquer en bas sur "Variables d'environnement"
   - Dans la nouvelle fenêtre, sur la partie du bas, chercher la variable PYTHONPATH. Si elle existe, la sélectionner puis cliquer sur "Modifier" ou sinon cliquer sur "Nouvelle"
   - Le nom de la variable doit être PYTHONPATH (en majuscule), et la valeur doit être le chemin du dossier précédemment créé (i.e. C:\Users\<username>\Documents\maya\2018\scripts\animPicker)
   - Valider pour fermer toutes ces fenêtres
   
5) Ajouter le script à Maya
   - Ouvrir Maya
   - Dans un shelf, créer un nouvel item
   - Pour utiliser un logo, renseigner le fichier logo_only.png qui est dans le répertoire animPicker
   - Dans le contenu du script, sélectionner Python pour le langage et renseigner le script ci-dessous
   - Adapter les chemins qu'il y a dans les scripts
   
import sys
sys.path.append(r'C:\Users\<username>\Documents\maya\2018\scripts\controllerSelector')
import controllerSelector
reload(controllerSelector)
controllerSelector.main(r'C:\Users\<username>\Documents\maya\2018\scripts\controllerSelector\\')

6) Enjoy =)