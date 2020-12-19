import string, random

while True:
    passwordLength = input("how long do you want your password to be ")

    if passwordLength.isnumeric() == True:
        passwordLength = int(passwordLength)
        break
    else:
        print("thi is a string")

for j in range(10):
    password = ""
    for i in range(passwordLength):

        password += random.choice(string.ascii_letters+string.digits+string.punctuation)

    print(password)
    