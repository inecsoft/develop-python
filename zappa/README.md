*** 
# __ZAPPA__

***
### __Create your env__
```
python -m venv venv
venv/Script/activate
pip install -r requirements.txt
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

### __Rolling update on the App__
```
zappa update
```
### __Debug your app__
```
zappa tail
``` 
***