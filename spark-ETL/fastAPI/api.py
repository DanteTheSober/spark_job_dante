from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine

app = FastAPI()

@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    data = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
    print(data)
    engine = create_engine('postgresql://root:root@localhost:5432/sensor_data')
    print(pd.io.sql.get_schema(data, name='sensor_data', con=engine))
    # data = data.set_index("sensor_id")
    print(data)
    data.to_sql(name='sensor_data', con=engine, if_exists='append')
    exec(open("../spark-etl-job.py").read())
    return {"file_name": file.filename + " has been saved to database"}