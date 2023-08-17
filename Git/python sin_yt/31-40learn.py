		## 31 VIDEO CONTENT 

##	Python Tutorial - 31 | Filter, Map, Reduce Functions in Python 


## use filter function 
## api udaharanayak lesa list ekaka athi numbers athurin iratte sankya 
	# wenkara ganimu

#number = [1,2,3,4,5,6,7,8,9]

#def even_num(x):
#	return x %2 == 0

#y = list(filter(even_num, number))
#print(y)
## >>> [2, 4, 6, 8]


## api meya sarala lesa laba ganimata lambda funtion eka yoda ganiu...

## mema kramaya mathaka thaba ganna .... padam karala thiya ganna...#$$$

#number = [1,2,3,4,5,6,7,8,9]

#y = list(filter(lambda x:x%2==0,number))
#print(y)
## >>> [2, 4, 6, 8]

##--------------------------

## map() function 

## mema function eka magin apata kisiyam list ekaka athi yam wenasak sidu kara 
	## ema list eka e widiyatama laba gatha hakiwe....


#number = [1,2,3,4,5,6,7,8,9]

#y = list(map(lambda x:x*2,number))
#print(y)
## >>> [2, 4, 6, 8, 10, 12, 14, 16, 18]


## melesa apata mema map() function eka use kara hakiwe...

##----------------------------------


## 	reduce () function 

## meya aththe ""functools"" yana library ekehi we....
	## emanisa mulin ema library eka import kara gatha yuthuwe...

## import functools 
	## meya melesa nowe from functools import reduce lesa laba diya yuthuya...

#from functools import reduce

#number = [1,2,3,4,5,6,7,8]

## dan api lambda function ekak yatathe x ha y variable dekak hadunwa ema variable dekata karana 
	## siyalu de me list eka purawatama siduwanu atha ....

###print(sum_number = reduce(lambda x,y:x+y, number))
## meya melesa print kala nohaka 

#sum_number = reduce(lambda x,y:x+y, number)
#print(sum_number)

## 36 lesa pilithura labe



##----------------------------------------------------------------------------------------


##		31 VIDEO CONTENT 

##	Python Tutorial-32 | Decorators in Python |


#def divide(a,b):
#	if b==0:
#		a,b = b,a
#	return a/b


#print(divide(34,0))
##>>> 0.0

## mehi sidu kara aththe 0 n bedimata nohaki nisa b=0 wita a ha b agayan maru wimaii...
## apita me function eka athule mukuth nokara mema karrya sidukala hakiwe...


#def new(func):
#	def inside(a,b):
#		if b==0:
#			a,b = b,a

#		return func(a,b)

#	return inside


#def divide(a,b):
#	return a/b

#divide = new(divide)

#print(divide(10,2))


## melesa menma meya pahatha paridida @ salakuna yodagena sidu kara hakiwe...

#@new 
#def divide(a,b):
#	return a/b

#print(divide(5,0))

## enam melesa decorators yoda ganu labe 
	## nawatha nawatha bala hodin practice kara mathaka thaba ganna....


					######################### 32



##					33 VIDEO CONTENT 


## ITHA WISHESHITHA WENAS VARIABLE EKAK GANA MEHIDI KATHA KARAII...

##Python Tutorial-33|if __name__=='__main__'|

## meya name varible eka lesa hadunwaii...


#print(__name__)
#>>> __main__
## memagin labenuye module ekaka namaki

#print("----------------------------")

#from video33 import add

#print(add(10,12))

#print("Hello")

#print(__name__)

### the out put
#----------------------------
#####################
#9
#video33 12234
#22
#Hello
#__main__



## dan api melesa mema import karana module ekehi athi anek ewa 
	# out put nokara anith adala ewa pamanak output wimata meya yoda ganna 
		# akaraya balamu...

		## e sadaha api import karana module eka thula me
				#if __name=='__main__':
				#	print(add(4,5))

				#	yanna laba diya yuthuwe...


## MEHIDI PRINT NOWANNE IF YATATHE ATHI EWA PAMANAKI
## ANEK SIYALLA SUPURUDU PARIDI PRINT WE, OUT PUT LABE....



						###################### 33


##----------------------------------------------------------------


		#	34 VIDEO CONTENT


## PYTHON TUTORIAL -34 |Polymorphism 1 (Method Overriding)|

