`Flask Forms`

Forms are an essential part of web applications, right from the user 
authentication interface to survey forms we require on our websites.

When the user requests the page for the first time – he receives it via 
what we call a `GET` method.

After filling the form, the user data is sent to the server via the `POST` method.

These forms are displayed to the user through templates using the ```<form> ```
attribute of HTML.
    
`GET/POST method for sending data.`

Each of these methods, also called HTTP methods, performs a specific action on the server resources. 

Each method corresponds to a different task:

1.`GET` – This method pulls specific information form the webserver (just to view it)

2.`POST` – This method sends data from the user to the server.
- ie Instagram: 
              `GET` -Allows you to see different content- posts and memes.
              `POST` -When you post a photo, you send information/data ,ie photo and caption, to the instagram application server.
     
     Blog website:
             When you are reading a blog on the website, it is through the `GET` method. When you write and publish your blog, it is through the `POST` method. 


`flask flash() method.`

Its good practice to give the user feedback for his/her actions.

Good applications and user interfaces are all about feedback. If the user 
does not get enough feedback they will probably end up hating the application.

The Flask `flash` method shows messages to the users.

With Flash, we can create a flash message in one Flask View and then show
it in another View, called `next` which usually is a template View.

Hence, a Flask view creates a Flash message in one view and then passes it to 
the next view( along with the request), which displays the message to the user.

The syntax for Flash:
     
    `flash(message,category) #keyword arguments`

message: The message to display.

category: An Optional parameter, which can be set to “error,” “info,” or “warning.”

To extract the flash message from the session, where it is stored, 
and display it on the template, we use the get_flashed_messages() function.

`get_flashed_messages(with_categories, category_filter)`

with_categories: An Optional Parameter to mention the category(error/info/warning)

category_filter: An Optional Parameter to filter and display only specific messages

`library vs modules vs package vs framework`
  
  `module`

In Python, Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program. 

In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.
  
  `package`

A package is basically a directory with Python files and a file with the name
 `__init__ .py` . This means that every directory inside of the Python path,
which contains a file named `__init__.py `, will be treated as a package by Python. 

It's possible to put several modules into a Package.

Python packages allow you to break down large systems and organize their 
modules in a consistent way that you and other people can use and reuse efficiently. 

Python's motto of "Batteries Included" means that it comes preloaded with lots of useful packages in the standard library.

  `library`

Library : It is a collection of modules. (Library either contains built 
in modules(written in C) + modules written in python). 

  `framework`

Python Web framework is a collection of packages or modules that allow developers to write Web applications or services. 

With it, developers don't need to handle low-level details like protocols, sockets or process/thread management.

`app.config('SECRET_KEY')`

-is commonly used for encryption with database connections and browser sessions. 

WTForms will use the SECRET_KEY as a salt to create a CSRF token.

`Role of underscore(_) in python`

Knowing its functions helps us write code productively

1.use in interpreter

Python automatically stores the value of the last expression in the interpreter to 
a particular variable called _ .
You can also assign these values to another variable.

2.ignoring variable

If you do not want to use specific values while unpacking, just assign that value
to _ ie 
```python
a, _, b = (1, 2, 3) or 
a, *_, b = (7, 6, 5, 4, 3, 2, 1) 
```
to ignore multiple values.
- *(variable) Is called extended unpacking. It is used to assign multiple 
values to a variable as a list

3.Use in looping

You can use _  as a variable in looping.

```python
for _ in range(5):
    print(_)

languages = ["python", "JS", "PHP", "Java"]

for _ in languages:
    print(_)
 
_ = 5
while _ < 10 :
    print(_)
    _ += 1
```
4.Separating Digits Of Numbers

If you have long digits of numbers, you can separate the group of digits for

better understanding
```python
million = 1_000_000
print(million)
```
5.Naming using _

_ can be used to name `variables, fuctions, classes.`
- single pre underscore:- _variable
- single post underscore:- variable_
- double pre underscores:- __variable
- double pre and post underscores:- `__variable__`

`_single_pre_underscore`

_name

Single pre underscore is used for internal use.(most of us do not use it for that reason)
```python
class Test:
  def __init__(self):
    self.name = "datacamp"
    self._num = 7
obj = Test()
print(obj.name)
print(obj._num)
```
single pre underscore does not stop you from accessing the single pre underscore variable.

It affects the names imported from the module
```python
##filename:- my_functions.py

def func():

  return "datacamp"

def _private_func():
  
  return 7

from my_functions import *

func()

_private_func() #returns an error
```
If you import all the methods and names from my_functions.py, Python doesn't import the names which starts with a single pre underscore.

avoid the above error by importing the module normally.
```python
import my_functions

myfunctions._private_func()
```
Single Pre Underscore is only meant to use for the internal use.

