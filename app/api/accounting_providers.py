from flask import jsonify
from . import api

@api.route('/accounting_providers', methods=['GET'])
def get_accounting_providers():
    accounting_providers = ['Xero', 'MYOB']
    return jsonify({'accountingProviders': accounting_providers})