#ndef push(stack,value):
#	stack.append(value)

#def pop(stack):
#	return stack.pop()

#my_stack = [ ]
#push(my_stack, 'a')
#push(my_stack,'b')
#push(my_stack,'c')
#print(my_stack)


#pop(my_stack)
#print(my_stack)

###--------------------------------------------------------------

## set { }




##-------------------------------------	DICTIONARIES -----------------------


## ordered = 
## mutable = වෙනස් කළ හැකි
## indexed = 
## unique = අද්විතීය

#my_first_dict = dict ()

#scores = {'Saman':65,'Kamal':45, 'Nimal':89}
#print(scores['Saman'])
#print(scores['Nimal'])

#		PYTHON DICTIONARY OPERATIONS 

#1)Adding an element 
#2)Updating an element
#3) Removing an element 
#4) Removing all elements
#5) Get the list of all keys 
#6) Get the list of all values



#scores = {'Saman':65,'Kamal':45, 'Nimal':89}
#1) adding an element 
#scores['Amaaya'] = 78
#print(scores)
#>>>  {'Saman':65,'Kamal':45, 'Nimal':89,'Amaaya':78}

#2) updating an element
#scores['Saman'] = 100
#print(scores)
#>>>  {'Saman':100,'Kamal':45, 'Nimal':89,'Amaaya':78}

#3) Removing an element 
#scores = {'Saman':65,'Kamal':45, 'Nimal':89}
#scores.pop('Saman')
#print(scores)
#>>>  {'Kamal':45, 'Nimal':89}

#4) Removing all elements
#scores = {'Saman':65,'Kamal':45, 'Nimal':89}
#scores.clear()
#print(scores)
#>>> {}

#5) Get the list of all keys
#scores =  {'Saman':65,'Kamal':45, 'Nimal':89}
#all_keys = list(scores.keys())
#print(all_keys)
#>>> ['Saman','Nimal','Kamal']

#6) Get the list of all values
#scores =  {'Saman':65,'Kamal':45, 'Nimal':89}
#all_values = list(scores.values())
#print(all_values)
#>>> [65,45,89]

#		Iterating through a Dictionary 

#scores = {'Saman':65,'Kamal':45, 'Nimal':89}

#print("-----------------------------------")
#for key in scores:
#	print(key,scores[key])

#d = {"john":40, "peter":45}
#print(list(d.keys()))

###------------------------------------------------------------------------------

##		PYTHON TUPLES


#Insertion, deletion, and Update 

		# Because tuples are immutable .
		# Once a tuple is created, it cannot be modified .
		# Hence, insertion, deletion and update are not possible.

#Lists vs tuples 

		# List and tuples are very similar to each other 
		# List are versatile than Tuples 
			# Lists can be updated while tuples cannot be 
		# List have more built-in functions. 

		# Tuples are memory efficient.

#import sys 
#my_list = [1,2,3,4,5]
#my_tuple = (1,2,3,4,5)

#print(sys.getsizeof (my_list))   ###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#>>> 104
#print(sys.getsizeof (my_tuple))   ####$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#>>> 80


## 			TUPLE OPERATIONS

#1) Length 

#len((1,2,3,4,))
#>>> 4

#2) Concatenation 

#a=(1,2,3)
#b=(4,5,6)
#a+b
#>>> (1,2,3,4,5,6)

#3) Repetition 
#("Hi") * 4
#>>> ("HI", "HI", "HI", "HI", )

#4) Membership 
#3 in (1,2,3)
#>>> True 

#5) Iteration 
#for x in (1,2,3):
#		print(x)
#>>>
#1
#2
#3

##------------------------

#				SUMMARY 

#Tuple is sequence data type
#-----------------
#------------------


#--------------------------------	


#####################################################################################


#class monster:
#	def __init__(self, age, name):
#		# instance of attributes
#		self.age = age
#		self.name = name

	# instance of method 
#	def steal(self, warrior):
#		warrior.loose_stick()


## 
#A Sample Python Class age


#class Monster:
#	# class attributes
#	color = "black"
#
#	def __init__(self, age, name):
#		# instance attributes
#		self.age = age 
#		self.name = name
#
#		self._is_innocent = None
#
	# instance method 

#	def steal(self, warrior):
#		warrior.loose_stick()



# creating an instance
#monster1 = Monster(15, "mon1")

# accessing attributes
#print(monster1.age)

# changing attribute value
#monster1.age = 10

#print(monster1.age)

# creating another instance 
#monster2 = Monster(10, "mon2")

## Constructors 
#-----------------------------------------------------

#(1)----------

