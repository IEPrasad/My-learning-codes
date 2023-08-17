## 21 VIDEO CONTENT

## Python Tutorial - 21 | __init__ method in Python | Constructor 

#class student:
#	def __init__(self,name,age):
#		self.name = name
#		self.age = age
#		

#st1 = student("Kamal",13)
#st2 = student("Nimal",15)
#print(st1.name,end=" "),
#print("age is",st1.age)
#print(st2.name,end = " " )
#print("age is",st2.age)

###meka yt eke thibuna code eka we
### ihatha dakwenne __init__ method eka yoda gena ihatha sadahan de __init__ nathuwa balamu.



#class student:
#	def say(self,name,age):
#		print(name,end=" ")
#		print(" age is",age)

#st1 = student()
#st2 = student()
#st1.say("Kamal",13)
#st2.say("Nimal",15)

###$$$$$$$$$ please more practice __init__ method


###-----------------------------------------------------------------------------------------------------------------------------------------


#class practice:
#	def __init__(self,name,age):
#		print(name,end=" ")
#		print("age is",age)

#st1 = practice("Kamal",13)
#st2 = practice("Nimal",15)
#st1 = practice("Eranda",56)
#a = practice("Kasun Mama",56)

## so that is the most easy way to do it 
## samanya kramayedi object ekak create kara in pasu ema object eka haraha call kala yuthuwe
	## namuth mehidi object eka create karana witama adala parameters laba dima sidu kala hakiwe.

########################################################################################################


### 		22 VIDEO CONTENT

##Python Tutorial - 22 | Encapsulation |

##"private variables ha method sadima mehidi sidu kere"
##variable saha method walata access kirima sima kirima memagin sidu karaii

##"Let\'s go to the lesson"

#class myclass:
#	__x= "Nimala"
#	def mydef(self,name):

#		print("Hello",name)
#		self.__mymeth()
#		print(self.__x)
#	def __mymeth(self):
#		print("Nika")
	
#myobject =myclass()
#myobject.mydef("kamal")
#myobject.__mymeth()
#print(myobject.__x)

###-------------------------------------------------------------------------------------------------------------------

##		23 VIDEO CONTENT

## Python Tutorial - 23 | Python Inheritance | 

#class phone1:
#	x= "Rs.45000.00/="
#	def feature1(self):
#		print("SMS")

#class phone2(phone1):
#	def feature2(self):
#		print("Camara")

#class phone3(phone2):
#	def feature3(self):
#		print("Internet")

#myobject =phone2()
#myobject.feature1()


##saralawa gath kala memagin siduwenne eka class ekaka athi variables saha method walata thawath class
	## ekak sadaha create karana object ekakin access kirimata hakiweemaii
## nathahoth class wala athi variables ha methods poduwe bawitha kirimata hakiweemaii.
 
##$$$$$$ mehidi method walata self laba deema aniwarya we, puruddak lesa self laba denna.

###----------------------------------------------------------------------------------------------------------------------------------------------


## 		24 VIDEO CONTENT 

##Python Tutorial - 24 | Inheritance Exercise

### mehidi aluth function ekak bawitha karana akaraya igena ganimu
		## $$$ super()

#class parent:
#	def func1(self):
#		print("Hello")

# parent class eka child class ekata inherit karamu
#class child(parent):
#	def func2(self):
#		print("welcome")

## dan object ekak child class ekata adalawa create kara eamagin method dekatama call karamu.

#myobject = child()
#myobject.func1()
#myobject.func2()
## >>> Hello saha welcome yana deka out put lesa labe

## mehidi mema hello saha welcome yana dakama child class ekehi method ekata call kara laba 
	## ganimata super() class eka bawitha kala hakiwe

#class myclass:
#	def myfunc1(self):
#		print("Isuru")
#	my1 = "ayyo sami"
#class mychild(myclass):
#	def myfunc2(self):
#		super().myfunc1()
#		print(super().my1)
#		print("Good job")


#myobj = mychild()
#myobj.myfunc2()


## memagin ekawara ek class ekaka sita anith class eke athi method saha attributes walata enam 
	## function eke athi variables saha methods child class eke sita kriyathmaka kala hakiwe.


##---------

##%%%%% dan api method ovewriting gana blamu

#class myclass:
#	def func1(self):
#		print("welcome")
#	x = "Priyantha"
#class child(myclass):
#	def func2(self):
#		print("hello")
## dan api func1 lesa enam parent class ekehi athi method name ekama yoda gena thawa method ekak create karamu
		## meyata overiting kiyanu labe
#	def func1(self):
#		print("overwriting is successful")
#	x = "Same atrributes"
#myobj = child()
#myobj.func1()
#print(myobj.x)
	##>>> overwriting is successful 
	##>>> Same attributes
## ewita labenne child class ekehi athi method ekata adala out put eka we
## parent class ekehi athi methods name pamanak nawa attribute name da overwriting kala hakiwe.


##-------self practice overwriting

