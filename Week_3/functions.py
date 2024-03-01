#a block of code running together as a unit
# definig function
def print_name():
    print("My name is Michael Macharia")
#calling the function
print_name()   
print_name()
print_name()

def print_details(name , age , gender , id):
    print("I am {0}, {1} years old ,{2}, my id number is{3}".format(name , age ,gender ,id))

print_details("Michael Macharia", "18 years" , "male" , "19802021")
print_details("miguel sancho", "34 years" , "male" , "0101010101")

print("\n")

def sum_nums(x,y):
    return x+y
z=sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return x*y
print(prod_nums(11,90))


def print_odds(first_no,last_no):
    for i in range(first_no,last_no,2):
     print(i%2)     
print_odds(1,16)     