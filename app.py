#app.py

from flask import Flask, request

app = Flask(__name__)

# Authenticate a credit card and get user access to his account in the ATM client.
@app.route('/authenticate-card', methods=['POST'])
def authenticate_card():
    req_data = request.get_json(force=True)
    card_id = req_data['card_id']

    return '''The card passed for reading is: {}'''.format(card_id)

# Check the credit card's validity, balance ,and process the payment.
@app.route('/process-payment', methods=['POST'])
def process_payment():
    return 'Todo...'

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000