import requests
from flask import request, jsonify
from . import api

# mock this data which the last year is loss
def get_from_xero(data):
    url = 'https://6572a38dd61ba6fcc015491a.mockapi.io/type/xero'
    res = requests.get(url, json=data)
    # get the first item as returned mockup data is an array
    return res.json()[0]


def get_from_myob(data):
    url = 'https://6572a38dd61ba6fcc015491a.mockapi.io/type/myob'
    data['year'] = data['establishedYear']
    res = requests.get(url, json=data)
    return res.json()[0]

@api.route('/balance_sheet', methods=['POST'])
def get_balance_sheet():
    data = request.get_json()
    match data['type']:
        case 'Xero':
            res = get_from_xero(data)
        case 'MYOB':
            res = get_from_myob(data)
        case _:
            res = {'sheet': []}
    return jsonify(res)