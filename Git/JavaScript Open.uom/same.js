
(1) ---------->>
python 							
	print("Hello!")
JS 
	console.log("Hello!")


(2)----------->>
python

def Name(age,mark):
	print(age)
	print(mark)
Name(int(input("Enter age: ")), int(input("Enter mark: ")))


JS

function Name(age, mark) {
	console.log(age);
	console.log(mark);
}

Name(parseInt(prompt("Enter age: ")), parseInt(prompt("Enter mark: ")));



(3)------------->>

class test1:
	def details(name,age):
		print(Name, "is",age,"year old.")

	def subj(maths,science):
		print(maths)
		print(science)
		return maths


myobj = test1()
myobj.subj("Kamal", 31)
myobj.subj(31,76)

myobj.details("John", 25)




JS

class test1 {
	details(name, age){
		console.log(name+ "is" + age + "years old.");

	}

	subj(maths, science) {
		console.log(maths);
		console.log(science);
		return maths;
	}
}

let myobj = new test1();
myobj.subj("Kamal", 31);
myobj.subj(31, 76);

myobj.details("John", 25);























