from  ADTcircularLinkedChain import circular_chain
from ADTqueue import  queue
from  BinarySearchTree import BinarySearchTree
from BinarySearchTree import TreeItem

bst = BinarySearchTree(None, None, None)
bst.searchTreeInsert(TreeItem(10, 10))
bst.searchTreeInsert(TreeItem(7, 7))
bst.searchTreeInsert(TreeItem(8, 8))
bst.searchTreeInsert(TreeItem(9, 9))
bst.searchTreeInsert(TreeItem(12, 12))
bst.searchTreeInsert(TreeItem(11, 11))
bst.searchTreeInsert(TreeItem(13, 13))
bst.searchTreeRetrieve(11)
bst.searchTreeDelete(12)
bst.print()

q = queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(1)
q.getFront()
q.dequeue()
q.visualize()

clchain = circular_chain()
clchain.insert(0, 5)
clchain.insert(1, 6)
clchain.insert(2, 2)
clchain.insert(3, 345)
clchain.insert(1, 10)
clchain.insert(5, 54)
clchain.retrieve(0)
clchain.delete(5)  # removes the item at index 5
clchain.visualize()