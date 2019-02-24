# -*- coding:utf-8 -*-
from decouple import config
import requests
import json
import pandas as pd
from random import randint 
from faker import Faker

def makeCall(endpoint):
	headers = {
		'X-User':config('XUSER'),
		'x-api-key':config('HSBCAPI'),
		'X-Client':config('XCLIENT'),
		'X-Password':config('XPASS')
	}

	response = requests.get(endpoint, headers=headers)
	return response.json()

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

headers = {'x-api-key': 'hZK8U789vE2yaOvOkCtxa17vGKWeaLZ3QF2Vonfh',
            'X-client': 'ac8a5e6344674223a773e9227c654069',
            'X-User': 'TEAM13',
            'X-Password': '4A58e6Ad3dd54083b0D60Aa24091cB2d'}

def movimientos(acc_number):
	url = 'https://w799f0c9c3.execute-api.us-east-1.amazonaws.com/dev/v1/sandbox/checking-accounts/account-statement?accountNumber={}&movementsNumber=90'.format(acc_number)
	s = requests.Session()
	s.headers = headers
	resp = s.get(url)
	out = resp.json()

	out['historicalMovements']['movements'] = [x for x in out['historicalMovements']['movements'] if x['amount']]
	return out

def balance(accountNumber):
	url_balance = "https://w799f0c9c3.execute-api.us-east-1.amazonaws.com/dev/v1/sandbox/checking-accounts/balance"
	params = {'accountNumber': accountNumber}
	resp = requests.get(url_balance, params=params, headers=headers)
	out = resp.json()['accountBalance']['available']
	return out

	
dicc_gastos = {'Ropa y calzado': (500, 2000),
			'Entretenimiento': (50, 300),
			'Restaurantes': (70, 500),
			'Taxis': (40, 200),
			'Retiro de efectivo': (100, 500),
			'Supermercado': (200, 1000),
			'Gasolina': (200, 700),
			'Farmacia': (50, 200),
			'Electricidad': (100, 300),
			'Telefonia': (100, 500),
			'Otros gastos': (500, 1500)}
categorias_gastos = list(dicc_gastos.keys())

categorias_movimientos = categorias_gastos + ['Pago de renta', 'Pago tarjeta de credito', 'ABONO POR TRANSF CAJERO AUT TELECOMM']

