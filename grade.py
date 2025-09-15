math = int(input("enter the marks of math"))
english = int(input("enter the marks of english"))
science = int(input("enter the marks of science"))
sum = math + english + science
avg = sum/3
print("you got",avg, "%")
if avg > 90:
    print("You have got A grade")
elif avg > 80:
    print("you have got B grade")
else:
    print("you have got c grade")