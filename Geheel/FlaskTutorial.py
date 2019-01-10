from flask import Flask, redirect, request, url_for, render_template, make_response
app = Flask(__name__)


@app.route('/')
def home_page():
    punten = {"Bob": 23, "Jan": 45, "Jef": 4}
    return render_template('home_page.html', result=punten)


# Tussen <> betekent een parameter
@app.route("/hello?name=<name>score=<score>")
def hello_name(name, score):
    print("Redirected to hello_name")
    if name == 'admin':
        return redirect('/admin_page')
    # score = int(request.cookies.get('score'))
    print("Showing hello_name:", name, score)
    return render_template('hello_name.html', name=name, score=int(score))
    # return "test"

@app.route('/admin_page')
def hello_admin():
    print("Showing hello_admin")
    return 'Hi administrator! :-)'


# Gaat ook met <float:ID>
@app.route('/number/<int:ID>')
def hello_number(ID):
    print("Showing hell_number:", ID)
    if ID%2 == 0:
        return 'That\'s an even number'
    else:
        return "That's an odd number"

@app.route('/setcookie', methods=['POST'])
def setcookie():
    message = request.form['message']
    resp = make_response(redirect('/getcookie'))
    resp.set_cookie('score', message)
    print("Cookie created")
    return resp

@app.route('/getcookie')
def getcookie():
    message = request.cookies.get('score')
    return "Cookie: " + message

# Maakt gebruik van hello_name.html
@app.route('/login_form', methods=['POST', 'GET'])
def login():
    print("Handling login...")
    if request.method == "POST":
        user = request.form['naam']
        score = request.form['score']

        print("Request:", user, score)

        return redirect(url_for('hello_name', name=user, score=score))
    else:
        # GET, wordt nooit gebruikt want home_page gebruikt post
        user = request.args.get("naam")
        score = request.args.get("score")
        return redirect('hello_name', name=user, score=score)


if __name__ == '__main__':

    app.debug = True
    app.run()
