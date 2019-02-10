########################################################
############# INSTALLATION ANIM PICKER #################
########################################################


1) Fermer Maya

2) Extraction de l'archive:
   - D�zipper l'archive animPicker dans un r�pertoire. Un bon choix est le r�pertoire de scripts de maya, dans "C:\Users\<username>\Documents\maya\2018\scripts\animPicker"
   - Attention � ne pas avoir deux dossiers animPicker imbriqu�s, du genre "C:\...\scripts\animPicker\animPicker"
   - Garder de c�t� le chemin du dossier animPicker, on en a besoin plus tard.
   
3) Modification du fichier animPicker.py (dans le dossier animPicker)
   - Editer le fichier animPicker.py (avec le bloc-note par exemple)
   - Tout en bas du fichier, modifier la ligne qui commence par "path =", en la compl�tant avec le chemin ad�quat vers animPicker.
   - Enregistrer les changements

4) Configurer la variable d'environnement PYTHONPATH :
   - Depuis le menu d�marrer, chercher "environnement" puis s�lectionner "Modifier les variables d'environnement syst�me"
   - Dans la fen�tre qui s'ouvre, cliquer en bas sur "Variables d'environnement"
   - Dans la nouvelle fen�tre, sur la partie du bas, chercher la variable PYTHONPATH. Si elle existe, la s�lectionner puis cliquer sur "Modifier" ou sinon cliquer sur "Nouvelle"
   - Le nom de la variable doit �tre PYTHONPATH (en majuscule), et la valeur doit �tre le chemin du dossier pr�c�demment cr�� (i.e. C:\Users\<username>\Documents\maya\2018\scripts\animPicker)
   - Valider pour fermer toutes ces fen�tres
   
5) Ajouter le script � Maya
   - Ouvrir Maya
   - Dans un shelf, cr�er un nouvel item
   - Pour utiliser un logo, renseigner le fichier logo_only.png qui est dans le r�pertoire animPicker
   - Dans le contenu du script, s�lectionner Python pour le langage et renseigner le script ci-dessous
   - Adapter les chemins qu'il y a dans les scripts
   
import sys
sys.path.append(r'C:\Users\<username>\Documents\maya\2018\scripts\controllerSelector')
import controllerSelector
reload(controllerSelector)
controllerSelector.main(r'C:\Users\<username>\Documents\maya\2018\scripts\controllerSelector\\')

6) Enjoy =)