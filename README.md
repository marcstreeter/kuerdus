# Calendar

meant to provide easy way to add
entries to calendar for missionaries 

### development

```
cd api/src
export FLASK_ENV=development
export FLASK_APP=serve.py
flask run
```

#### Building

```
cd api/src
docker build . -t calendar
docker run --rm -p 8080:8080 calendar
```
