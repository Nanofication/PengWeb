from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'PengYu Web Homepage'

if __name__ == '__main__':
    app.run(debug=True)
