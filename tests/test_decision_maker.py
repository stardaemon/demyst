import pytest
import json

def test_loan_greater_than_assets_and_summary_loss(client):
    user_input = {
        'name':'test1',
        'establishedYear':'2023',
        'loanAmount': 654218999,
        'sheet':[
            {
                'year':2023,
                'month':12,
                'profitOrLoss':-250000,
                'assetsValue':1234
            },
            {
                'year':2023,
                'month':11,
                'profitOrLoss':-1150,
                'assetsValue':5789
            },
            {
                'year':2023,
                'month':10,
                'profitOrLoss':-2500,
                'assetsValue':22345
            },
            {
                'year':2023,
                'month':9,
                'profitOrLoss':187000,
                'assetsValue': 223452
            }
        ]
    }
    response = client.post('/api/v1/decision_maker', json=user_input)
    data = json.loads(response.data.decode('utf-8'))
    assert data['approvalStatus'] == 'unapproved'
    
    
def test_loan_less_than_assets(client):
    user_input =  {
        'name':'test1',
        'establishedYear':'2023',
        'loanAmount': 3567,
        'sheet':[
            {
                'year':2023,
                'month':12,
                'profitOrLoss':-250000,
                'assetsValue':1234
            },
            {
                'year':2023,
                'month':11,
                'profitOrLoss':-1150,
                'assetsValue':5789
            },
            {
                'year':2023,
                'month':10,
                'profitOrLoss':-2500,
                'assetsValue':22345
            },
            {
                'year':2023,
                'month':9,
                'profitOrLoss':187000,
                'assetsValue': 223452
            }
        ]
    }
    response = client.post('/api/v1/decision_maker', json=user_input)
    data = json.loads(response.data.decode('utf-8'))
    assert data['approvalStatus'] == 'approved'
    assert data['loanAmountApproved'] == 3567

def test_loan_greater_than_assets_and_summary_profit(client):
    user_input =  {
        'name':'test1',
        'establishedYear':'2023',
        'loanAmount': 10000000,
        'sheet':[
            {
                'year':2023,
                'month':12,
                'profitOrLoss':250000,
                'assetsValue':1234
            },
            {
                'year':2023,
                'month':11,
                'profitOrLoss':1150,
                'assetsValue':5789
            },
            {
                'year':2023,
                'month':10,
                'profitOrLoss':-2500,
                'assetsValue':22345
            },
            {
                'year':2023,
                'month':9,
                'profitOrLoss':187000,
                'assetsValue': 223452
            }
        ]
    }
    response = client.post('/api/v1/decision_maker', json=user_input)
    data = json.loads(response.data.decode('utf-8'))
    assert data['approvalStatus'] == 'approved'
    assert data['loanAmountApproved'] == 6000000
 