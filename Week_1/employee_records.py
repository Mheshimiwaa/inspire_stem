#This is a program to show income of an employee
#Date: 21/02/2024
#Name: Michael Macharia
 
#Employee details
f_name=input("enter first name: ")
s_name=input("enter second name: ")
age=input("enter age: ")

#Employee salary and adjustments
sal=int(input("enter salary: "))
sal_increase=int(input("enter increment"))
percentage=(sal_increase / 100)
sal_increased=(sal * percentage + sal)
print("salary increased",sal_increased)

#Employee bonuses and adjustments
bonus=int(input("enter bonus "))
bonus_decreased=int(input("enter bonus decreased"))
bonus_remained=(bonus - bonus_decreased)
print("solution of bonus that remained", bonus_remained)

#Total income after adjustments
total_income=(sal_increased + bonus_remained)
print("total income after adjustments", total_income)

salary=int(input("enter salary :"))
if salary >100000 :
 salary =salary * 0.3 + salary
 print(salary)
 print("\t")

if salary >150000:
 salary =salary * 0.05 + salary
 print(salary)
 print("\t")
 
 if salary >100000 and salary <150000:
  salary =salary * 0.15 + salary
  print(salary)
  
















