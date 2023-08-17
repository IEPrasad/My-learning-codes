## apped bawithaya

#x=[1,2,3,]
#print(x)
#x.append("the name is ")
#print(x)
#x.append("Kamal Perera")
#print(x)

### the output is 
#>>>[1, 2, 3]
#>>>[1, 2, 3, 'the name is ']
#>>>[1, 2, 3, 'the name is ', 'Kamal Perera']

###____________________________

#x=["name"]
#print(x)
#x.append("name is","Kamal")
#print(x)
#>>> TypeError

## enam append() magin elements kishipayak add kala nohakiwe
### e sadaha extend() use kala uthuya.

###__________________________________________

## extend() bawithaya.

#x=["name",234,"kamal"]
#print(x)

#x.extend("Name")
#print(x)
##the out put is 
##>>>['name', 234, 'kamal']
##	['name', 234, 'kamal', 'N', 'a', 'm', 'e']

##___________________________________________

### sdlakiya yuthuii extend magin elements kihipayak athulath kirimedi ha >>
## >> string values athulath karana wita list ekak akarayata laba diya yuthuya.

#x=["name","Kamal","Uditha",23]
#x.extend(["add an elements ",234,34])
#print(x)
## the out put is 
#>>>['name', 'Kamal', 'Uditha', 23, 'add an elements ', 234, 34


### ___________________________________

##  insert() bawithaya

#x=["Nimal",23,"kamal"]
#x.insert(2,22)
#print(x)
##>>> [23, 'name', 22, 'kamal']

## How to use
## list_name.insert(index_number,element)

###__________________________---

## remove() bawithaya 

#x=["Nishantha","Kalubovitiyana",35]
#print(x)
#x.remove(35)
#print(x)
### the out put is 
##>>> ['Nishantha', 'Kalubovitiyana', 35]
##>>> ['Nishantha', 'Kalubovitiyana']
### How to use remove()

##list_name.remove(the_element)
### list ekehi athi element ekak remove kirimata use karaii.

###___________________----------------

## pop() bawithaya 

#x=["name","Nishantha",34]
#x.pop(1)
#print(x)
## the out put is 
##>>> ['name', 34]

##How to use pop()
##list_name.pop(index_number_of_the_element)

### kisiyam index nuber ekakata adala element ekak remove kirimata pop use karaii.

###_______________________________________________


## clear() bawithaya 

#x=["Exception ","expect"]
#x.clear()
#print(x)
## the out put is 
##>>> []

## list eka thula athi siyalu elements clear wi his list ekak labe

## How to use clear()
##list_name.clear()

###_______________-------------------______________-------______

## index() bawithaya 

#x=["name","variables",23,"generation"]
#x.index(23)
#print(x)
##the out put is
##>>>['name', 'variables', 23, 'generation']

### adala element eka list eka thula athnam pamanak list ekama print we
## how to use index()
## list_name.index(an element on the list)

###___________________________________________________

## count() bawithaya 

#x=["Documents",23,23,23,"system",23]
#print(x.count(23))
## the out put is 
##>>> 4
## laba dena lada element eka list eka thula yedi athi wara ganana penwaii.

## how to use count()
##  list_name.count(an element from the list)

##______________--------------___________--------______-----------


## sort() bawithaya 

##prime_numbers = [11, 3, 7, 5, 2]
##prime_numbers.sort()
##print(prime_numbers)

#x=[23,334,4,"name","Government",3]
#x.sort()
#print(x)
##>>>TypeError: '<' not supported between instances of 'str' and 'int'

## sort() magin list ekak thula athi sankyathmaka agayan aarohana piliwelata >>
##>>sakas karanu labe..mehidi yoda gatha hakke int,float values pamani.

#x=[23.44,56,65.46,22]
#x.sort()
#print(x)

## how to use sort()
## list_name.sort()
## print(list_name)

##___________--------------_____________------------____

## reverse() bawithaya.

#x=["name","government",234]
#x.reverse()
#print(x)
##>>> [234, 'government', 'name']
 ## reverse() magin list eka thula athi elments wala order eka reverse karaii.

## how to use reverse()
## list_name.reverse()

##_______---------_________--------_______-----____----___-----__---

## copy() bawithaya
#x=["name","access","new world"]
#a=["kamal","nimal",234	]
#a=a+x
#print(a)
##>>>['kamal', 'nimal', 234, 'name', 'access', 'new world']
## mehidi copy() magin adala list ekehi elements copy kara wenath list ekakata >>
##>> athulath kirimata hakiwe.

##--------_________------amthara-------______-------__--------
##x=["name","environment"]
##x[0]=100
##print(x)
##>>> [100,"environment"]
## melesada elements wenas kala hakiwe.

ALL OVER ABOUT PYTHON LIST.....
































 










































































