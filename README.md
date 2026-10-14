# **Temperature Converter using Python**



###### **Description**



This project is a simple Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin.



The program provides six different conversion options:



1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



The program uses Python functions, arithmetic operations, conditional statements, user input, and input validation.



###### **Objective**



The main objectives of this project are:



\- To practice Python functions

\- To understand return statements

\- To perform arithmetic calculations

\- To use if-elif-else statements

\- To take input from the user

\- To validate temperature values

\- To format decimal output using round()



###### **Technologies Used**



\- Python

\- IDLE / Python Interpreter



###### **Features**



\- Converts Celsius to Fahrenheit

\- Converts Celsius to Kelvin

\- Converts Fahrenheit to Celsius

\- Converts Fahrenheit to Kelvin

\- Converts Kelvin to Celsius

\- Converts Kelvin to Fahrenheit

\- Validates physically meaningful temperature values

\- Displays results up to two decimal places

\- Uses separate functions for each conversion

###### 

###### **Conversion Formulas**



**1. Celsius to Fahrenheit**



Fahrenheit = (Celsius × 9/5) + 32



**2. Celsius to Kelvin**



Kelvin = Celsius + 273.15



**3. Fahrenheit to Celsius**



Celsius = (Fahrenheit - 32) × 5/9



**4. Fahrenheit to Kelvin**



Kelvin = (Fahrenheit - 32) × 5/9 + 273.15



**5. Kelvin to Celsius**



Celsius = Kelvin - 273.15



**6. Kelvin to Fahrenheit**



Fahrenheit = (Kelvin - 273.15) × 9/5 + 32



###### **Python Program**

def celsius\_to\_fahrenheit(c):

&#x20;   return (c \* 9/5) + 32





def celsius\_to\_kelvin(c):

&#x20;   return c + 273.15





def fahrenheit\_to\_celsius(f):

&#x20;   return (f - 32) \* 5/9





def fahrenheit\_to\_kelvin(f):

&#x20;   return (f - 32) \* 5/9 + 273.15





def kelvin\_to\_celsius(k):

&#x20;   return k - 273.15





def kelvin\_to\_fahrenheit(k):

&#x20;   return (k - 273.15) \* 9/5 + 32





print("Temperature Converter")

print("---------------------")



print("1. Celsius to Fahrenheit")

print("2. Celsius to Kelvin")

print("3. Fahrenheit to Celsius")

print("4. Fahrenheit to Kelvin")

print("5. Kelvin to Celsius")

print("6. Kelvin to Fahrenheit")



c = int(input("Enter your choice: "))

temperature = float(input("Enter temperature: "))



if c == 1:

&#x20;   if temperature < -273.15:

&#x20;       print("Invalid temperature")

&#x20;   else:

&#x20;       result = celsius\_to\_fahrenheit(temperature)

&#x20;       print("Result:", round(result, 2), "°F")



elif c == 2:

&#x20;   if temperature < -273.15:

&#x20;       print("Invalid temperature")

&#x20;   else:

&#x20;       result = celsius\_to\_kelvin(temperature)

&#x20;       print("Result:", round(result, 2), "K")



elif c == 3:

&#x20;   if temperature < -459.67:

&#x20;       print("Invalid temperature")

&#x20;   else:

&#x20;       result = fahrenheit\_to\_celsius(temperature)

&#x20;       print("Result:", round(result, 2), "°C")



elif c == 4:

&#x20;   if temperature < -459.67:

&#x20;       print("Invalid temperature")

&#x20;   else:

&#x20;       result = fahrenheit\_to\_kelvin(temperature)

&#x20;       print("Result:", round(result, 2), "K")



elif c == 5:

&#x20;   if temperature < 0:

&#x20;       print("Invalid temperature")

&#x20;   else:

&#x20;       result = kelvin\_to\_celsius(temperature)

&#x20;       print("Result:", round(result, 2), "°C")



elif c == 6:

&#x20;   if temperature < 0:

&#x20;       print("Invalid temperature")

&#x20;   else:

&#x20;       result = kelvin\_to\_fahrenheit(temperature)

&#x20;       print("Result:", round(result, 2), "°F")



else:

&#x20;   print("Invalid choice")



###### **Sample Outputs**

**Example 1: Celsius to Fahrenheit**

Temperature Converter

\---------------------

1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



Enter your choice: 1

Enter temperature: 98

Result: 208.4 °F



**Example 2: Celsius to Kelvin**

Temperature Converter

\---------------------

1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



Enter your choice: 2

Enter temperature: 87

Result: 360.15 K



**Example 3: Fahrenheit to Celsius**

Temperature Converter

\---------------------

1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



Enter your choice: 3

Enter temperature: 78

Result: 25.56 °C



**Example 4: Fahrenheit to Kelvin**

Temperature Converter

\---------------------

1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



Enter your choice: 4

Enter temperature: 89

Result: 304.82 K



**Example 5: Kelvin to Celsius**

Temperature Converter

\---------------------

1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



Enter your choice: 5

Enter temperature: 89

Result: -184.15 °C



**Example 6: Kelvin to Fahrenheit**

Temperature Converter

\---------------------

1\. Celsius to Fahrenheit

2\. Celsius to Kelvin

3\. Fahrenheit to Celsius

4\. Fahrenheit to Kelvin

5\. Kelvin to Celsius

6\. Kelvin to Fahrenheit



Enter your choice: 6

Enter temperature: 78

Result: -319.27 °F



###### **Input Validation**

The program checks whether the entered temperature is physically meaningful.

**Celsius**

The lowest possible temperature is -273.15°C.

if temperature < -273.15:    print("Invalid temperature")





**Fahrenheit**

The lowest possible temperature is -459.67°F.

if temperature < -459.67:    print("Invalid temperature")





**Kelvin**

Kelvin cannot be less than 0 K.

if temperature < 0:    print("Invalid temperature")





###### **Python Concepts Used**

**1. Functions**

Separate functions are created for each temperature conversion.

Example:

def celsius\_to\_fahrenheit(c):    return (c \* 9/5) + 32



**2. Return Statement**

The return statement sends the calculated result back to the calling statement.

Example:

return c + 273.15



**3. User Input**

The program takes the conversion choice and temperature from the user.

c = int(input("Enter your choice: "))temperature = float(input("Enter temperature: "))



**4. Conditional Statements**

The program uses if, elif, and else to select the required conversion.

if c == 1:



**5. Arithmetic Operators**

The program uses multiplication, division, addition, and subtraction for temperature calculations.


**6. Round Function**

The round() function is used to display the result up to two decimal places.

round(result, 2)



###### **Advantages**

\- Simple and easy to use

\- Beginner-friendly Python project

\- Uses functions for better organization

\- Provides multiple temperature conversions

\- Includes input validation

\- Gives formatted output

###### 

###### **Conclusion**

The Temperature Converter is a beginner-friendly Python project that demonstrates the use of functions, return statements, arithmetic operations, conditional statements, user input, validation, and output formatting.

This project helps in understanding how functions can be used to perform repeated calculations and how user input can be processed to produce useful results.

