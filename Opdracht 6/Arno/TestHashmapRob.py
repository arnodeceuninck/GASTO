from hashmap import *

# Probleem bij dit hashmap-contract:
# Er staat nergens in het operation contract iets gespeciefierd over keys, hoewel dit wel echt noodzakelijk is

# In deze tests zal ik er dus vanuit gaan dat er een "HashmapType" bestaat dat bestaat uit een key en een value

test_hashmap = createHashmap()
hashmap_object1 = new hashmap_object("test1", "Dit is de tekst die hoort bij de zoeksleutel test1")
hashmap_object2 = new hashmap_object("test2", "Dit is de tekst die hoort bij de zoeksleutel test2")
hashmap_object3 = new hashmap_object("test3", "Dit is de tekst die hoort bij de zoeksleutel test3")

# Test insert
test_hashmap.tableInsert(hashmap_object1)
if(test_hashmap.tableRetrieve("test1")[1] == "Dit is de tekst die hoort bij de zoeksleutel test1"){
    print("Test passed: test1")
} else {
    print("Test failed: test1")
}

# Test retrieve onbestaand element
if(test_hashmap.tableRetrieve("test2")[1] == False and test_hashmap.tableRetrieve("test1")[1] == "Dit is de tekst die hoort bij de zoeksleutel test1"){
    print("Test passed: test2")
} else {
    print("Test failed: test2")
}

# Test delete
test_hashmap.tableInsert(hashmap_object2)
test_hashmap.tableInsert(hashmap_object3)
test_hashmap.tableDelete(hashmap_object3)
if(test_hashmap.tableRetrieve("test3")[1] == False and test_hashmap.tableRetrieve("test1")[1] == "Dit is de tekst die hoort bij de zoeksleutel test1" and test_hashmap.tableRetrieve("test2")[1] == "Dit is de tekst die hoort bij de zoeksleutel test2"){
    print("Test passed: test3")
} else {
    print("Test failed: test3")
}

# hashfunctie() wordt nooit publiek gebruikt, en is dus ook niet nodig om getest te worden.