`single_postunderscore`

name_

Sometimes if you want to use Python Keywords as a variable, function or class names, you can use this convention for that.

You can avoid conflicts with the Python Keywords by adding an underscore at the end of the name which you want to use.
```python
def function(class_):
  pass
```
Single Post Underscore is used for naming your variables as Python Keywords and to avoid the clashes by adding an underscore at last of your variable name.

`Double Pre Underscore`

__name

Double Pre Underscores are used for the name mangling.

Double Pre Underscores tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts.

- Name Mangling:- interpreter of the Python alters the variable name in a way that it is challenging to clash when the class is inherited.
```python
class Sample():
  def __init__(self):
    self.a = 1
    self._b = 2
    self.__c = 3

obj1 = Sample()
dir(obj1)
print(obj1._Sample__c)
```
self.a variable appears in the list without any change.

self._b Variable also appears in the list without any change.

You will find an attribute called _Sample__c. This is the name mangling. It is to avoid the overriding of the variable in subclasses.

Create another class by inheriting Sample class to see how overriding works.
```python
class SecondClass(Sample):
  def __init__(self):
    #The super() function is used to give access to methods and properties of a parent or sibling class
    #The super() function returns an object that represents the parent class.
    super().__init__()
    self.a = "overridden"
    self._b = "overridden"
    self.__c = "overridden"

obj2 = SecondClass()
print(obj2.a)
print(obj2._b)
print(obj2.__c) #returns attribute error
```
name mangling changes the obj2.__c to _SecondClass__c. 
```python
print(obj2._SecondClass__c)
```

You can access the Double Pre Underscore variables using methods in the class. 
```python
class SimpleClass:
  def __init__(self):
    
    self.__datacamp = "Excellent"
  
  def get_datacamp(self):
    return self.__datacamp

obj = SimpleClass()
print(obj.get_datacamp()) #prints Excellent which is a __var
print(obj.__datacamp) #returns attribute error.
```
Double Pre Underscore can also be used for the method names
```python
class SimpleClass():
  
  def __datacamp(self):
    return "Excellent"
  
  def call_datacamp(self):
    return self.__datacamp()

obj = SimpleClass()
print(obj.__datacamp()) #return attribute error
print(obj.call_datacamp())
```
create a variable with name `_SimpleClass__name`, and then we will try to access that variable using Double Pre Underscore name.
```python
_SimpleClass__name = "datacamp"

class SimpleClass:
  
  def return_name(self):
    return __name

obj = SimpleClass()
print(obj.return_name()) #print datacamp
```
`Double Pre And Post Underscores`

`__name__`

In Python, you will find different names which start and end with the double underscore. They are called as magic methods or dunder methods.

This will lead to the clashes if you use these methods as your variable names. So, it's better to stay away from them.

`Property vs. Getters and Setters in Python`

- `Getters`:- These are the methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class.

- `Setters`:- These are the methods used in OOPS feature which helps to set the value to private attributes in a class.

`Private Attribute - Encapsulation`
```python
class SampleClass:
    def __init__(self, a):
    #private variable or property in python
        self.__a = a #it has been mangled
 
    #getter method to get the properties using an object
    def get_a(self):
        return self.__a
    
    #setter method to change the value 'a' using an object.
    def set_a(self, a):
        self.__a = a
```
- `__init__`:- It is used to initialize the attributes or properties of a class.

-  __a:- It is a private attribute.

- get_a:- It is used to get the values of private attribute a.

- set_a:- It is used to set the value of a using an object of a class.

You are not able to access the private variables directly in Python.

This is how you implement private attributes, getters, and setters in Python.
```python
class PythonicWay:
    def __init__(self, a):
        self.a = a
obj = PythonicWay(100)
print(obj.a)
```

`What's the difference between the above two classes.`

- SampleClass hides the private attributes and methods. It implements the encapsulation feature of OOPS.

- PythonicWay doesn't hide the data. It doesn't implement any encapsulation feature.

`What's  better to use?`

If you want private attributes and methods you can implement the class using setters, getters methods otherwise , implement the normal way.

`Property`

What if you want to have some conditions to set the value of an attribute in the SampleClass.
```python
class SampleClass1:
  def __init__(self, a):
    #calling the set_a() method to set the value of a by checking certain conditions.
    self.set_a(a)
  
  # getter method to get the property using an object
  def get_a(self):
    return self.__a
  
  # setter method to change the value "a" using an object
  def set_a(self, a):

    #condition to check whether "a" is suitable or not.
    if a > 0 and a % 2 == 0:
      self.__a = a
    else:
      self.__a = 2

obj = SampleClass(16)
print(obj.get_a())
```
How to implement the above class using the @property decorator.
```python
class Property:
  def __init__(self, var):
    #initializing the attribute
  self.a = var

  @property
  def a(self):
    return self.__a
  
  #the attribute name and the method name must be the same.
  @a.setter
  def a(self, var):
    if var > 2 and var != 0:
      self.__a = var
    else:
      self.__a = 2

obj = Property(23)
print(obj.a)
```
@property is used to get the value of a private attribute without using any getter methods. We have to put a line @property in front of the method where we return the private variable.

