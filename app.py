from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_flag')
def find_flag():
    # 플래그를 파일에서 읽어옴
    flag_path = os.path.join(os.path.dirname(__file__), 'flag.txt')
    with open(flag_path, 'r') as file:
        flag = file.read().strip()
    
    response = {
        "message": "버튼이 눌렸습니다!",
        "flag": flag  
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
