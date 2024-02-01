def calculate_total(exp): # function defined to calculate total expenses
    total = 0
    for item in exp:
        total =total+item
    return total 

tom_exp_list = [2100,3400,3500]  # data list of expenses 
joe_exp_list = [200,500,700]

toms_total= calculate_total(tom_exp_list) # calling the funtion many number of time and attaching data to the common function
joes_total= calculate_total(joe_exp_list)

print('Toms total expenses:', toms_total) #printing funtion output 
print('joes total expenses:', joes_total)