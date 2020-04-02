***
<div align="center">
  <h1> Wellcome to Django </h1>
</div>

***

### __Set up your pyhton enviroment__  

  * __Linux env__

   ``` bash
    $ python3 -m venv venv
    $ . ./venv/bin/activate
   ```
    
  * __Windows env__
  
   ``` bash
    $ python3 -m venv venv
    $ . .\venv\Scripts\activate
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

*  #### __Create a new django project__  
django-admin startproject website

* #### __Create a new webapp__
cd website  
python manage.py startapp tutorial  

python manage.py runserver

***