#class myclass:
#	def myfunc(self):
#		print("practice same ")
#	x = 100
#class nikam:
#	def myfunc(self):
#		print("welcome")
#	x = 100000
#myobject = nikam()
#myobject.myfunc()
#print(myobject.x)

## enam overwiting yanu amuthu deyak nowe onama enam inherit nokarana lada awasthawalada 
		# overwriting kala hakiwe


#class fruits:
#	number_of_items = None
#	unit_price = None
#	def set_value(self,x,y):
#		self.number_of_items = x
#		self.unit_price = y

#class Apple(fruits):
#	def price(self):
#		print("For apple Rs:",self.number_of_items * self.unit_price)

#class Orange(fruits):
#	def price(self):
#		print("For orange Rs:",self.number_of_items * self.unit_price)

#class Grapes(fruits):
#	def price(self):
#		print("For grapes Rs:",self.number_of_items * self.unit_price)

#myobject1 = Apple()
#myob2 = Orange()
#myob3 = Grapes()

#myobject1.set_value(4,200)
#myob2.set_value(5,40)
#myob3.set_value(30,10)

#myobject1.price()
#myob2.price()
#myob3.price()


#### melesa mema class and inheritance bawitha kala haki we


########------------------------------------------------------------------------------------------------------------------



##			VIDEO 25 CONTENT

##Python Tutorial - 25 | Create Modules 


## mehidi palamuwa python files dekak awashya we
## ek python file ekaka athi methods anek file ekesita bawitha kirima sidukaraii..

## api me sadaha mema file eka harunukota thawath file ekak create kara ganimu.

#import 25lesson.py

#mport lesson
#i=45
#j=34
#print(lesson.add(i,j))
#print(lesson.sub(34,56))
#print(lesson.multi(100,45))
#print(lesson.divide(i,j))
##>>>79
##>>>-22
##>>>4500
##>>>1.3235294117647058



##$$ slakiya yuthuii mehidi sadana lada file eka enam imoort karana file eka ilakkam walin aramba nowana file ekak wiya yuthuya.

## emenma file xtention eka sadahan karanu nolabe
#	lesson.py ::>>>>>" import lesson " lesa pamanak bawitha kala yuthuya.

#$$$$$$$$$$$$$$$$
## dan api mema file eka directory ekak athule athi wita import karana akaraya balamu

#from Dir import less
#import Dir.less as less
#print(less.add(23,34))
##>>> 57
## ihatha import kara athi akara dekatama meya  use kala hakiwe.
	## mathaka thaba ganna atham wita palamu kramayedi print(Dir.less.add(45,56)) lesa da denna siduwana bawa
			## video eke dakkemi
		## IMPORT karana file eke mulata ilakkamk tibboth error massage penwaii.

#$$$$$$$$$$$$$$$$$$$$$$

###---------------------------------------------------------------------------------------------------------


## 		26 VIDEO CONTENT

##Python Tutorial - 26 | Date and Time 

#import datetime
#b_day = datetime.date(2003,5,19)
#print(b_day)

## >>> 2023-04-29
## salakiya yuthuii mehidi dinayan laba dena wita mulata binduwa 2023,04,07 lesa dima waradiya 
## eya bindu nathuwa laba denna,2023,4,7


#today = datetime.date.today()
#print(today)
##>>> 2023-04-29
## mehidi ada dinaya labe


##______##$$$$$$$$$$$$$$$$$$$
## date saha time format eka customize karana akaraya

#import datetime
#b_day = datetime.date(2003,5,19)

#print(b_day.strftime("%A:%d:%b:%Y"))
##>>> Monday:19:May:2003
###-----------

#import datetime
#today = datetime.date.today()
##====
#print(today)
##>>> 2023-04-29
#print(today.weekday())
##>>> 5
## enam mema weekday akarayata 5 lesa labi aththe ada senasurada dawasak nisa weni,
	## mehidi 0 saduda wana athara 1 agaharuwada, ..., 6 irida lesa adala anka labe.
## meya isoweekday lesa laba dun wita 1 sadudagen patan gena 7 irida lesa ganan gane.
#print(today.isoweekday())
## >>> 6 
## enam mema class ekedi 6 yanu senasurada we.

##-----------------------
## 
## dan api welawan pilibadawa balamu...


#import datetime


#t = datetime.time(9,30,45,10000)

### paya 9 miniththu 30 thathpara 45 micro second 10000
#print(t)
##>>> 09:30:45.010000
#print(t.hour)
##>>> 9
#print(t.minute)
##>>> 30
#print(t.second)
##>>> 45
#print(t.microsecond)
##>>> 10000
### lesa pilithuru laba ganimata hakiwe.
##---------------

#t = datetime.datetime.today()

#print(t) 
##>>> 2023-04-29 02:35:16.195529
### memagin apata dinaya saha welawa yana dekama labe.


#t = datetime.datetime.today()
#print(t)
#t_delta = datetime.timedelta(days = 20)
#print(t_delta)
#print(t-t_delta)

