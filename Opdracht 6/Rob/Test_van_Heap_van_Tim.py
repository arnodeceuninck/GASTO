from heap import *

Test_Heap = createHeap()
# als dit gelukt is, is er een nieuwe heap aangemaakt

Test_Heap.destroyHeap()
# indien geslaagt, is de heap verwijderd

Test_Heap.isEmpty()
# indien de heap leeg is krijg ik een true waarde terug

Test_Heap.insert("test")
# indien het toevoegen van "test" gelukt is, krijg ik een true waarde terug
# beetje onduidelijk wat er wel en niet mag toegevoegd worden (int/text/...)
# krijg ik een fout als het item niet in de heap zit? Niet uitgelegd.

Test_Heap.getTop()
# geeft het bovenste element terug van de heap
# wat als je deze operatie uitvoert op een heap die niet bestaat? Krijg ik een
# foutmelding?

Test_Heap.remove()
# verwijderd het bovenste element uit een heap
# ik krijg die waarde dan ook terug en een true als het verwijderd is.

Test_Heap.size()
# dit geeft me de totaal aantal elementen in de heap.
