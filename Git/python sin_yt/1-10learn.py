##			PYTHON SINHALA YOUTUBE VIDEO SET 

##1 VIDEO CONTENT
## how to install python and work python with cmd
##how to use and IDE(Integrated Development Environment) use
## Pycharm,PyDev,Atom,SPYDER
##-------------------------------------------------------------------------------------

## 2 VIDEO CONTENT
## +,-,*,/, // ,**,%,#

##-------------------------------------------------------------------------------------
## 3 VIDEO CONTENT
##VARIABLES AND DATA TYPES

##DATA TYPES
##integer,float,string,complex,boolean,list,set,tuple,dictionary

##-------------------------------------------------------------------------------------
## 4 VIDEO CONTENT
## input () and print () functions
#a="name"
#b=23
#print(a+b)
## canot add different data types values.
#print(a+str(b))
##>>> name23
#a=input("Enter value: ")

##-------------------------------------------------------------------------------------
## 5 VIDEO CONTENT
## FUNCTIONS
##1- Built-in-Functions
##2- User defined Functions
##$ mema Built in functions bala ganimata 
## code eka == dir(__builtins__)

## watina functions
## help() == meya apita hadunwa di athi function pilibadawa dana ganimata 
			#> upakri we
## use:
	## ex:
		## pow() == b in f eka gana balamu
		## help(pow)
## pow() magin balya laba ganimata puluwani.

##-------------------------------------------------------------------------------------

##6) VIDEO CONTENT

## PYTHON STRINGS

##STRING WALADI \ FORWARD SLASH BAWITHAYA .

#print('nimal's')  >> melesa udu coma yedimata nohaki nam ee sadaha forword slash 
#yoda ganimu

#print('Eranda\'s')
#\  lakuna magin ' balaya nathiwe.


##element ekaka index numbers :
#x= "Eranda Prasad"
#print(x[3])
##>>> n


##parasayak print kirima :
#print(x[2:9])
##>>> anda Pr

##element wenas kirima sadaha replace bavithaya
##How to use: "replace"

#z= x.replace( 'a', 'i')
#print(z)
##>>> Erindi Prisid

##____ SPLIT AND JOIN BAWITHAYA _____

#x = "Eranda Prasad"
#z= x.split(' ')
#print(z)
##>>> ['Eranda', 'Prasad']

#y=' and '.join(z)
#print(y)
##>>> Eranda and Prasad

##-------------------------------------------------------------------------------------

###  7 VIDEO CONTENT IS COMPARISON OPERATORS

#1)  == equal 
#2)  != not equal
#3)  > greter than 
#4)  < less than 
#5)  >= greter than or equal
#6)  <= less than or equal

##-------------------------------------------------------------------------------------

### 8 VIDEO CONTENT 

## 		 IF ELSE STATMENT

## if yanu sathya awasthawedi kriyathmaka wana statment ekaki.

#if true:
#	print(12445)
##>>> 12445

## mehidi asathaya awasthawedi kriyathamaka wiamata else bawitha karaii.

#name= 12345
#if name = 123 :
#	print("True")
#else:
#	print(888)
##>>> 888

##--------------------------------------------------------------------------------------------------------------------------------------------

##	9 VIDEO CONTENT 

## PYTHON COLLECTIONS 
###	LIST [ ]

#DATA TYPES KIHIPAYAKA ELEMENTS ATHULATH KARAGANIMATA MEMA 
#- COLLECTIONS BAWITHA KARAII.

##mema list walata index numbers atha.

#x = ["name", "marks", "Kamal", 78,234,True]
#print(x[5])
##>>> True
#print(x[0])
##>>> name

### elements wenas kirimata 
#x= [1,2,3,4,45]
#x[1] = "age"
#print(x)
##>>> [1, 'age', 3, 4, 45]

##list ekaka length eka bala ganima, elements ganana bala ganima.

