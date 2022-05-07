#Wtite a program to calculate Total and percentage

roll_no=int(input("Roll no:"))
Name=input("Name:")
Maths=int(input("Maths:"))
Science=int(input("science:"))
Hindi=int(input("Hindi:"))
English=int(input("English:"))
AI=int(input("AI:"))
Total=Maths+Science+Hindi+English
Percentage=Total/5
print("Total marks scored=",Total)
print("Total percentage scored=",Percentage)