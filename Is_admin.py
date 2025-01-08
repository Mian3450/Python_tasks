age = int(input("Enter your age: "))
is_admin = input("Are you an administrator?: ")

if age >= 20 and is_admin == "True":
    print("Success. You are an administrator!")
elif age >= 20 and is_admin == "False":
    print("Success")
else:
    print("Denied")
