print('Start')
try:
    no1 = int(input('Enter no1 value')) 
    no2 = int(input('Enter no2 value'))
    print("add = ",no1+no2)
except ValueError:
    print('Exception is getting & handled it')
    print('Enter int type')
finally:
    print('Stop')
##try without catch
#SyntaxError: expected 'except' or 'finally' block