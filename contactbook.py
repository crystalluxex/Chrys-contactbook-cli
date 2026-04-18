contactbook={}
print("What do you want to do today")
while True:
    contact=int(input("1. Add contact\n2. Search contact\n3. Delete contact\n4. Edit contact name\n5. View all contacts\n6. Exit CLI.\nPlease enter number associated with any option to choose  it.\n"))
    if contact==1:
        new_contact=input("Please input contact name\n")
        contact_num=input("Please enter contact's number\n")
        contactbook[new_contact]=contact_num
        print(f"\n{new_contact.title()} has been added to book. Anything else?")
    if contact==2:
        keywords=input("Please input the contact name\n").lower()
        if keywords in contactbook:
            print(f"Contact:{keywords.title()}\nContact's number:{contactbook[keywords]}")
            print("All done,anything else?")
        else:
            print("Sorry,contact does not exist. Please confirm contact name by viewing all contacts.")
    if contact==3:
        to_be_deleted=input("Please input name of of contact to be deleted\n")
        if to_be_deleted in contactbook:
            del contactbook[to_be_deleted]
            print("All done,anything else?")
        else:
            print("Sorry,contact does not exist. Please confirm contact name by viewing all contacts.")
    if contact==4:
        rename=input("Please input name of contact to be renamed\n")
        if rename in contactbook:
            renamed_contact=contactbook[rename]
            del contactbook[rename]
            new_name=input("Please input new name\n")
            contactbook[new_name]=renamed_contact
            print("All done. Anything else?")
        else:
            print("Sorry,contact does not exist. Please confirm contact name by viewing all contacts.")
    if contact==5:
        for key,value in contactbook.items():
            print(f"Name:{key.title()}\nContact number:{value}\n")
            if contactbook=={}:
                print("Contactbook is empty.Would you like to......")
    if contact==6:
        print("Thanks for using the Chrys ContactBook. Hope too see you soon*-*")
        break