## mehi sarala theruma nam wiwidaakara yannaii
	## enam ekama deyak wiwida swarupa walin hasirena eka we...

	## mema widiyata wiwida aakarawalin hasirena eka penwimata 
		#Method overriding 
		#Method Overloading 
		#Operator Overloading 
				##yana mema python concept walin penwimata haka...


## Method Overriding ----------------------

## mehidi method dekak hamu we...
	#mema dekehima nam ekama we
	#namuth karyan dekak sidu karaii....

#Different Method
#	Same Name 
#		Different Tasks

##$$ 


#class parent:
#	x = 40

#class child(parent):
#	pass	

#myobj = child()
#print(myobj.x)
#>>> 40

## overriding concept 

#class parent:
#	x = 40

#class child(parent):
#	x = 100

#myobj = child()
#print(myobj.x)
#>>> 100
## mehidi 100 lesa labi aththe parent class ekehi thibu x overriding wimenya...


## method overrinding wana akaraya balamu.


#class parent:
#	def meth1(self):
#		print("hello")

#class child(parent):
#	def meth1(self):
#		print("welcome")


#myob = child()
#myob.meth1()

## mehidi sidu wanne inherit karana lada class dekak bawitha kara ekama nam 
#ahti varibale ho methods walata call kirimedi sidu wana da dana ganimaii
#child class eke mukuth naththm parent class eke athi varibale ho mehtod ekata ganimaii
#adalawa out put eka labe 
#namuth child class eke varibale ho mehtod ekak athnam ita adalawa output eka labe 
#issara wanne object eka sadana lada class eka issara wima we... 
#meya e e tharam hithannawath deyak natha....


##--------------------------------------------------------------------------------------------------------


##		35 VIDEO CONTENT 

	## Polymorphism 2|Method Overloading|


#class myclass1:
#	def add (self,a,b):
#		sum = a+b
#		print(sum)

#myobject = myclass1()
#myobject.add(3,4)

#myobject.add(2,3,4)
## api create karana class ekaka athi method ekak bawitha kirimedi 
	## ehi athi arguments gananata wada apita labadimata nohaka

#class myclass2:
#	def add2 (a,b,c):
#		sum2 = a+b+c
#		print(sum2)

#myobject2 = myclass2()
#myclass2.add2(2,3,4)
#myobject2.add2(2,3)

## emenma ema arguments gananata wada aduwenda laba dimata nohaka.. 
### emanisa pahatha paridi api mehtods bawitha karamu...


##-----------$$$$



#class class3:
#	def add3(self,a=None,b=None,c=None):
#		if a!=None and b!=None and c!=None :
#			sum3 = a+b+c
#			print(sum3)
#
#		elif a!=None and b!=None:
#			sum3 = a+b
#			print(sum3)
#		else:
#			sum3 = a
#			print(sum3)


#myobject3 = class3()
#myobject3.add3(2,3,4)
#myobject3.add3(2,3)
#myobject3.add3(3)

#>>> 9
#>>> 5
#>>> 3	

## melesa bawitha kirimedi apata sankya 3ka 2 ka 1 ka out put aulaka nathuwama
# labe....

### meya METHOD OVERLOARIDNG LESA HADINWE


####-------------------------------35 NIMI------------------------------------------

##--------------------------------------------------------------------------


#		39 VIDEO CONTENT 

#		Python Tutorial-36|Types of Errors|

#		------------Types of Errors---------


#		1. Syntax Errors 
#		2. Runtime Errors
#		3. Logical Errors



#1-(A)Syntax Errors-------->>

## yamkisi bashawaka athi wyakarana dosha memagin penwaii
## enam programming language walatada adala wana syntax errors lesa mewa 
##hadinwe....

#	E.g.:print("Hello") yana meya qutation marks athule bageta dun 
      #wita syntax Errors penwaii print('hello)                                                     '


#(B) Name Errors-------------->>>
	## mema programming languages wala athi function name adiya 
		#niwaradi lesa nodima mita hethuwe....

	#E.g.: print yana building function eke athi akurak aduwen 
			#sadahan kala wita Name Error ekak generate ...

			
#2-Runtime Errors------------------>>

	#E.g.: a = 4
	#	  print(a)
	#	  >> 4 lesa labe 
	#	 Namuth meya user input karana agayaki...meyata akurak nikam laba 
	#	 dunnoth Name Runtime error ekaka generate we...
	#	 meya Name Error ekak lesa output we...
	#	 a = h
	#	 print (a)

