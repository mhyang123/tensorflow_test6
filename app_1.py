from flask import Flask, render_template, request, jsonify
from member.controller import MemberController
from ai_calc.controller import CalcController
from blood.model import BloodModel
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    userid = request.form['userid']
    password = request.form['password']
    print('로그인 들어온 아이디 {}, 비번 {}'.format(userid, password))
    c = MemberController()
    view = c.login(userid, password)
    return render_template(view)

@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))

#윗 4개 move뒤 단어를 변수로 <>추가하여 처리한다.
#변수를 path로 변경
#{}--->form(path)
'''
@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))
'''


@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt', 'NONE')
    if(stmt == 'NONE'):
        print('넘어온 값이 없음')
    else :
        print('넘어온 식 {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자 {}'.format(op))
        nums = stmt.split(op)
        result = 0
        if op == '+':
            result = int(nums[0]) + int(nums[1])
        elif op == '-':
            result = int(nums[0]) - int(nums[1])
        elif op == '*':
            result = int(nums[0]) * int(nums[1])
        elif op == '/':
            result = int(nums[0]) /int(nums[1])

    return jsonify(result= result)


@app.route('/ai_calc',methods=['POST'])
def ai_calc():
    num1=request.form(['num1'])
    num2=request.form(['num2'])
    opcode=request.form(['opcode'])
    print('계산기에 들어온 num1={},num2={},opcode={}'.format(num1, num2, opcode))
    c = CalcController(num1, num2, opcode)
    result=c.calc()
    render_params={}
    render_params['result']=result
    return render_template('ai_calc.html',**render_params)


@app.route('/blood',method="POST")
def blood():
    weight=request.form(['weight'])
    age=request.form(['age'])
    print(" weight:{},age:{}".format(weight,age))
    model=BloodModel("blood/data/data.txt")
    raw_data=model.create_raw_data()
    render_params={}
    value=model.create_model(raw_data,weight,age)
    render_params['result']  =value  #render_params==값;다른건 hmtl과 관련됨
    return render_template('blood.html',**render_params)


'''
@app.route('/gradient_descent')
def gradient_descent():
    weight=request.form(['weight'])
    age=request.form(['age'])
    print(" weight:{},age:{}".format(weight,age))
    model=BloodModel("blood/data/data.txt")
    raw_data=model.create_raw_data()
    render_params={}
    value=model.create_model(raw_data,weight,age)
    render_params['result']  =value  #render_params==값;다른건 hmtl과 관련됨
    return render_template('blood.html',**render_params)
'''
if __name__ == '__main__':
    app.run()