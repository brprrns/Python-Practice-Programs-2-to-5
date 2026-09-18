# Python Assignment Practice Program 2 to 5

### Questions

2. Define a class Person and its two child classes: Male and Female. All classes have
a method "get_gender" which can print "Male" for Male class and "Female" for Female
Class.
Bonus: Make class Person an abstract class and make get_gender an abstract method in the
same class. The two child classes must inherit and implement get_gender. i.e., When trying to
initialize an object of class Person, the program must throw an error.
Hint:
Use ABC library (comes natively with Python3)
The 'ABC' of Abstract Base Classes | OOP | python-course.eu
abc — Abstract Base Classes — Python 3.10.0 documentation

3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
Hint: Use set() to store a number of values without duplicates.

4. Write a program that can map() to make a list whose elements are squares of numbers
between 1 and 20 (both included).
Hints:
Use map() to generate a list.
Use Lambda to define anonymous functions.

5. Write a program anti_html.py that takes a URL as an argument, downloads the HTML from
the web, and prints it after stripping HTML tags.
