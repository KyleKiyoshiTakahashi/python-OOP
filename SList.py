# Part 1 - recreate SList and Node.  Recreate addNode and printAllValues methods.
# 
# Singly Linked List is one of the most fundamental data structures you'll be using.  
# Using the concepts here, you'll learn how to create other data structure such as Stacks, 
# Queues, Doubly Linked List, Binary Search Trees, Tries, Graphs, etc.  As it's such a critical concept, 
# please re-create the codes demonstrated above without looking at the platform.  Make sure you feel 
# very comfortable with adding a new Node, traversing through the linked list, etc.  
# Once you can create both SList and Node without looking at the codes above, then proceed with Part 2.

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class SList:
	def __init__(self, value):
		node = Node(value)
		self.head = node

	def addNode(self, value):
		node = Node(value)
		runner = self.head
		while(runner.next != None):
			runner = runner.next
		runner.next = node

	def deleteNode(self, value):
    	head = self.node
    	if head.getValue() == value:
        	return SList(head.next)
    	temp = head
    	while temp.next is not None:
        	if temp.next.getValue() == value:
            	temp.next = temp.next.next
				return self
            	temp.next = None
            	return SList(head)
        temp = temp.next


	def printAllValues(self, msg=" "):
		runner = self.head
		print("\n\nhead points to ", id(self.head))
		print("Printing the values in the list ---", msg,"---")
		while(runner.next != None):
			print(id(runner), runner.value, id(runner.next))
			runner = runner.next
		print(id(runner), runner.value, id(runner.next))
			









