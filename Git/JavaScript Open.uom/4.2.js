

		Understanding DOM, Objects, and Classes

** Understanding Document 
** Object Model (DOM),
Classe and Objectsw


Objects in JavaScript 


----------------

What is DOM Ctd.


** Stands for Document Object Model
** Structure a document as a tree
** An object-oriented representation of
	a document. 

Example: 
	
		|HTML document|

<html>
<head>

	<meta charset="UTF-8">
	<title>My Title<title/>
</head>
<body>
<a href="href">my link </a>
<p id="pid"></P>
</body>
</html>

------------------

/ // 

How JavaScript Access DOM 

Example: Change the text content
		 of paragraph tag with
		 id="pid" to "Hello!".


...
...

------------

How JavaScript Access DOM ctd.

------HTML Document-----------

	<html>
	<head>
		<meta charset="UTF-8">
		<title> My Title </title>

	</head>
	<body>
	<a href="href"><my link</a>
	<p  id="pid"></p>

	// css walata <style> tag eka wagema JS walata <script> tag eka atha...

	<script>

		document.getElementById("pid").textContent="Hello!";
   
	</script>
	</body>
	</html>




---------












