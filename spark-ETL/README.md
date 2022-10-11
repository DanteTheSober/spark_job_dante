# Linux
### create virtual env name  spark-etl-env

python -m venv spark-etl-env

### activate venv

source spark-etl-env/bin/activate

### install dependencies (ls -l spark-etl-env/lib)

pip install -r requirements.txt

### open 2 terminal with this virtualenv

###terminal 1
if you use Flask -> cd upload-app -> python app.py -> access http://127.0.0.1:5000 -> upload the data.csv file in upload-app
if you use fastAPI -> cd fastAPI -> uvicorn api:app --reload -> http://127.0.0.1:8000/docs -> upload the data.csv file in upload-app

###terminal 2

python spark-etl-job.py

*note : you need to change the line 19 of the file spark-etl-job.py to the path which Linux accept