n=int(input("Enter number of days="))
year=int(n/365)
a=int(n%365)
week=int(a/7)
days=int(a%7)
print("Years=",year)
print("Weeks=",week)
print("Days=",days)
