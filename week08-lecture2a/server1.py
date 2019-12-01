from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='.')
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

@app.route('/books')
def getAll():
    return "in getALL"

@app.route('/books/<int:id>')
def findByID(id):
    return "in find by ID for id"+str(id)

if __name__ == '__main__' :
    app.run(debug= True)