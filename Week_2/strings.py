#string in python
#Date:22/02/2024
#Name:Michael Macharia

city="nairobi"
print(city[0])#n
print(city[1])#a
print(city[2])#i
print(city[3])#r
print(city[4])#o
print(city[-1])#b
print(city[-2])#i
#convert to upper case

print(city)
print("\n\n") # this gives a new line
print(city.upper())

name="Michael Macharia"
print(name)
print(name.lower())#converts string to lower case

town="    Naivasha   "
print(town)
print("\t")#this will print new tab
print(town.strip())

f_name="Michael"
s_name="Macharia"
full_name=f_name+s_name
print(full_name)

#replacing a character

fruit="orangeoooo"
print(fruit.replace("o","y"))

#split
subject="physical,sciences"
print(subject.split(","))

#THE FOLLOWING IS HOW TO FORMAT
#1.{}
age=18
height=1.72
print("i am {0} years old and{1} metres tall".format(age,height))

#2a.printing a string
activity="dancing"
print("my hobby is %s"%(activity))


height=1.2326271
print("my height is %5.2f" %(height))

#3printing an integer %d
age=18
print("my age is %d" %(height))


name = "Michael Macharia"
print(len(name))
#2b
print(f"my full name is {name}")

school="Engineering"
course="Electrical"

print("I am studying {course} in the school of {school}".format(course="medicine",school="Agakhan"))