#	E.g.: (2)
#		a = 4
#		b = 0
#		print (a/b)
#		melesa laba dun wita Zero Divishion Error lesa Runtime error ekak 
#		generate we

## enam mema Runtime Error wala aththe code eke prashnayak nowe...user input kala
#agaye we


#3-Logical Errors------------>>

## mema awasthawedi apa wisin godanagana lada logic wala problems memagin 
	## hadinwe...

##----------------------------------36 nimi--------------------------------------------##

				#37 VIDEO CONTENT  PYTHON 
		#Python Tutorial-37 |Exception Handling|


## MEMAGIN SIDU KARANUYE CODE EKE NOWANA WARADI ENAM USER KENK GEN SIDUWANA 
	## WARADI PALANAYA KIRIMA MEMAGIN SIDUWE...

#eg: a = int(input("Enter first number: "))
#	 b = int(input("Enter second number: "))
#	 print(a/b)
#	>>> Enter first number: 4
#		Enter second number: 0
		## memagin Zero divishion error ekak generate we
	## Enam mehidi user waraddak kara atha enam bedima sadaha 
		## 0 input kirimaii

	## dan mema error coder wisin "Python wisin di athi blocks bawitha kara"
	#fix karana akaraya balamu....


#try:
#	a = int(input("Enter first number: "))
#	b = int(input("Enter second number: "))
#	print(a/b)
#except:
#	print("Something went wrong!")

## thawaduratath melesa wana waradda output kara ganimata melesa bawitha karamu
#try:
#	a = int(input("Enter first number: "))
#	b = int(input("Enter second number: "))
#	print(a/b)
#except Exception as e:
#	print("Something went wrong!",e)

## mehidi apata e wenuwata kamathi namak labadiya haka
## emenma mehidi e magin mehi wana waradda output karanu labe...

#------------------- ##

## thawada mehidi apata finally yana block eka bawitha kara mema code 
	## eken waraddak genarate uwada nathiuwada poduwe kara ganimata awashya 
		## dewal kara ganimata meya bawitha kala hakiwe....

#try:
#	a = int(input("Enter first number: "))
#	b = int(input("Enter second number: "))
#	print(a/b)
#except Exception as e:
#	print("Something went wrong!",e)
#finally:
#	print("bye")



## APITA ERROR EKA FOCUS KARALA API HITHANAWANAM MEKA THAMAII METHANA WENNA 
#PULUWAN WARADDA KIYALA APIATA MELESA BAWITHA KALA HAKIWE...



#try:
#	a = int(input("Enter first number: "))
#	b = int(input("Enter second number: "))
#	print(a/b)
#except ZeroDivisionError as e:
#	print("Canot divide by zero! ",e)

#try:
#	a = int(input("Enter first number: "))
#	b = int(input("Enter second number: "))
#	print(a/b)
#except ZeroDivisionError as e:
#	print("Canot divide by zero! ",e)
#except Exception as e:
#	print("something went wrong! ",e)
##finally:
#	print("bye")

## API MEHIDI BINDUWA NATHUA akurak input kalahoth mehidi apata pennanuye
	#>>> something went wrong! invalid literal for int()
	#	bye 
	#	lesa we...
## meyada awashyanam kalin wage thawa block ekak bawitha kara melesa hadunwamu..



#try:
#	a = int(input("Enter first number: "))
#	b = int(input("Enter second number: "))
#	print(a/b)
#except ZeroDivisionError as e:
#	print("Canot divide by zero! ",e)
#except ValueError as e:
#	print("please use integers! ",e)
#except Exception as e:
#	print("something went wrong! ",e)
##finally:
#	print("bye")



#>>> please use integers! invalid literal for int() with bas...
 	#bye
 	#lesa out put eka labe....

 	## ENAM MEMA EXEPTION HANDLING MAGIN SIDUKARANNE MOKAK HARI ERROR EKAK WENNA
 	#PULUWAN NAM EKA HADUNAGENA ITA ADALA WISADUMAK LABADIMA WE 


 ##---------------------------------37 NIMI-----------------------------
 


 	##	Python Tutorial-38| Arrays in Python|


 ## List wagema data structure ekak we

 ## What is the difference of Lisst and Array?

 	## List ekaka wiwida data types wala data store kara athath
 	#	Arrays wala elesa nowe, eka wargaye data type wala data 
 	#	store kara ganimata mema arrays yoda ganu labe 