##len ()
## (meya in built function ekaki.)
#x= ("Oshadi", "maranaya",12,45,67,78.89)
#print(len(x))
##>>> 6


##list ekakata elements add kirima.
##insert() bawithaya;

##how to use insert()
##x.insert(index num,element)

#x = [1,'name',2,"age",3,"Kalubowitiyana",4,5]
#x.insert(1,"Lakshitha")
#print(x)
##>>> [1, 'Lakshitha', 'name', 2, 'age', 3, 'Kalubowitiyana', 4, 5]

###list eka agata element add kirimata append bawitha karaii.
###how to use append()

#x = [12,2,3,4,5,6]
#x.append("apple")
#print(x)
##>>> [12, 2, 3, 4, 5, 6, 'apple']

### how to remove elements from the list

#x = [1,2,4,,5]
#x.remove(4)
#print(x)
##>>> [1,2,5]

### aga element eka iwatha kiimata pop bawitha kara hakiya.
#x = [1,2,3,4,"element"]
#x.pop()

#print(x)
##>>> [1, 2, 3, 4]

##  LIST EKAK DELETE KIRIMA
##	del bawithaya/.

#x = [1,2,3,4]
#del x
#print(x)
##>>> NameError: name 'x' is not defined

###	ELEMENTS CLEAR KIRIMA

#	# clear bawithya/.

#x = [1,4,5,6,7,88,78]
#x.clear()
#print(x)
##>>> []
### elements siyalla clear wi his list ekak ithuru wima mehidi sidu we.


##----------------------
##		AROHANA PILIWELATA HA AWAROHANA PILIWELATA SADA GANIMA\.

##x = [34,56,78,2,4,678,4]
##x.sort()
##print(x)
##>>> [2, 4, 4, 34, 56, 78, 678]
### meya itha hodin mathaka thaba ganna.
###$$$$$$$ salakiya yuthuii sort magin labenne AROHANA patipatiya we

#x = [2344,45,679,2,34767,45,567,54,2,4]

#x.sort(reverse=True)
#print(x)
##>>> [34767, 2344, 679, 567, 54, 45, 45, 4, 2, 2]

###  $$$$$$ salakiya yuthuii AWAROHANA patipatiyata labaganimata
###>>>   sort(reverse = True) lesa laba diya yuthuwe.


####============----------------

##list wala thawath akara

#a,b,c,d = [1,2,3,4]
#print(c)
## >>> 3

#a,b,*c = ["name","age",3,4,565,67]
#print(c)
##>>> [3, 4, 565, 67]

##-------------------------------------------------------------------------------------------------------------------------------------------------

##	10 VIDEO CONTENT :- tuple

## tuple wala elements wenas kala nohakiwe.
## ex: 
#x= (2,3,4,5,6)
#x[2] = "name"
#print(x)
##>>> TypeError: 'tuple' object does not support item assignment

## list wala menma index nubers atha.

#x= (23,5,77,8,99,34)
#print(x[3])
##>>> 8 

### list wala menma length eka bala ganimata puluwani.

#x = (1,22,3,4,5,576,878,6)
#print(len(x))
##>>> 8

## list menma delete kirimata puluwani namuth clear kala nohakiya.

#x = (1,22,34,455)
#del x
#x.clear()
#print(x)

##>>> NameError: name 'x' is not defined
## >>> AttributeError: 'tuple' object has no attribute 'clear'

##		 SALAKIYA YUTHUII LIST WALATA WADA TUPLE SPEED WE

##  timeit bawitha kara speed eka bala ganima

#import timeit

#list_time = timeit.timeit(stmt = "[1,2,3,4]")
#tuple_time = timeit.timeit(stmt = "(1,2,3,4)")

#print(list_time * 100)
#print(tuple_time * 100)
##>>>15.937806999863824
##>>>3.3549484000104712
##enam memagin dakwenne tuple speed bawaii

##-----------------------------------------------------------------------------------------------------------------------------------------




















