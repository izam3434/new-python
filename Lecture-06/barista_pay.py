num_employess = 6
def main():
    hours = [0] * num_employess
    
    for index in range(num_employess):
        print('Enter the hours worked by employee ', \
              index + 1, ': ', sep='', end='')
        hours[index] = float(input())
        
    pay_rate = float(input('Enter the hourly pay rate: '))
    
    for index in range(num_employess):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ', index + 1, ': $', \
              format(gross_pay, ',.2f'), sep='')
main()