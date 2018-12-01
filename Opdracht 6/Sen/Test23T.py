from TweeDrieTree import *

Test_Tree = create23T()
# Maakt een nieuwe lege 23T aan.

# Wat als er meerdere bomen worden aangemaakt hoe kunnen ze van elkaar worden onderscheid.
insertItem(Test_Tree, "Test")
#Geeft een True terug als het succesvol geïnsert is.

deleteItem(Test_Tree, "Test")
#Geeft een True terug als het succesvol gedelete is.

#Onduidelijk wat er gebeurd indien het laatste element verwijdert wordt.

retrieveItem(Test_Tree, "Test")
#Geeft True terug als het item succesvol is gevonden in de 2-3T en geeft deze waarde ook mee.
#Geeft False indien het niet gevonden is.



#De functies: inorder(), split() en fix() zijn niet publiek waardoor ze niet apart getest moeten worden.

#opmerking:
#De boom kan niet verwijdert worden -> memory leaks.
#Hoe wordt er gecontroleerd of de boom leeg is.