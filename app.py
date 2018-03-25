#app.py

from flask import Flask, request

app = Flask(__name__) #create the Flask app

# Authenticate a credit card and get user access to his account in the ATM client.
@app.route('/authenticate-card', methods=['POST'])
def authenticate_card():
    card_id = request.args.get('card_id')

    return '''<h1>The card id is: {}</h1>'''.format(card_id)

# Check the credit card's validity, balance ,and process the payment.
@app.route('/process-payment', methods=['POST'])
def process_payment():
    return 'Todo...'

@app.route('/json-example')
def json_example():
    return 'Todo...'

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000