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
 __init__ .py . This means that every directory inside of the Python path,
which contains a file named __init__.py , will be treated as a package by Python. 

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
- double pre and post underscores:- __variable__

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
