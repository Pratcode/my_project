# WebResume
  
WebResume is a non-static website resume, which utilises database and 
every data which is represented is comming from database.


## Features

- We can create many sections without editing html, since data will be comming form database. 
- It is responsive based on bootstarpe.
- We can also upload resume which can be accessed in one click.
- Contact page has contact form, and social media handles section, which also connected to database.
- here i have used sqllite for testing and postgres for production.
- ones deployed we dont need to edit things manually, all things can be updated from
   admin panel.
  
# User interface

![alt text](img/UI.gif)


### How to use

Install python in the machine and set environment path, either by ticking on installer or setting up manually.
Open cmd or powershell.

###### virtual environment -

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

###### Setting up database configuration -


Download PostgreSQL from official website and install it. <br />

`note - `  <br />
`username - postgres(default)`  <br />
`password and port -'5432'(default)`  <br />

Then download/install pgadmin which is graphical tool to manage database,
it helps us to create and manage database from GUI.
```bash
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
``` 


###### To run product -

locate project folder, locate it by cmd-
```bash
> cd [project name]
```

and then to install rest of dependencies for project type- 
```bash
> pip install -r requirements.txt
```

and to start server-
```bash
> python manange.py run server
```
**---finally WebResume is running.---**

###### To start filling details and accessing admin panel -

create super user - 
```bash
> python manage.py create superuser
```
and create your admin account.

- Now type `/admin` in url after url of local host and access login panel
where u can type ur login credentials. finally u have access to admin panal. </br>
- To start seeing everything filled in WebResume u have to put data,
because database is owned by u.  


###### there are there sections in admin panel-

**messages-** where u will see all ur massages. <br />

**Person-** where u can put ur -
- name (which will be shown in navbar brand and card as well and bottom of page)
- profession (it will be shown highlighted)
- other descriptions.
- image (it is on home page)
- resume (resume page will directly load resume)
- your social media links.
- your email.

**Sections-** 
where u can put your all content, by putting title.
Every discription will be shown in bullet points.

# Admin Section 

![alt text](img/admin.gif) 

### Note----

###### If you are having difficulty in powershell, you can these steps- </br>
run powershell as administrator,
then type command- 
```bash
set-ExecutionPolicy Unrestricted
```
and then run powershell in normal mode as you were using before.


**--- Now finally your details are on WebResume ---**
