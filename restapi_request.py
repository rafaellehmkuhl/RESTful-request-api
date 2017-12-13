import requests

api_url = 'http://api.promasters.net.br/cotacao/v1/valores'

payload = {
    # 'moedas': 'USD',
    'alt': 'json'
}

response = requests.get(api_url, params=payload)

if response.ok:
    JSON = response.json()

else:
    print('Server offline')

for key in JSON['valores']:
    print('Valor de {} em Real: R${}.'.format(JSON['valores'][key]['nome'], JSON['valores'][key]['valor']))
