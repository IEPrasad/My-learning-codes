##			11 VIDEO CONTENT
	## PYTHON SET { }

#x = {12,34,45,56}
#print(x)
##>>> {56, 34, 12, 45}

##1 mehi elemnts walata index numbers natha 
	# enisa piliwelata print nowe
#x= {45,1,"opportiunity",2,3,4,5}
#print(x)
##>>> {1, 2, 3, 4, 5, 'opportiunity', 45}

##2 elements add kirima
	## ekak add karana wita ""add""
		## kihipayak add karana wita ""update"" list ekak athule awashya elements laba diya yuthuwe.

#x.add(12)
#x.update([12,23,45,"Nimala"])

##3 element remove kirimata remove bawitha karaii

#x= {1,2,3,4,5,6,7}
#x.remove(7)
#print(x)
## >>> {1,2,3,4,5,6}

##4 clear ()
#x.clear()

##5 del x

##6 list saha tuple set bawata pariwarthanaya kirima

#x= [12,43,45,56]
#y = tuple(x)
#print(y)
#z=set(x)
#print (z)
#a= list(z)
#print(a)

#>>> (12, 43, 45, 56)
#	{56, 43, 12, 45}
#	[56, 43, 12, 45]


##7 type()

#x= ["name",12,334]
#print(type(x))
##>>> <class 'list'>

###---------------------------------------------------

## mema set wala CHEDANAYA saha MELAYA laba ganima

#x = {1,2,3,4,5,6}
#y = {2,4,6,8}

#print(x & y)
##>>> {2, 4, 6}
#print(x.intersection(y))
##>>> {2, 4, 6}

#### ihatha krama deka maginnma "|CHEDANAYA |" laba ganimata puluwani

#print (x | y)
#print(x.union(y))
##>>>
##	{1, 2, 3, 4, 5, 6, 8}
##	{1, 2, 3, 4, 5, 6, 8}
##>>> 
## salakiya yuthuii set waladi kulaka nithi bawitha we,enam melayedi 2,4,6 wani dekehima athi elements depaarak yedi natha

#x= {2,2,2,2,}
#print(x)
##>>> {2}

##-----------------------------------------------------------------------------------------------------------------------------------------------------

##				12 VIDEO CONTENT 
			## DICTIONARIES
## MEHIDI YUGAL KARAPU ELEMENTS ATHA.

#x = {"Name":"Kamal","Marks": 23,"Age" : 21}
#print(x)
##>>> {'Name': 'Kamal', 'Marks': 23, 'Age': 21}

#print (x["Name"])
##>>> Kamal 
#print(x["Age"])
##>>> 21

#print(x.items())
##>>> dict_items([('Name', 'Kamal'), ('Marks', 23), ('Age', 21)])

#print(x.values())
##>>> dict_values(['Kamal', 23, 21])

#print(x.keys())
##>>> dict_keys(['Name', 'Marks', 'Age'])

#print (len(x))
##>>> 3

#x["Grade "] = "seven"
#print(x)
##>>> {'Name': 'Kamal', 'Marks': 23, 'Age': 21, 'Grade ': 'seven'}
### melesa elements add kala hakiwe.

##x[(12,23)] = 23
#print(x)
##>>> {'Name': 'Kamal', 'Marks': 23, 'Age': 21, (12, 23): 23}

#x[(12,23,34,)] = 12,23,34
#print(x)
##>>> {'Name': 'Kamal', 'Marks': 23, 'Age': 21, (12, 23, 34): (12, 23, 34)}

## element iwath kirimata pop()  bawitha karaii
#x.pop("Name")
#print(x)
##>>> {'Marks': 23, 'Age': 21}

## x.clear()
## del x

##--------------------------------------------------------------------------------------------------------------------

## 13 VIDEO CONTENT
##		Python Tutorial - 13 | Slicing and Negative Indexing in Python | 

## Slicing waladi kotasak print kara ganima sidu kala hakiwe

#lst = [1,2,3,4,5,6]
#print(lst[2:4])
##>>> [3,4]

## slicing wala igena ganimata boho karunu nathath itha wadagath we.

## 1 Method:
		# lst [start :end+1]

## 2 Method:
		# lst[start : end+1: step]

