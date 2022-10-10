# Windows
####To create the python environment for this application
 python -m venv venv

####To access the environment
.\venv\Scripts\activate

####To install all required libraries 
pip install -r requirements.txt

####To build up database
#### you need to install docker compose and also docker is ready on your device
docker-compose up

####To upload the csv file and activate API
terminal 1
if you use Spunk -> cd upload-app -> python app.py -> access http://127.0.0.1:5000
if you use fastAPI -> cd fastAPI -> uvicorn api:app --reload -> http://127.0.0.1:8000/docs

#### Check if data has been ingested into DB
pgcli -h localhost -p 5432 -U root sensor_data

#### To run the spark job
python spark-etl-job.py

*note : you need to change the line 19 of the spark-etl-job.py to the path Window accept


# Linux
#### create virtual env name  spark-etl-env

python -m venv spark-etl-env

#### activate venv

source spark-etl-env/bin/activate

#### install dependencies (ls -l spark-etl-env/lib)

pip install -r requirements.txt

#### open 2 terminal with this virtualenv

####terminal 1
if you use Spunk -> cd upload-app -> python app.py -> access http://127.0.0.1:5000 
if you use fastAPI -> cd fastAPI -> uvicorn api:app --reload -> http://127.0.0.1:8000/docs

####terminal 2

python spark-etl-job.py

*note : you need to change the line 19 of the file spark-etl-job.py to the path which Linux accept