*** 
# __ZAPPA__

***
### __Create your env__
```
python -m venv venv
venv/Script/activate
pip install -r requirements.txt
pip install -U zappa

```

### __Start or clone a project__   
_Ref:_ https://romandc.com/zappa-django-guide/

```
django-admin startproject zappa_inecsoft
cd zappa_inecsoft
python manage.py runserver
```

### __Inicialize the project__
```
zappa init
```
### __Deploy your app to the cloud__
```
zappa deploy 
```
#### _NOTE:_ Add to the api url settings.py  
```
ALLOWED_HOSTS = [ '127.0.0.1', 'x6kb437rh.execute-api.us-east-1.amazonaws.com', ]
```

### __Rolling update on the App__
```
zappa update
```
### __Debug your app__
```
zappa tail
```

### __Rollback to previous version__
```
zappa rollback production -n 3
```
### __If you need to see the status of your deployment and event schedules__  
```
zappa status
```
***