#lst = [1,2,3,4,5,6,7,8,10]
#print(lst[1:6:2])
##>>> [2, 4, 6]

### NEGATIVE INDEXING 
## mehidi awasana element ekehi sita aramba karana athara eya -1 n aramba we.

##mehidi dia ihatha foramat ekama we

## Method 1
		# lst[start: end+1]
## Method 2
		# lst[start:end+1: step]

#lst = [2,4,6,8]
#print(lst[-1: :-1])

## >>> [8, 6, 4, 2]
##-----------------------------------------------------------------------------------------------------------------

## 		14 VIDEO CONTENT
		##  Python Tutorial - 14 | Python While Loop |

#i=0
#while (i<=6):
#	i+=1;
#	print("Hello World!");

#sum = 0
#i = 0
#while (i<=5):
#	number = int(input("Enter Value: "))
#	i+=1
#	sum = sum + number

#print("sum of all enter the numbers:",sum)

##$$$ while loop ekak kriyathmaka wenne contdition eka true wana wita pamani.



##>>> 
##-----------------------------------------------------------------------------------------------------------------------

##  15 VIDEO CONTENT

##				Python Tutorial - 15 | Python For Loop |

## for loop walata conditions natha

#x = [1,2,3,4,5,6]

#for num in x:
#	print(x)
#>>> 
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6]
##>>>>> 

#	print(num)
##>>> 
#1
#2
#3
#4
#5
#6
##>>>>>
## melesa labe 

##------------------------------------------


##how to us for loop with dictionaries

#for i in x:	
#	print(i)

#for i in x.values():
#	print(i)

#x= {"name":"kamal","age":23,"gender":"male"}

#for i,j in x.items():
#	print(i)

##------------------------------------------

#for name in range (2,16,2):  ## (start, end+1,step)
#	print(name)
#>>>>>
#2
#4
#6
#8
#10
#12
#14


##--------------------------------------------------------------------------------------------------------------------

## 16 VIDEO CONTENT
			## Python Tutorial - 16 | Break and Continue statement in Python |

## mema break and continue yoda ganne loop waladi we.

## 	FOR LOOP EKA SAMAGA BREAK AND CONTINUE YEDENA AKAARAYA

#for i in range (1,6):
#	if i==3:
#		continue
#	print(i)
#print("-----------------------------------")
##>>>(result = 1,2,4,5)
## mehidi i==3 di skip we
## ithuru tika print we

#for i in range (1,6):
#	if i == 3:
#		break
#	print(i)
##>>> (result = 1,2)
## mehidi i ==3 wana wita loop eka nawathi atha

##================================================


## WHILE LOOP EKA SAMAGA BREAK AND CONTINUE YEDENA AKARAYA

###
#i=0
#while (i<6):
#	if i==3:
#		continue
#	print(i)
#	i+=1

## mema loop eka waraiya meya nonawath wa run we.


#i=0
#while (i<5):
#	i+=1
#	if i==3:
#		continue
#	print(i)
##>>> (result: 1,2,4,5)
## i == 3 wita eya print nokara skip kara atha 

#print("-----------------------------")

#i=1
#while (i<5):
#	if i==3:
#		break
#	print(i)
#	i+=1
##>>> (result: 1,2)
## i== 3 wana wita loop eka nawathi

#print("-------------------------------------------")

#i=0
#while (i<5):
#	i+=1
#	if i ==3:
#		break
#	print(i)

## (result: 1,2)
## mehidi i==3 wana wita loop eka nawathi.
## salakiya yuthuii i=0 ha i=1 lesa awastha dekedi wenas lesa laba di atha.

###444444%%% enam saranshayak lesa gath wita 
	## break = adala condition eken pasu nawathi.
	## continue = adala condition eken pasu ema piyawara skip karaii.

##----------------------------------------------------------------------------------------------------------------

## 17 VIDEO CONTENT

		## Python Tutorial - 17 | Functions in Python |

## USER DEFIND FUNCTONS 

#def name(arg1,arg2):
#	print("The name is: ",arg1)
#	print("The age is: ", arg2)
############	print(id)

#name(str(input("Enter your name: ")),int(input("Enter your age: ")))
#name("Nimal Santha",16)


#def cal_some(length,width):
#	return length*width

