import json

def test_get_account_providers(client):
    response = client.get('/api/v1/accounting_providers')
    data = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert 'accountingProviders' in data
    assert type(data['accountingProviders']) is list
