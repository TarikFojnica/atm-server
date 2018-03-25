#app.py

from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/authenticate-card')
def get():
    card_id = request.args.get('card_id') #if key doesn't exist, returns None

    return '''<h1>The card id is: {}</h1>'''.format(card_id)

@app.route('/form-example')
def form_example():
    return 'Todo...'

@app.route('/json-example')
def json_example():
    return 'Todo...'

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000