#hypotenuse
#katet a=3 b=4
import math 
a = 3
b = 4
hypotenusa = a**2 + b**2
print(hypotenusa)

hypoteneuse_c2 = 7.0
a2 = 5.0
cathetus = math.sqrt((hypoteneuse_c2**2) - (a2**2))
bresult = f"{cathetus:.1f}"
print(bresult)

#classification accuracy
accuracy = 300/365
print(f"{accuracy:.0%}" + " accuracy")

#very accurate model yes 98% accuracy 

#file metadata
filename = "sales_data.csv"
filesize_mb = 3.14 
lastmodified = 2024
metadata = f"filename:{filename} \nfilesize(mb):{filesize_mb} \nLastmodified:{lastmodified}" 
print(metadata)

#inch to cm converter 
inchesinput = float(input("type in inches"))
print(f"{inchesinput} inches is {inchesinput * 2.54} cm")

#countcharacters 
typein = input("please type something")
print(f"your input contains {len(typein)} characters!")

#data types
number = 5
coolguy = True
subject = "math"
pi = 3.1415
listo = ["kaka","maka","baka","waka"]
print(f"number: {number} has type {type(number)}, \n coolguy: {coolguy} has type {type(coolguy)}, \n subject: {subject} has type {type(subject)}, \n pi: {pi} has type {type(pi)}, \n listo: {listo} has type {type(listo)}")

#terminology	explanation
#data type	    type of data in a variable 
#variable	    name for a function or a data container/holder 
#assignment	    assigning something to a variable = giving data to a variable
#dynamically typed	    in a dynamically typed language cheking of datatypes happens at runtime which makes program a bit slower but more effective for acutal writing but n a statically typed language datatype checking happens at compile time(eg before runtime)
#input	        instructions for computer or program
#output	        the results of said executed instructions
#type casting	giving a specific type to a data/variable content 
#boolean	    a datatype that can be either true or false
#string	        a datatype that is just treated as text and does not have any function other than being readable to humans
#f-string	    a hybrid string of both only readable text and pointers/operations
#indentation	space : :   :   :before a new code block or a nested codeblock for more clearer and readable code
#convention	    unwritten rules for programmers that are mainstreamly accepted such as CamelCasing when naming things.