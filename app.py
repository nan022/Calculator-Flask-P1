from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/penjumlahan', methods=['GET'])
def show_penjumlahan():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'message': 'GET request is working!'})

@app.route('/penjumlahan', methods=['POST'])
def save_penjumlahan():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hasil = bil1+bil2
    print(hasil)
    return jsonify({'message': hasil})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)