import pytest
import json

@pytest.mark.parametrize('accoutingType, establishedYear, name', [
    ('myob',  '2020', 'test1'),
    ('myob',  '2023', 'test1'),
    ('xero',  '2023', 'test1'),
])
def test_balance_sheet(client, accoutingType, establishedYear, name):
    user_input = {'type': accoutingType, 'establishedYear':establishedYear, 'name': name}
    
    response = client.post('/api/v1/balance_sheet', json=user_input)
    data = json.loads(response.data.decode('utf-8'))
    assert 'sheet' in data
    json_data = json.loads(json.dumps(data))
    assert type(json_data['sheet']) is list

def test_unexist_provider(client):
    user_input = {'type': 'unknown', 'establishedYear':2020, 'name': 'test'}
    response = client.post('/api/v1/balance_sheet', json=user_input)
    data = json.loads(response.data.decode('utf-8'))
    assert 'sheet' in data
    json_data = json.loads(json.dumps(data))
    assert type(json_data['sheet']) is list