## string values athinam string array lesa float value athnam float array lesa
	##aadi lesa mema arrays hadinwiya hakiwe..

	## mehidi wivida data type wala data store kala haki athara
		#ita adala Type Code ekakda atha... 


#		Data Type 			Type code


#	1) Character	-	"c"
#	2) Unicode 		-	"u"
#	3) Signed Short 	-	"h"
#	4) Unsigned Short -	"H"
#	5) Signed int	- 	"i"
#	6) Unsigned int	- 	"I"
#	8) Unsigned Long 	- 	"L"
#	9) Float 		- 	"f"
#	10) Double		-	"d"


##2) Unicode = magin string values 
##5) signed int = dana saha rina onama parasayaka athi integer values 
##6) Unsigned int = dana sankaya pamanak store kara gatha hakiwe
## 



## salakiya yuthuii mema arrays bawitha kirimedi mema package eka import 
	## kala yuthuwe...

## inpasu ehi athi array() function ekata call kala yuthu we..

#import array
#
#x = array.array('i',[1,-2,3,4,5])
#print(x)

## >>> array('i', [1, -2, 3, 4, 5])
##------------
#import array
#x = array.array('u',)
#print(x)

## I don't know what are the unocode charactors so I don't know how to use the 
## 'u'... please search and find how to use array with unicode




##---------------------

#import array
#my_first_array = array.array('i',[1,-2,4,-6])
#print(my_first_array)

## >>> array('i', [1, -2, 4, -6])
## Arrays waladi i magin dana saha rina sankya dewargayama store kara gatha hakiwe

#import array
#my_first_array = array.array('I',[1,2,4,6])
#print(my_first_array)

#>>> array('I', [1, 2, 4, 6])
## dana sankya store kara ganimata I bawitha kala hakiwe

##------------ 
##Emenma mehidida list wala bawitha karana appned, indexing and negative 
	#indexing use kala hakiwe


#import array
#y = array.array('i',[1,2,3,4,5,10])

#print(y)
#y[0] = 11
#print(y)

#print(y[4])
# >>>>
	#array('i', [1, 2, 3, 4, 5, 10])
	#array('i', [11, 2, 3, 4, 5, 10])

##api mehidi kara aththe array kiyana package eke athi array function ekata 
	#call kirimaii 
	#array wala athi siyaluma function import kara ganimatada puluwani 
	#ewita array yana function ekata call kirimada awashaya nowe



#from array import  *
#x = array('i',[2,4,6,756])
#print(x)

## >>>  array('i', [2, 4, 6, 756])


#from array import *
#v = array('i',[3,4,5,67,7])
#print(v)


##------------

#from array import *
#a = array('i',[2,4,6,7,-7,6])
#print(a)
## ------------ how to add element/ elements to array
#a.append(100)
#print(a)

#a.extend([13,345,57,678])

## element ekak add kara ganimata append da element kihipayak add kara ganimata 
# extend use karanu labe.. 

#>>>
#	array('i', [2, 4, 6, 7, -7, 6])
#	array('i', [2, 4, 6, 7, -7, 6, 100])

##---------------


## mema append saha extend yana function magin element add kara ganimata 
	## haki wuye array ekehi agata we

## apita kamathi place ekakata element add kara ganimata insert function eka 
	## use kala haki we


# a.insert(3,100)

	## mehidi index 3 ta adala thana enam 4 wana element eka hatiyata 
		## 100 add wi atha .....


##--------- how to remove an element of remove elements in array


##we can use the pop() function for remove last element of array...

## a.pop()

## we can use the index number with pop function for remove an element in array

## a.pop(3)
## 4 wani element eka remove we

## how to use the remove function for remove an element 


#from array import *
#a = array('i',[2,34,4,-5])
#a.remove(34)

#print(a)
#>>[2,4,-5]

##---------------------------------

## from array import *
#x = array('i', [2, 14, 16])
#y = array('i', [-7, 6, 100])

#z = x + y 

#print(z)
#>> array('i', [2, 14, 16, -7, 6, 100])
 ## samana jathiye arrays ekathu kala haki we

 #i + i == correct 
 #I +i  == false


##----------------
## how to use for loop with array

#from array import *
#x = array('i', [2, 14, 16])

#for i in range(len(x)):
#	print(x(i))

#>>>
#2
#14
#16
#------
#for i in x:
#	print(i)

#>>>
#2
#14
#16

## ------------------------- 38 VIDEO CONTENT IS OVER ---------------





























