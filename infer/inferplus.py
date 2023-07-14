import os
from flask import Flask, request, jsonify
import sys
path=os.environ.get('LIBPATH')
path='./lib'
sys.path.append(path)

from plus import sum_numbers_from_file

sys.path.append('./infer')

# WHAT TO DO
# 1. 추론과 관련없는 것은 다 날렸습니다.
# 2. 추론을 위한 코드를 추가했습니다.
# 3. 모델을 읽어오기 위한 코드를 추가했습니다. (모델 패쓰 포함)
# 4. Flask를 통한 POST 서비스를 위한 코드를 추가했습니다.

app = Flask(__name__)                   #4
app.debug = True                        #4

@app.route('/')
def hello_world():
    file_path = './data/data.txt'
    file= open(file_path, 'r')
    a=file.readlines()
    sen='Data example \n'
    for i in a:
        sen+=i
    return sen

@app.route('/add', methods=['POST'])          #4
def add():                                  #4
    if 'data' not in request.files:                #4
        return "No Data file uploaded", 400        #4
    data_file = request.files['data']             #4
    try:                                            #4
        result = sum_numbers_from_file(data_file)
        return "숫자의 총합:"+ str(result)

    except Exception as e:                              #4
        return f"Error recognizing data: {str(e)}", 500    #4

if __name__ == '__main__':      #4
    app.run(host='0.0.0.0',port=5000)                   #4