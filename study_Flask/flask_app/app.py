from flask import Flask, render_template  # render_template을 불러옵니다.

app = Flask(__name__)  # Flask 앱 생성

@app.route("/")  # 기본 경로("/")
def home():
    name = "홍길동"
    message = "Flask를 배우는 중입니다!"
    return render_template("index.html", name=name, message=message)  # 데이터 전달


if __name__ == "__main__":
    app.run(debug=True)  # Flask 앱 실행
