

			4.6 Loops and Conditions 

Different kinds of Loops in JavaScript 

	** for - loops through a block of code a number of times 
	** for/in - loops through the properties of an object 
	** for/of - loops through the values of an inerrable object
	** while - loops through a block of code while a specified condition is true
	** do/while - also loops through a block of code while a specified condition is true

/
The for loop 
	## Structure 
		for (statement1; statment2; statment3){
			// code block to be executed 
		}


		## Statment 1 is executed (one time) before the execution of the code block
		## Statment 2 defines the condition for executing the code block 
		## Statment 3 is executed (every time) after the code block has been executed



		for (let i = 0; i < 5; i++){
			text += "The number is " + i + "<br>";	
		}

-----------------


		The For In Loop


		for (key in object){
			// code block to be executed
		}

		-------- ----

		const values = [150, 100, 150, 160, 250];

		let txt = "";
		for (let x in values) {
			txt += values[x];
		}

------------------


		The For Of Loop


		for (variable of iterable){
			//code block to be executed 
		}


		------ ------

		const animals = ["CAT", "DOG", "PARROT"];

		let text = "";
		for (let x of animals){
			text += x;		
		}


----------------------


		The While Loop

		while (condition){
			// code block to be executed 
		}


		Conditianl Statments

		** Conditianl Statments control the behaviour in JavaScript an determine 
		   whether pieces of code can run depending on the decesion.


		Conditions 

			if (condition){
				// block of code to be executed if the condition is true
			}


			----- ----

			if (age < 18){
				message = "Not an Adult";
			} else {
				message = "An Adult";
			} 


--------------- 










