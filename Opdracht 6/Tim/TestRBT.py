
#Er word een nieuwe boom aangemaakt
test_RB = createRBT()

#Test of de Boom leeg is
test_RB.IsEmpty()
#omdat de boom net is aangemaakt moet dit true zijn

#Insert test
test_RB.insert(Type, 50)
test_RB.insert(Type, 60)
test_RB.insert(Type2, 40)
#De boom zou nu moeten bestaan uit 1 4node met geen kinderen en de volgende items op deze volgorde 40 50 60

test_RB.IsEmpty()
#omdat er nu items zijn toegevoegd moet deze functie false terug geven

test_RB.insert(Type, 55)
#De 4node zit vol en dus moeten we de 55 toevoegen als kind, de verbinding tussen 60 en 55 is een kind verbinding
#                           50
#                         /   \
#                        /     \
#                      40       60
#                              /
#                             /
#                           55

test_RB.delete(60)
#Het element met key 60 zal verwijderd worden uit de zoekboom en het 55 element word opgenomen in de node
#                           50
#                         /   \
#                        /     \
#                      40       55

test_RB.retrieve(40)
#deze operatie moet type2 terug geven

test_RB.getroot()
#Het item van key 50 word gereturned

test_RB.insert(type, 30)
test_RB.insert(type, 20)
test_RB.insert(type, 100)

test_RB.inorderTraverse(print)
#De boom zal de nodes in volgende volgorde afprinten
#20 30 40 50 55 100

test_RB.preorderTraverse(print)
#De boom zal de nodes in volgende volgorde afprinten
#50 30 20 40 55 100

test_RB.postorderTraverse(print)
#de boom zal de nodes in volgende volgorde afprinten
#20 40 100 30 50 55
