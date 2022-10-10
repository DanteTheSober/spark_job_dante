from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']

        # put data to postgresql database
        data = pd.read_csv(file)
        engine = create_engine('postgresql://root:root@localhost:5432/sensor_data')
        print(pd.io.sql.get_schema(data, name='sensor_data', con=engine))
        data.to_sql(name='sensor_data', con=engine, if_exists='append')


        return render_template('data.html', data=data.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
