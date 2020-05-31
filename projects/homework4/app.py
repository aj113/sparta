from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/oders', methods=['POST'])
def write_oder():
    # 1. 클라이언트가 준 정보 가져오기.
    name_receive = request.form['name_give']
    op_receive = request.form['op_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    oder = {
        'name': name_receive,
        'op': op_receive,
        'address': address_receive,
        'phone': phone_receive
    
    }
    # 2. DB에 정보 삽입하기
    db.oders.insert_one(oder)

	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


@app.route('/oders', methods=['GET'])
def read_oders():
    oders = list(db.oders.find({},{'_id':0}))
    return jsonify({'result':'success', 'oders': oders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)