#def __init__(self, age, name):
#	# instance attributes
#	self.age = age
#	self.name = name 
#	self._number_of_sticks = 0
#

#(2)------------

#def __init__(self, age, name="mon1"):
#	# instance attributes 
#	self.age = age 
#	self.name = name 
#	self._number_of_sticks = 0
#
		
#(3)--------------

#def __init__(self):
#	# instance attributes
#	self.age = 10
#	self.name = "mon1"
#	self._number_of_sticks = 0


#--------------------------------------------------

## Methods 

#(1)

# instance method in monster class
#	def change_warrior_age(self, warrior):
#		new_age = 5
#		warrior.age = new_age


#(2)

# instance method in monster class
#	def steal(self, warrior):
#		warrior.loose_stick()
#		self._number_of_sticks += 1


#----------------------------------------------------------------------

#2.2 OOP Principles 

#	Object
#	Class
#	Encapsulation
#	Inheritance
#	Abstraction
#	Polymorphism


#At the End of this Lecture 
#	You should be able to;
#		Apply the two OOP principles encapsulation and inheritance in
#		OO Program development.


#							---------------

#			Encapsulation in Python
#
#	** Encapsulation hides the implementation details.
#	** Class announces some operation (mehods) available
#		for its clients-Its public interface.

		
#class warrior:

#	def __init__(self, name):
#		# instance attributes
#		self.name = name								--
#		self._age = 10 <--------- private by convention  |--|Instance 
														 |--Attributes|
														--	
				
	# using property decorator - Getter function
#	@property
#	def age(self):
#		return self._age 		
#					<----------- |Getter|
#	@age.setter
#	def age(self, age):
#		if age > 10:
#			self._age = age
#		
#		else:		<----------- |Setter|
#			print("Age should be greater than zero")




#class Warrior:

#	 def __init__(self,name):
#	 	# instance attribute
#	 	self.name = name
#	 	self._age = 0

	 # using property decorator 
	 # getter function 
#	 @property
#	 def age(self):
#	 	return self._age
#	 
#	 @age.setter
#	 def age(self, age):
#	 	if age > 0:
#	 		self._age = age
#
#	 	else:
#	 		print("Age should be greater than zero")

#warrior = Warrior("warr1")

#warrior.age = 15
#print(warrior.age)

#			------------------------------------------------------


#Encapsulation Benifits
	
#	** Encapsulation allows adding some logic when 
#		accessing the client's data 																																'
#			E.g., validation on modyfing a property value.

#	** Hidding implementation details reduces complexit, thus 
#		easier manitenance		


#-----------------------------------------------------------------------------------


#			2.3 OOP Principles 2

#At the End of this Lecture
#	** You should be able to,

#			** Apply the two OOP principles Abstraction and Polymorphism in
#				OO Program development.
				


##---------------------- 2 is over --------------------------------------------

## --------------  3 - WORKING WITH DATA -------------------------------

##  3.1 Database Basics ||


Learning Outcomes 


	** After watching this video you will be able to:

		1: Define Database and its main functionalities.
		2: Explain the evolution of database till RDBMS (Realational Database 
			Management Systems) and the rationals.
		3: Compare and contrast the following.

				1. Flat files Databases
				2. Navigational Databases
				3. Realational Databases


------------- 
How Data is Stored in a Disk?

	Hard Drive Structure
	A: Track
	B: Sector
	C: Sector of a Track
	D: Cluster

A cluster (sometimes also called block) is a unit of disk space allocation for
files and directories.

The sector is the minimum storage unit of a had drive. 


------------------------

Let''s create a File in a HDD (Hard Disk Drive)

	** Cluster: 512 Bytes.
	** We ask OS to create a new empty text file.
	** It may allocate/reserve 512 Bytes for this new file.

Let's' Write More to That File

	** Allocated size is 512 Bytes for this new file.
	** We typed for 682 Bytes and saved.
	** Since initial allocation is not enough, it will have to
		 allocate another cluster.



	Lets Read That File

		** Note the reading is not completely sequential.
		** 


***** What is a Database (DB) ?

	** A database is an oraganized collection of strucured 
		inforamtion, or data, typically stored electronnically in a
		computer system. 

	** A database is usually controlled by a Database 
		Management System (DBMS)

	** Together, the data and the DBSM, along with the 
		applications that are associated with them, are referred
		to as a database system. 

		* Often shortened to just database.



----------------------

				Let Us Create a Simple Database

		** Lets assume we have the following data
		** Use CSV file format to create a simple 'flat' Database.
			* Comma Seperated Files: CSV

		
















