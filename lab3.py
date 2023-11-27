sales_goals =float(input("Sales goal:"))
total=0
weeks = 1
salesman1 = 1
for i in range(4):
    print("Salesperson "+str(salesman1)+" week " + str(weeks))
    temp=float(input())
    total+= temp
    weeks+=1

salesman= input("Another salesperson?")
while salesman =="y":
    salesman1 +=1
    weeks =1
    for i in range(4):
        print("Salesperson "+str(salesman1)+" week "  + str(weeks))
        temp = float(input())
        total += temp
        weeks += 1
    salesman= input("Another salesperson?")

if total>sales_goals:
    bonus=total*.05
else:
    bonus=total*.02

print("Number of Employees",salesman1)
print("Department Sales Goal",sales_goals)
print("Total Sales",total)
print("Mgr. Bonus",bonus)
