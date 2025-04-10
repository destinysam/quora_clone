## Steps to setup project


### Clone project

```
git glone https://github.com/destinysam/quora_clone
```

### Setup environment 

```
python3 -m env venv
```

### Activate environment

```
source env/bin/activate
```

### Setup dependencies

```
pip install -r requirements.txt
```

### Run the migrations

```
python3 manage.py makemigrations
```
### Migrate changes

```
python3 manage.py migrate
```

### Finally, start project

```
python3 manage.py runserver
```

### To check all questions

```
http://127.0.0.1:8000/
```

### To signup

```
http://127.0.0.1:8000/signup
```

### To Login

```
http://127.0.0.1:8000/login
```


### To View question

```
http://127.0.0.1:8000/question/question_id/
```


### To add question

```
http://127.0.0.1:8000/post-question/
```
