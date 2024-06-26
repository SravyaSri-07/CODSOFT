#CONTACT BOOK
#creating empty dictionary
print("--WELCOME--")
print("HERE'S YOUR CONTACT BOOK")
contact={}
while True:
    print("""You can 
 1.Add a contact
 2.Delete a contact
 3.Search a contact
 4.print contact list
 5.Exit""")
    n=int(input("Enter respective number:"))
    if n==1:
        name=input("Enter name:")
        phone=int(input("Enter mobile no:"))
        email=input("Enter email:")
        adress=input("Enter address:")
        contact[name]={}
        contact[name]['phoneno']=[phone]
        contact[name]['email']=[email]
        contact[name]['adress']=[adress]
        print("---CONTACT SAVED SUCCESSFULLY----")
        for keys in contact.keys():
            print(keys,':',contact[keys])
    elif n==2:
        name=input("Enter name:")
        del contact[name]
        print("---CONTACT DELETED SUCCESSFULLY---")
    elif n==3:
        name=input("Enter name:")
        if name in contact:
            print(contact.get(name))
        else:
            print("NO CONTACT FOUND")
    elif n==4:
        for keys in contact.keys():
            print(keys,':',contact[keys])
    elif n==5:
        print("THANK YOU :)")
        break
    if len(contact)==0:
        print("NO CONTACT SAVED")
    

    
        


