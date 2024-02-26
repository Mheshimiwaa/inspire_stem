#Programme to show salary adjustments
#Name:Michael Macharia
#Date:26/02/2024

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