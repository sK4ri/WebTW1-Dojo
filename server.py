from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/request')
def get_request():
    return render_template('request.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
