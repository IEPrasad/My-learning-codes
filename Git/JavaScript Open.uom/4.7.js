


	4.7 Handling Forms with Input Fields and Checkboxes, Radio Buttons, and Validations 


	Handling Forms 

		** HTML form can be done by a JavaScript.
		** A JavaScript function can be used to validate a form.


	Input field validation 

	function validateform() {	<<----------------------------|Function name| 		|Accessing the|
		let x = document.forms["myform"]["fname"].value; <<-----------------------  |value of the |
		if (x == "") {	<<-------------------------------- |condition for| 			|input field  |
			alert("name must be filled out"); <<-------|   | validation	 |					
			return false; << -------|				   |-------------------- |output|
		}							|----------|
	} 										   |-------|return type|



	-------------

	Checkbox validation 

       
