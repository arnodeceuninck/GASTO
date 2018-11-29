from TweeDrieTree import *

Test_Tree = create23T()
# Onduidelijk wat de inputs zijn bij create23T().
# rootKey = 0 logischerwijs als root ok, maar wat als mensen eender welk getal ingeven?


# Bij de eerste twee operaties is het misschien handig om in de haken te
# definiëren welke boom er verwijderd wordt. (Als er meerdere bomen aangemaakt mogen worden)
isEmpty()
# returns true of false als de boom leeg is? --> niet duidelijk

destroy23T()
# Returns true of false als de boom volledig is verwijderd? --> niet duidelijk

insertItem(Test_Tree, "test")
# Returns niets

delete(Test_Tree, "test")
# Als het item correct is verwijderd dan is de return waarde true, als het item
# niet in de boom zit dan is het false

retrieveItem(Test_Tree, "test")
# Returns de waarde true als het item gevonden is en false indien dat niet zo is.
# De waarde wordt ook terug gegeven als het gevonden is. Er wordt niet vermeld
# wat er terug gegeven wordt indien het item niet in de boom zit.

## Geloof dat inorder(Test_Tree) gebruikt wordt voor het doorlopen van de boom
## bij de operatie retrieveItem(), en publiek niet gebruikt wordt / mag worden.
## Dus er wordt dan ook geen test voor geschreven.

## De split(Test_Tree) wordt enkel gebruikt tijdens de operatie insertItem() en
## is dus publiek niet te gebruiken, en moet het daarom ook niet getest worden.

## fix(n) wordt enkel gebruikt bij de operatie delete() en is niet publiek dus
## moet er ook geen test voor geschreven worden.
