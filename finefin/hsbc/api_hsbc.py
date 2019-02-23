from decouple import config
import requests
<<<<<<< HEAD
import json
=======
>>>>>>> 655085a2a9c26bba4ef789eafbb49a9b722f9d3f

def makeCall(endpoint):
	headers = {
		'X-User':config('XUSER'),
		'x-api-key':config('HSBCAPI'),
		'X-Client':config('XCLIENT'),
		'X-Password':config('XPASS')
	}

	response = requests.get(endpoint, headers=headers)
	return response.json()

<<<<<<< HEAD
def makePost(endpoint, data):
	headers = {
		'X-User':config('XUSER'),
		'x-api-key':config('HSBCAPI'),
		'X-Client':config('XCLIENT'),
		'X-Password':config('XPASS'),
		'content-type':'application/json'
	}

	response = requests.post(endpoint, headers=headers, data=data)
	print(response.status_code, response.reason)
	return response.json()

=======
>>>>>>> 655085a2a9c26bba4ef789eafbb49a9b722f9d3f
def clientProfile(client_number):
	endpoint = '{}clients/{}/profile'.format(config('HSBCURL'),client_number)
	response = makeCall(endpoint)
	client = None
	if 'responseCodes' in response:
		client = response['clientProfile']
	return client

def accountProfile(account_number):
	endpoint='{0}checking-accounts/profile?accountNumber={1}'.format(config('HSBCURL'),account_number)
	response = makeCall(endpoint)
	account = None
	if 'responseCodes' in response:
		account = response['accountProfile']
	return account

def accountBalance(account_number):
	endpoint='{0}checking-accounts/balance?accountNumber={1}'.format(config('HSBCURL'),account_number)
	response = makeCall(endpoint)
	balance = None
	if 'responseCodes' in response:
		balance = response['accountBalance']
	return balance

def accountStatement(account_number, movements_number):
	endpoint='{0}checking-accounts/account-statement?accountNumber={1}&movementsNumber={2}'.format(config('HSBCURL'),account_number,movements_number)
	response = makeCall(endpoint)
	historical = None
	if 'responseCodes' in response:
		historical = response['historicalMovements']
	return historical

<<<<<<< HEAD
def accountTransfer(source, destination, amount, description):


	data = json.dumps({
	  "transaction": {
	    "sourceAccount":str(source),
	    "destinationAccount": str(destination),
	    "transactionAmount": '{}'.format(amount),
	    "description": str(description)
	  }
	})
	endpoint = '{}checking-accounts/transfer'.format(config('HSBCURL'))
	response = makePost(endpoint, data)
	return response

print(accountTransfer(4085432003,4085432052,66.61,'Taxi'))
=======
print(clientProfile(9001365))
print(accountProfile(4085432003))
print(accountBalance(4085432003))
print(accountStatement(4085432003,15))
>>>>>>> 655085a2a9c26bba4ef789eafbb49a9b722f9d3f
