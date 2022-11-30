from flask import Flask,jsonify,request
import pandas as pd
import os

file_path = 'VERB_QUIZ_007.csv'
df = pd.read_csv(file_path, encoding='utf-8')

quiz_set_flask = df.sample(frac=1).reset_index(drop=True)
quiz_set_flask = quiz_set_flask.to_dict('records')


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def ReturnJSON():
	if(request.method == 'GET'):

		return jsonify(quiz_set_flask)

if __name__=='__main__':
	app.run(debug=True)
