"'#input the balance'"
def paying_debt_offina_year(input_bal, annual_interest_rate):
    '''
    function definition
    '''
    month_pay = 0
    bal = input_bal
    while bal > 0:
        bal = input_bal
        month_pay = month_pay+10
        month = 1
        while month <= 12:
            monthly_interest_rate = (annual_interest_rate)/12.0
            monthly_unpaid_balance = (bal)-(month_pay)
            updated_balance = (monthly_unpaid_balance) +\
            (monthly_interest_rate*monthly_unpaid_balance)
            bal = updated_balance
            month += 1
    return month_pay
def main():
    '''
    function call
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "+str(paying_debt_offina_year(data[0], data[1])))
if __name__ == "__main__":
    main()