#cuenta = 4085432078 #4085432086
def score_financiero(cuenta):
	fake = Faker()
	fake.seed_instance(1)
	m = movimientos(cuenta)
	balance_cuenta = balance(cuenta)
	df = pd.DataFrame(m['historicalMovements']['movements'])\
		.query('description==@categorias_movimientos')
	df['gastos'] = df['amount']*df['transactionType'].map({'C': 0, 'D': 1})
	df['ingresos'] = df['amount']*df['transactionType'].map({'C': 1, 'D': 0})
	df['movimiento'] = -1*df['gastos'] + df['ingresos']
	start_date = pd.datetime(year=2018, month=11, day=2)
	end_date = pd.datetime(year=2019, month=1, day=31)
	df['fake_date'] = df['description'].apply(lambda x: fake.date_between(start_date=start_date, end_date=end_date))
	df['fake_date'] = pd.to_datetime(df['fake_date'])
	# Primer depósito tiene la fecha más antigual
	df.loc[df['description']=="DEPOSITO POR CUENTA NUEVA", 'fake_date'] = start_date-pd.Timedelta(days=1)
	df['year'] = df.fake_date.dt.year
	df['mes'] = df.fake_date.dt.month
	df.sort_values('fake_date', inplace=True)
	df['saldo'] = df['movimiento'].cumsum()

	# Ingresos
	agrupado = df.groupby(['year','mes', 'transactionType']).sum()[['amount', 'gastos', 'ingresos']]
	# ahorros
	df_ahorros = agrupado.loc[(slice(None), slice(None), ['C']), 'ingresos'].reset_index()\
									[['year', 'mes', 'ingresos']].set_index(['year', 'mes'])\
									.join(
								agrupado.loc[(slice(None), slice(None), ['D']), 'gastos'].reset_index()\
									[['year', 'mes', 'gastos']].set_index(['year', 'mes']))\
			.eval('ahorro=ingresos-gastos', inplace=False)\
			.eval('tasa_ahorro=(ahorro/ingresos)*100', inplace=False).clip_lower(0)

	datos_indice = dict()
	# ingresos mensuals
	datos_indice['ingresos_mensuales'] = agrupado.loc[(slice(None), slice(None), ['C']), 'ingresos'].reset_index()\
		[['year', 'mes', 'ingresos']].to_dict(orient='records')
	datos_indice['ingresos_promedio'] = agrupado.loc[(slice(None), slice(None), ['C']), 'ingresos'].reset_index()\
		['ingresos'].mean()
	# gastos
	datos_indice['gastos_mensuales'] = agrupado.loc[(slice(None), slice(None), ['D']), 'gastos'].reset_index()\
		[['year', 'mes', 'gastos']].to_dict(orient='records')
	datos_indice['gastos_promedio'] = agrupado.loc[(slice(None), slice(None), ['D']), 'gastos'].reset_index()\
		['gastos'].mean()
	datos_indice['gasto_renta'] = df.loc[df['description']=="Pago de renta", 'amount'].mean()
	datos_indice['gasto_deuda'] = df.loc[df['description']=="Pago tarjeta de credito", 'amount'].mean()
	# Saldos a fin de mes
	max_fecha = df.groupby(['year', 'mes'])['fake_date'].max().tolist()
	datos_indice['balance_fin_mes'] = df.query('fake_date==@max_fecha')[['year', 'mes', 'saldo']].to_dict(orient='record')
	# Balance actual de la cuenta
	datos_indice['balance_actual'] = balance_cuenta
	# Ahorro mensual
	datos_indice['ahorro_mensual'] = df_ahorros.reset_index()[['year', 'mes', 'ahorro']].to_dict(orient='records')
	# Libertad financiera
	datos_indice['salud_fin'] = {'libertad': df.query('fake_date==@max_fecha')\
													.assign(libertad_fin=lambda x: (30*x['saldo']/datos_indice['gastos_promedio']).clip_lower(0))\
													[['year', 'mes', 'libertad_fin']].to_dict(orient='records'),
								'ahorro': df_ahorros.reset_index()[['year', 'mes', 'tasa_ahorro']].to_dict(orient='records'),
								'vivienda': agrupado.loc[(slice(None), slice(None), ['C']), 'ingresos'].reset_index()\
													.assign(esfuerzo_viv=lambda x: (100 * datos_indice['gasto_renta']/x['ingresos']).clip_upper(50))\
													[['year', 'mes', 'esfuerzo_viv']]\
													.to_dict(orient='records'),
								 'deuda': agrupado.loc[(slice(None), slice(None), ['C']), 'ingresos'].reset_index()\
													.assign(esfuerzo_deuda=lambda x: (100 * datos_indice['gasto_deuda']/x['ingresos']).clip_upper(50))\
													[['year', 'mes', 'esfuerzo_deuda']]\
													.to_dict(orient='records'),
								}

	datos_indice['score'] = {'ahorro': pd.DataFrame(datos_indice['salud_fin']['ahorro'])\
										.assign(score_ahorro=lambda x: 25*(1-((x['tasa_ahorro'].clip(0, 20)-20)/x['tasa_ahorro'].clip(0, 20)))
												.replace(pd.np.inf, 0))\
										[['mes', 'year', 'score_ahorro']].to_dict(orient='records'),
							 'libertad': pd.DataFrame(datos_indice['salud_fin']['libertad'])\
												.assign(score_libertad_fin=lambda x: 25*(1-((180-x['libertad_fin'].clip(0, 180))/180))
																						.replace(pd.np.inf, 0))\
												[['mes', 'year', 'score_libertad_fin']].to_dict(orient='records'),
							 'vivienda': pd.DataFrame(datos_indice['salud_fin']['vivienda'])\
											.assign(score_esfuerzo_viv=lambda x: 25*(((35-x['esfuerzo_viv'].clip(0, 35))/35))
																					.replace(pd.np.inf, 0))\
											[['mes', 'year', 'score_esfuerzo_viv']].to_dict(orient='records'),
							  'deuda': pd.DataFrame(datos_indice['salud_fin']['deuda'])\
											.assign(score_esfuerzo_deuda=lambda x: 25*(((35-x['esfuerzo_deuda'].clip(0, 35))/35))
																					.replace(pd.np.inf, 0))\
											[['mes', 'year', 'score_esfuerzo_deuda']].to_dict(orient='records')}
	datos_indice['score']['total']= pd.DataFrame(datos_indice['score']['ahorro'])\
										.set_index(['mes', 'year'])\
										.join(
											pd.DataFrame(datos_indice['score']['libertad'])\
											.set_index(['mes', 'year'])
										)\
										.join(
											pd.DataFrame(datos_indice['score']['vivienda'])\
											.set_index(['mes', 'year'])
										)\
										.join(
											pd.DataFrame(datos_indice['score']['deuda'])\
											.set_index(['mes', 'year'])
										)\
										.assign(score_total=lambda x:x.sum(axis=1))\
										.reset_index()\
										.assign(score_total=lambda x: x['score_total'].clip(0, 100))\
										[['mes', 'year', 'score_total']].to_dict(orient='records')
	#print(datos_indice)
	return datos_indice
