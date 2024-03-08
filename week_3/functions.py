def print_name():
    print("My name is joshua")


#calling the fuction
    
print_name()
print_name()
print_name()

def print_details(name,age,Id,gender):
    print("I am {0},{1} years old .My id is {2} and gender is {3}".formart(name,age,Id,gender))


    print_details("Joshua","18","128889","male")
    print_details("mwangi","18","29987","female")

def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return(x*y)

z = prod_nums(40,20)
print(z)
def print_odds(first_no,last_number):
    for i in range(first_no,last_number):
    print(i % 2)


print_odds(0,15)


 
