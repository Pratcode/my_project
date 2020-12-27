-WebResume-

The WebResume is a website resume platform, which is minimalist in nature,
means that it doesn't have cluttered design, it has card based modular design,
where many sections can be created as per need, it is responsive, means that it can be viewed in any kind of screen size,
here we can also upload resume which can be accessed in one click, and contact section has many ways to contact a person.

Install python in the machine and set environment path, either by ticking on installer or setting up manually.
Open cmd or powershell.

virtual environment----

Locate the project and extract it.
and then if you have other project and don't wanna mess up dependency, install virtual environment-
```bash
> pip install virtualenv
```
then create environment-
```bash
> virtualenv [name of env]
```
then to activate it-
```bash
> cd [name of env]
> cd Scripts
> activate.bat and ./activate.ps1 for powershell
```

Setting up database configuration----


Download PostgreSQL from official website
and install it.
and note username - postgres(default), password and port -'5432'(default)

and then download/install pgadmin which is graphical tool to manage database,
it helps us to create and manage database from GUI.

DATABASES = {
    'default': {
      'ENGINE': 'django.db.back ends.PostgreSQL',             -----(which will remain same)
      'NAME': 'my_database',                                  -----(create database names- my_database in pg admin and put that same name here
                                                               you can create database with other names too but name should be same in settings)
      'USER': 'postgres'                                      -----(set by default in postures)
      'PASSWORD': 'set by you' generally -'1234',             -----(it is a password which has been setup by u while installing postgres)
      'HOST': 'local host',                                   ------(local host is ur machine)
      'PORT': 'your port numb' generally -'5432',             ------(port number is shown at installing PostgreSQL, generally--'5432')

     }
}



To run product----


locate project folder, locat it by cmd-
> cd [project name]

and then to install rest of dependencies for project type- 
> pip install -r requirements.txt

and to start server-
> python manange.py run server

and finally your website is running.



To start filling details and accessing admin panel----

create super user - 
> python manage.py create superuser
and create your admin account,

now type /admin in url after url of local host and access login panel
where u can type ur login credentials.

and finally u have access to admin panal.

To seeing everything filled in web resume u have to put data,
because database is owned by u.

there are there sections in admin panel-

Contacts- where u will see all ur massages.
Media - where u can put ur -

(1) name (which will be shown in navbar brand and card as well and bottom of page)
(2) profession (it will be shown highlighted)
(3) other description.
(4) image (it is on home page)
(5) resume (resume page will directly load resume)
(6) to (15)and (17) - your social media links.
(16) here you can put your email.
Which will directly redirect user to mail client.
your copyright in buttom of page will load automatically as u put info.

Data-
where u can put your all content, by putting title.
Every discription will be shown in bullet points,
this section is based on cards where u can create as many cards,
based on your need, which is shown in your home page.


Note----


If you are having difficulty in powershell, you can these steps-
run powershell as administrator,
then type command- set-ExecutionPolicy Unrestricted
and then run powershell in normal mode as you were using before.



----Now finally your details are on website---
