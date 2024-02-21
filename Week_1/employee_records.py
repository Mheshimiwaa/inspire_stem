#This is a program to show income of an employee
#Date: 21/02/2024
#Name: Michael Macharia
 

f_name=input("enter first name: ")
s_name=input("enter second name: ")
age=input("enter age: ")

sal=int(input("enter salary: "))
sal_increase=int(input("enter increment"))
percentage=(sal_increase / 100)
sal_increased=(sal * percentage + sal)
print("salary increased",sal_increased)


bonus=int(input("enter bonus "))
bonus_decreased=int(input("enter bonus decreased"))
bonus_remained=(bonus - bonus_decreased)
print("solution of bonus that remained", bonus_remained)

total_income=(sal_increased + bonus_remained)
print("total income after adjustments", total_income)
















