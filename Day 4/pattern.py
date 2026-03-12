#pattern for printing stars
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''
'''
#pattern for printing stars in def
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
n=int(input("Enter the number of rows: "))
pattern(n)
'''
#print the pattern of numbers
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
'''
#pattern for printing numbers in def
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
n=int(input("Enter the number of rows: "))
pattern(n)
'''
'''
#print the pattern of numbers in reverse order
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
 #pattern for printing numbers in reverse order in def
def pattern(n):
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print(j,end="")
        print()
n=int(input("Enter the number of rows: "))
pattern(n)
'''
'''
#print the pattern of numbers in upside down
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

def pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()
n=int(input("Enter the number of rows: "))
pattern(n)
'''
