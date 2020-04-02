***
<div align="center">
  <h1> Wellcome to Django </h1>
</div>

***

### __Set up your pyhton enviroment__  

  * __Linux env__

   ``` bash
    $ python3 -m venv venv
    $ ./venv/bin/activate
   ```
    
  * __Windows env__
  
   ``` bash
    $ python3 -m venv venv
    $ ..\venv\Scripts\activate
   ```
##### __Note:__
(venv) $ which python

* #### __Install Django__  
pip install django

* #### __Update pip__  
python -m pip install --upgrade pip  

***  
* #### __Customise visual Studio Code__

ctl + shift + P and search for themes 

* #### __To find the path to your python verion__
import sys  
print(sys.executable)  

***  
* #### __Start your project in Visual Studio Code__  
code .  

    - _Create new terminal_  
    - _Select the venv_  

*  #### __Create a new django project__  
django-admin startproject django_project  

* #### __Create a new webapp__
cd django_project    
python manage.py startapp blog  

* #### __Run the app__
python manage.py runserver

***
* #### __First stpes__
  - Copy urls.py from django_project to blog.  
  - Create your fuction in wiews, like home and about.  
  - Set the path to views on urls in blog folder
  - Set the path to the new web app in urls in django_project folder.  
  - Add this config in settings.py INSTALLED_APPS = [ 'blog.apps.BlogConfig',  
  
***

* #### __Second steps__
``` bash
mkdir template  
cd template  
mkdir blog  
touch home.html about.html base.html 
```

***