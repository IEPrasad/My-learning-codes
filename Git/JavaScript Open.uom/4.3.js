

	Variables and Functions in JavaScript 


Variables in JavaScript

	** Variables in JavaScript are used to store data.
	** The data stored in a variable can change.
	** Different data types can be stored in a variable.
	** Example data types in JavaScript:

		- A number like 24
		- A string like "Anne"
		- A person object like {firstname:"Anne", age:24}


----------- How to use Variables in JavaScript ----------------


Example: 
	In this game screen, we need to display the text "Hello <username>!".


----->>>  JavaScript code

var username; <<---- create variable named username

username = "Alice"; <<---- Store data value "Alice"

document.getElementById("pid").textContent = "Hello" + username + "!";

** creating a variable uses var <variable name>
** storing  a data value uses <variable name> = <value>
** Accessing variable uses <variable name>

------------------

------------------------------------------------

Functions in JavaScript



Why Functions

Example:
	In this game screen, we need to additionally display a greeting text.

Why Functions Ctd

	------ JavaScript code ---------

var username;
username = "Alice";
document.getElementById("pid").textContent = "Hello" + username + "!";
var greeting;
greeting = "Good Morning!";
document.getElementById("pid2").textContent = greeting;


-----

			##What if we can simply call display function 


-------- JavaScript code -----------

var username;

username = "Alice";

display("pid", "Hello" + username + "!");

var greeting;

greeting = "Good Morning!"

display("pid2", greeting);

------------------------------------

What is a Function 

display(id, text)
	
Function 
	** is a block code.
	** performs a specific task.
	** reduce complexity and increase code reuse.

"pid", "Hello" -------> display(id, text) -----------> Hello!
	input					function  				   Output


------**********-------


		JavaScript Function Implementation

function display(id, text) {

	document.getElementById(id).textContent = text ;
} 



-------------------------0000---------------------


s





