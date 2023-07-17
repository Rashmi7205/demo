print('Start')
try:
    no1 = int(input('Enter no1 value')) 
    no2 = int(input('Enter no2 value'))
    print("add = ",no1+no2)
    print("Division",no1//no2)
except ValueError:
    print('Exception is getting & handled it')
    print('Enter int type')
except ZeroDivisionError:
    print('Enter any non zero value for 2nd input')    
finally:
    print('Stop')