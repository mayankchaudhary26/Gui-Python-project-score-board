import sqlite3
mystore=sqlite3.connect('bookstores.db')
mycursor=mystore.cursor()
total=0

while True:
    title=input("enter the title:")
    
    sql="select * from book where title='"+title+"';"
    x=mycursor.execute(sql)
    if x!=None:
        copies=int(input("enter the no. of copies"))
        mycursor.execute("select price from book where title='"+title+"';")
        price=mycursor.fetchone()
        print(price[0])
        total+=price[0]*copies
    else:
        print("searched book not found")
        
        
    inp=input("add more books y/n")
    if inp=='y':
        continue
    else:
        print("the total amt:",total)
        break

#ADDING NUMPY FILE ONE OF FIVE
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()
print(c)
print("Vectorized version: " + str(1000* (toc-tic))+ "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print(c)
print("For Loop: " + str(1000*(toc-tic))+ "ms")