#print("The squre is :",cal_some(int(input("Enter length: ")),int(input("Enter width: "))))

##------------------------------------------------

#def func(length,width):
#	return 2*(length+width)

#print("The perimeter is: ",func(12,34))


#def func(length,width):
#	area = length*width
#	perimeter = 2*(length +width)
#	print("The are is: ",area)
#	print("The perimeter is: ",perimeter)

#func(12,23)
#print("----------------------------------")
#func(123,34)

#for i in range (6 ):
#	print(i)

#print("@@@@@@@@@@@@@@@")

#func(21,23)

## melesa onama thanaka sita function ekata call kala hakiwe

##---------------------------------------------------------------------------------------------------------

		## 18 VIDEO CONTENT


##   		Python Tutorial - 18 | Default Arguments in Python |

## 
#def func_defarg(name="Kamal",age=22):
#	print("the name is: ",name)
#	print("the age is: ",age)

#func_defarg()
#>>> 
#the name is:  Kamal
#the age is:  22
### lesa labae enam default arguments yanu kalin function ekehi arguments sadana witama ewata dena parameters we
#	## enam aluthin function ekata parameters denne nathnam ema para meters walata adala out put labe
#	## ewita func_name() lesada laba diya hakiwe.

#print("-------------------------------------------")

#func_defarg("Eranda",45)
### parameters laba dun wita ewaata adala output labe

##----------------========

##$$$$$#####

## arguments sadaha * lakuna bawithaya.

#def func(name,age,*friends):
#	if age >= 20:
#		print("He is not a child")
#	print("The name is: ",name)
#	print("The age is: ",age)
#	print("Him/Her freiends are",friends)

#func("Kamal",23,"Nimal","Kavinda","Weranga")
##>>>>
#He is not a child
#The name is:  Kamal
#The age is:  23
#Him/Her freiends are ('Nimal', 'Kavinda', 'Weranga')
##------------

#def newfunc(subject,**marks):
#	print("The subject is:",subject)
#	print("The markd is:",marks)

#newfunc("Maths",science=33,physics =78)
#>>>
#The subject is: Maths
#The markd is: {'science': 33, 'physics': 78}

## ** tharu dekak laba dunwita dicionary ekak lesa add kala hakiwe.

##------------------------

#def marks(subject,marks,**friends):
#	print("subject =",subject)
#	print("marks = ",marks)
#	for keys,values in friends.items():
#		print(keys ,"=",values)

#marks("Maths",56,Kamal = 23,Nimal=45,Weranga =99)
#>>>>>>>
#subject = Maths
#marks =  56
#Kamal = 23
#Nimal = 45
#Weranga = 99

##_-----------___------------------____-----------------
##--------------------------------------------------------------------------------------------------------------

	# 19 VIDEO CONTENT

##Python Tutorial - 19 | Object Oriented Programming |
## OOP CONCEPT

## OBJECTS
			## phone ,cats ,cars
## ATTRIBUTES
			## name, colour, weight
## METHODS
			## massage, internet, email,

##-------------------------___________-------------_____---------------____--------------------------------------------

## 		20 VIDEO CONTENT

##Python Tutorial - 19 | Object Oriented Programming |

## >> how to create a class, how to add attributs and methods, how to access to the class and there attributs and methods

## attributs variables lesa laba dena athara methds functions widiyata laba deii
##1)
#class phone:
#	pass

## pasuwa bawithayata ganimata melesa yoda gatha hakiya.
## mema pass yana keyword eka function walatada laba diya hakiwe.

#class phone:
#	def say(self,name):
#		self.x= name
#		print("Hello",name)
#phone1 = phone()
#phone1.say("samsung")#

### say yanu method ekak wana athara phone1,phone2 yanu objects we


#phone2 = phone()
#phone2.say("Redmi 9C")

#phone1.x = "apple"
#print(phone1.x)



###----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class myclass:
	def lesson_1(self, name, age):
		self.name = "Kamal"
		self.age = 23

		print("Hello", name, "Your age is", age)

student1 = myclass()
student1.lesson_1("Kamal",22)

#student1.x = "Nishantha"
#student1.y = 40

#print(student1.name)
#print(student1.age)

print(student1.name)













