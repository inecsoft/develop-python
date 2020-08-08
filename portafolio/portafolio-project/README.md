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

***
# __Database Posgres__
docker run -itd --name postgres --rm -e POSTGRES_USER=postgres -e POSTGRES_DB=portafoliodb -e POSTGRES_PASSWORD=mysecretpassword postgres  

docker exec -it postgres psql -U postgres  

docker run --name postgres -user "$(id -u):$(id -g)" -v ./data/web/database:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpassword -d postgres  

docker exec -it postgres bash  

psql -l  

* __Create User__
  createuser cent

* __Show users and databases__
  psql -c "select usename from pg_user;"

* __Create new db own by cent user__
  createdb dbname -O cent

* __Conect to the database__
  psql dbname

* __Create table__
create table test_table (no int, name test);

* __Insert data in the table__
insert into test_table (no,name) values (01,'CentOS');

* __Exit database__
  \q

* __Delete db__
  dropdb dbname