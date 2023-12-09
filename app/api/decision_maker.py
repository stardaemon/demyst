from flask import request, jsonify
from . import api

# calculate summary based on attribute
def cal_summary(data, attribute):
    res = 0
    # get data of at most one year
    months = min(len(data), 12)
    for month in range(months):
        res += data[month][attribute]
    return [res, months]

def cal_avg_asset(data):
    [total_assets_value, months] = cal_summary(data, 'assetsValue')
    if months > 0:
        return total_assets_value/months
    return 0

# mockup decision maker response 
def get_decision_maker_res(data):
    if int(data['preAssessment']) == 100:
        return {
            'approvalStatus': 'approved', 
            'loanAmountApproved': data['loanAmount']
        }
    elif int(data['preAssessment']) >= 60:
        return {
            'approvalStatus': 'approved', 
            'loanAmountApproved': data['loanAmount'] * 0.6
        }
    else:
        return {
            'approvalStatus': 'unapproved', 
            'loanAmountApproved': 0
        }

@api.route('/decision_maker', methods=['POST'])
def get_decision():
    data = request.get_json()
    avg_assets_value = cal_avg_asset(data['sheet'])
    [summary_profit, months] = cal_summary(data['sheet'], 'profitOrLoss')
    pre_assessment = '20'
    if avg_assets_value > int(data['loanAmount']):
        pre_assessment = '100'
    elif summary_profit > 0:
        pre_assessment = '60'
        
    res = get_decision_maker_res({
        'name': data['name'],
        'establishedYear': data['establishedYear'],
        'summaryProfit': summary_profit,
        'loanAmount': data['loanAmount'],
        'preAssessment': pre_assessment
    })    
    return res
        