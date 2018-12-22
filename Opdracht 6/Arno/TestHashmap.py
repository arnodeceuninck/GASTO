from hashmap import *

# Probleem bij dit hashmap-contract:
# Er staat nergens in het operation contract iets gespeciefierd over keys, hoewel dit wel echt noodzakelijk is

test_hashmap = createHashmap()

# Test insert
test_hashmap.tableInsert("test1")
if(test_hashmap.tableRetrieve("test1")[1] == "test1"){
    print("Test passed: test1")
} else {
    print("Test failed: test1")
}

# Test retrieve onbestaand element
if(test_hashmap.tableRetrieve("test2")[0] == False and test_hashmap.tableRetrieve("test1")[1] == "test1"){
    print("Test passed: test2")
} else {
    print("Test failed: test2")
}

# Test delete
test_hashmap.tableInsert("test2")
test_hashmap.tableInsert("test3")
test_hashmap.tableDelete("test3")
if(test_hashmap.tableRetrieve("test3")[0] == False and test_hashmap.tableRetrieve("test1")[1] == "test1" and test_hashmap.tableRetrieve("test2")[1] == "test2"){
    print("Test passed: test2")
} else {
    print("Test failed: test2")
}

# hashfunctie() wordt nooit publiek gebruikt, en is dus ook niet nodig om getest te worden.
