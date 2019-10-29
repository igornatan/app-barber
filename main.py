from flask import *

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/produtos')
def produtos():
    return render_template('produtos.html')


if __name__ == '__main__':
    app.run(debug=True)
