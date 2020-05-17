***
# __Portafolio project__

***
### __Start project and Apps__

python -m venv venv
venv/Script/activate
or 
source /venv/bin/activate

```
django-admin startproject portafolio
cd portafolio
django-admin startapp blog
django-admin startapp jobs
touch .gitignore
cd ..
mv portafolio portafolio-project
cd portafolio-project
```
### __manage your repo__
```
git init
git add .
git commit "first commit"
git push
```
### __Add modules__
app/models.py

 ```
python manage.py migrate
python manage.py makemigrations
```
### __Add the following to settings__

INSTALLED_APPS = [
  'jobs.JobsConfig',
     
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL  = '/media/'

***
pip install Django-environ

_Note:_
edit settings with SECRET_KEY = env('SECRET_KEY')
https://django-environ.readthedocs.io/en/latest/

.env
SECRET_KEY=SECRET_KEY
***