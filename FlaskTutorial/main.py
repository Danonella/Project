from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('one.html')


@app.route('/two', methods=['POST'])
def success1():
    if request.method == 'POST':
        return render_template('two.html')
    else:
        pass


@app.route('/three', methods=['POST'])
def success2():
    if request.method == 'POST':
        return render_template('three.html')
    else:
        pass


@app.route('/four', methods=['POST'])
def success3():
    if request.method == 'POST':
        return render_template('four.html')
    else:
        pass


@app.route('/five', methods=['POST'])
def success4():
    if request.method == 'POST':
        return render_template('five.html')
    else:
        pass


@app.route('/six', methods=['POST'])
def success5():
    needValues = request.values.to_dict()
    if request.method == 'POST':
        if needValues['radio1'] == '1':
            return render_template('six.html')
        elif needValues['radio1'] == '2':
            return render_template('seven.html')
    else:
        pass


@app.route('/eight', methods=['POST'])
def success6():
    if request.method == 'POST':
        return render_template('eight.html')
    else:
        pass


if __name__ == "__main__":
    app.run()
