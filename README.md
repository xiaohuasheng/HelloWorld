# HelloWorld
django-admin startproject HelloWorld
cd HelloWorld/
ls
python3 manage.py runserver 0.0.0.0:8000
ls
django-admin startapp TestModel
ls
vim TestModel/models.py 
vim HelloWorld/settings.py 
python3 manage.py migrate
python3 manage.py makemigrations TestModel
python3 manage.py migrate TestModel

# 模板
模板路径
settings.py  
TEMPLATES  
    DIRS