To set the value of the private variable, we use @method_name.setter in front of the method. We have to use it as a setter.

@a.setter will set the value of a by checking the conditions we have mentioned in the method.
```python
class AnotherWay:
  def __init__(self, var):
    #calling the set_a() method to set the value "a" by checking certain conditions
    self.set_a(var)
  
  #getter method to get the properties using an object.
  def get_a(self):
    return self.__a
  
  #setter method to change the value 'a' using an object
  def set a(self, var):
    
    #condition to check whether var is suitable
    if var > 2 and var % 2 == 0:
      self.__a = var
    else:
      self.__a = 2

  a = property(get_a, set_a)

obj =  AnotherWay(28)
print(obj.a)
```
Pass all the getter and setter methods to the property and assign it to the variable which you have to use as a class attribute.

Make the setter and getter methods as private to hide them.
```python
class FinalClass:
    def __init__(self,var):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.__set_a(var)
    
    ## getter method to get the properties using an object
    def __get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def __set_a(self, var):
      
      ## condition to check whether var is suitable or not
      if var > 2 and var % 2 == 0:
        self.__a = var
      else:
        self.__a = 2

    a = property(__get_a, __set_a)

obj = FinalClass(26)
print(obj.a)
```
```python
class Portal:
  def __init__(self):
    self.__name = ""
  
  #using @property decorator
  @property
  def name(self):
      return self.__name
  
  #setter method
  @name.setter
  def name(self, var):
    self.__name = var
  
  #deleter method
  @name.deleter
  def name(self):
    del self.__name

#creating object
p = Portal()

#setting name
p.name = "Unicorn"

#prints name
print(p.name)

#deletes name
del p.name

#as name is deleted above this will throw an error.
print(p.name)
```
Here, the @property decorator is used to define the property name in the class Portal, that has three methods(getter, setter, and deleter) with similar names i.e, name(), but they have different number of parameters. Where, the method name(self) labeled with @property is a getter method, name(self, val) is a setter method as it is used to set the value of the attribute __name and so its labeled with @name.setter. Lastly, the method labeled with @name.deleter is a deleter method which can delete the assigned value by the setter method. However, deleter is invoked with the help of a keyword del.

`flask login`
`load_user`

Flask-login will try and load a user BEFORE every request. Your code will be called before every request. It is used to check what userid is in the current session and will load the user object for that id.

load_user is critical for making our app work: before every page load, our app must verify whether or not the user is logged in (or still logged in after time has elapsed). user_loader loads users by their unique ID. If a user is returned, this signifies a logged-in user. Otherwise, when None is returned, the user is logged out.

Flask-Login can manage user sessions. Start by adding the UserMixin to your User model. The UserMixin will add Flask-Login attributes to the model so that Flask-Login will be able to work with it.
`installation`

```python
pip install flask-login
```
The most important part of an application that uses `Flask-Login` is the `LoginManager` class. 

```python
login_manager = LoginManager(app)
```
The login manager contains the code that lets your application and Flask-Login work together, such as how to load a user from an ID, where to send users when they need to log in, and the like.

By default, Flask-Login uses sessions for authentication. This means you must set the `secret key` on your application, otherwise Flask will give you an error message telling you to do so.

Each Flask web application contains a `secret key` which used to sign session cookies for protection against cookie data tampering. It's very important that an attacker doesn't know the value of this secret key.

`How it Works`

You will need to provide a `user_loader` callback. This callback is used to reload the user object from the user ID stored in the session. It should take the unicode ID of a user, and return the corresponding user object.
```python
@login_manager.user_loader
def load_user(user_id):
  return User.get(user_id)
```
It should return None (not raise an exception) if the ID is not valid. (In that case, the ID will manually be removed from the session and processing will continue.)

`Your User Class`

The class that you use to represent users needs to implement these properties and methods:

`is_authenticated`

This property should return True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)

`is_active`

This property should return True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).

`is_anonymous`

This property should return True if this is an anonymous user. (Actual users should return False instead.)

`get_id()`

This method must return a unicode that uniquely identifies this user, and can be used to load the user from the user_loader callback. **Note that this must be a unicode - if the ID is natively an int or some other type, you will need to convert it to unicode.**

To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations for all of these properties and methods. (It’s not required, though.)
