#This is a programme to show arithmetic and geometric progressions
#Name: Michael Macharia
#Date: 20/02/2024

#arithmetic progressions

a1=int(input("enter first term: "))
d1=int(inpt("enter common difference: "))
n=int(input("enter number of terms: "))
nth=(a1 + (n - 1)*d1)
print("solution of nth term",nth)

#geometric progressions

a2=int(input("enter first term of geometric: "))
r=int(input("enter common ratio: "))
nr=int(input("enter number of terms: "))
nthr=(a2 * r **(n-1))
print("solution of the nth term",nthr)
