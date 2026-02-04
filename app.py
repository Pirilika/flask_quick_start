from flask import Flask
from flask import url_for, redirect, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return "<p>おはよう！世界！<p>"

@app.route("/echo/<echo>")
def echo_url(echo):
    return f"<p>{escape(echo)}<p>"

@app.route("/greet_user/<string:user>")
def greet_user(user):
    return f"<p>Hello, {escape(user)}<p>"

@app.route('/seacret/<string:args>')
def out_put_page(args):
    return f"Ya! {escape(args)}"

@app.route('/Ya')
def Ya():
    args:str = "Power!!"
    print(url_for('out_put_page', args=args))
    return redirect(url_for('out_put_page', args=args))

@app.route('/get_html', methods=["GET"])
def get_html():
    return "<p>HTML<p>"

@app.route('get_html', methods=["POST"])
def post_html():
    # db操作など
    return "Your request Done"


@app.get('/get_my_html')
def get_html2():
    return "<p>HTML2<p>"

@app.post('get_my_html')
def post_html2():
    # db操作など
    return "Your request Done"

@app.route('/users', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        #db操作など
        return "Add User"
    return "Add User Form"

@app.get('/user2')
@app.post('/user2')
def add_db_user():
    if request.method == "POST":
        #db操作など
        return "Add User"
    return "Add User Form"       



if __name__ == "__main__":
    app.run(debug=True)
    with app.test_request_context():
        Ya()