##>>> 2023-04-29 03:14:38.383015
##>>> 20 days, 0:00:00
##>>> 2023-04-09 03:14:38.383015
### enam mehidi dawas 20 kata kalin dawasa labi atha.
### meya ekathu kirimak lesa laba dun wita dawas 20 kata pasu dinaya labe.
### emenma days=20 wenuwata hourse lesada laba diya hakiwe.

##------------
## birth day eka laba di wayasa laba ganimu.


###b=int(input("Enter birth month: "))
###c=int(input("Enter birth date: "))
###b_day = datetime.date(2001,10,27)
#print(b_day)

#today = datetime.date.today()
#print(today)

#age = today-b_day
#print(age)
##>>> 7854 days, 0:00:00
## api meya 364n beda aurudu gana ganimu
#print(age/364)
##>>> 21 days, 13:50:46.153846

### ------------------------------------------------------------------------------------

## 			27 VIDEO CONTENT 

## Python Tutorial - 27 | Turtle Module

## THAT IS VERY IMPORTANT AND VERY INTERESTING PART OF PYTHON 

## Megidi apata wiwida hadathala adiya nirmanaya kirimata ha wiwida rupa adimata 
	## turtle module eka bawitha kala hakiwe...


##palamuwa turtle yana module eka import kara gatha yuthuya...
	## inpasu object ekak create kara gatha yuthuwe...
		## ehidi turtle module eke athi Turtle nam class ekata call kala yuthuwe...

#import turtle

#x = turtle.Turtle()
#x.forward(600)

## mema commands linux terminal eke type karanna...
#>>> import turtle
#>>> x = turtle.Turtle()
#>>> x.forward(200)
#>>> x.circle(40)
#>>> x.shape(turtle)
#>>> 
#>>> 
#>>> x.shape("turtle")
#>>> x.color("red")
#>>> x.pencolor("green")
#>>> x.right(90)
#>>> x.forward(100)
#>>> x.pencolor("yellow")

## mema akarayata terminal eka bawitha kara wiwida hadathala nirmanaya kala hakiwe..

####---------------------------------------------------------------------------------------


## 		28 VIDEO CONTENT 

## Python Tutorial - 28 | Factorial ( n! ) 

## KRAMAROPITHA sambandawa mehidi igenaganu labe....

## 4! = 4*3*2*1
## meya apa for loop ekak adarayen laba ganimu

##x=4
## x yanna user input ekak lesa laba ganimu...
#x = int(input("Enter number: "))
#result = 1
## for i in range(1,5): ewita meya pahatha paridi wenas karamu...

#for i in range(1,x+1):
#	result = result*i

#print(result)

### memagin apit adala agayak labadi Factorial out put eka laba ganimata hakiwe.


###-----------------------------------------------------------------------------------

##		29 VIDEO CONTENT 

## Python Tutorial - 29 | Factorial Using Recursion

## mehidi apa Recurtion function ekak yodagena Factorial value ekak calculate karana akaraya....
	## mehidi apa for loop ekak wenuwata Recurtion funciton ekak yoda ganu labe...


#def fact(n):
#	if n==0:
#		return 1
#	else:
#		return n*fact(n-1)

#print(fact(4))
#>>> 24

## $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

## hodin function eka kriyathmaka wana hati balanna...
	## igena ganimata bohode atha....
	## memagin siduwi aththe enam mema Recurtion function eken sidu wanne,
		## ekama function ekata nawatha nawatha call kirima we....


###---------------------------------------------------------------------------

## 30 VIDEO CONTENT 

## Python Tutorial - 30 | Python Lambda Function (Anonymous Function )

## learn date 2023-05-01
## learn time 23:07:00

##----------------

## Memagin lambda function eka gana katha karamu..
	## Lambda yanu keyword ekaki function ekak nowe..


## samachathurasrayake wargapalaya ganima

#def area(x):
#	return x*x

#print(area(5))
##>>> 25

## apita memwani calculation kirimata lambda function eka yoda gatha hakiya...
## salakiya yuthui emagin thani prakashanayaka function ekak lesa baeitha we..
		# enam loku calculation piyawara gana wadi calculations sidu kala nohaka...



#area = lambda x : x*x

#print(area(5))
#>>> 25

## enam mema akarayata lambda function eka bawitha karanu labe...

## meya riju konasrayakata yoda ganimu..

#area = lambda x,y : x*y

#print(area(4,6))
#>>> 24

## api dan thawath udaharanayak balamu..

#def apple(unit_price):
#		return (lambda number_of_apples : number_of_apples*unit_price)

#x = apple(40)
#print(x(10))

##>>> 400

## mema yedawuma gana nawatha nawatha adyanaya karanna, mata me x variable eka kathawa 
	# therune nah....



##$$$$$$$$$$$$$$$$$ 21-30 video set is over.....$$$$$$$$$$$$$$$


































