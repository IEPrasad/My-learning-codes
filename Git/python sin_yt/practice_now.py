## Filter, Map, Reduce Functions sinhala #31 tutorial 

## how to use filter function 
## mema filter function eka magin list ekaka kisiyam eliments kihipayak filter kara gatha hakiwe...


## list ekakin even numbers filter kara ganimu

#numbers = [1,2,3,4,5,6,7,8,9]

#def even_num(x):
#	return x%2 == 0


## mema filter function ekata argument dekak laba diya yuthuwe...
		# palamuwa adala function name eka laba di dewanuwa list name eka laba denna..

#y = list(filter(even_num,numbers))
#print(y)

##>>> [2, 4, 6, 8]

## meya lambda function eka yoda gana lesiyen yoda ganimu...

#---------------------------------------

#area = lambda x : x*x

#numbers = [1,2,3,4,5,6,7,8,9]

#even_numbers = lambda x : x%2==0

#y = list(filter(even_numbers,numbers))
#print(y)

##>>> [2, 4, 6, 8]


#numbers = [1,2,3,4,5,6,7,8,9]
#y = list(filter(lambda x : x%2==0, numbers))
#print(y)
##>>> [2, 4, 6, 8]

##---------------------------------Map function___--------------------


## mema function eka magin list ekata kisiyam wensak sidu kara list eka nawatha laba gatha hakiwe...

#p = list(map(lambda x : x/2 + 4, numbers))
#print(p)

##>>> [4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5]



###----------------------------------Resuce function____-----------------------

## meya aththe functools yana library ekehi we...
## ema library eka import kara gatha yuthuwe....
## inpasu x ha y lesa varible dekak lambda function ekak yatathe sada ganimu
	## inpasu e variable dekata karana sama deyakma list eka purama sidu we...


#from functools import reduce

#number = [1,2,3,4,5,6,7,8]

#sum_of_num = reduce(lambda x,y: (x+y), number)
#print(sum_of_num)

##>>> 36
##-----------------------------------------------------------------------------




























