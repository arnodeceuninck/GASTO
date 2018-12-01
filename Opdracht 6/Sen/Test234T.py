from TweeDrieVierTree import *

Test_Tree = create234T()
#Maakt een nieuwe 234T aan.

# Wat als er meerdere bomen worden aangemaakt hoe kunnen ze van elkaar worden onderscheid.
destroy234T()
#Verwijdert de 234T.

# Wat als er meerdere bomen worden aangemaakt hoe kunnen ze van elkaar worden onderscheid.

isEmpty()
# Geeft True terug als de 234T leeg is en geeft False terug indien er nog data in de 234T zit.

insert("Test", 0)
#Geeft True terug indien het item succesvol in geïnsert.
#Geeft False terug indien de operatie niet gelukt is.

remove(0)
#Verwijdert het element "Test", indien het succesvol is verwijdert geeft het True terug anders False.

retrieve(0)
#Geeft het element True indien het succesvol het element "Test" heeft teruggegeven.
#Geeft False terug indien de operatie niet succesvol was.

getRoot()
#Geeft de root terug.
#Onduidelijk wat er gebeurd indien de Root leeg is.



# De functies inorderTravers(), preorderTraverse() en postorderTravers() zijn geen publieke functies,
# deze moeten niet getest worden.
