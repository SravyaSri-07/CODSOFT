#Password Generator
import random
import string
print("---PASSWORD GENERATOR---")
def code():
    l=int(input("Please enter the number of letters you would like in your password:"))
    d=int(input("Please enter the number of digits you would like in your password:"))
    p=int(input("Please enter the number of punctuations you would like in your password:"))
    letters=random.choices(string.ascii_letters,k=l)
    digits=random.choices(string.digits,k=d)
    punctuations=random.choices(string.punctuation,k=p)
    password=letters+digits+punctuations
    random.shuffle(password)
    print("DESIRED PASSWORD:","".join(password))
code()
while True:
    choice=input(("Need another strong Password?(yes/no):"))
    if choice=='yes':
        code()
    else:
        print("THANK YOU :)")
        break
