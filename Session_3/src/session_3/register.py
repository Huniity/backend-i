class UserRegistration:
    def __init__(self):
        self.user_database = []

    def register_user(self, name,*args, **kwargs):
        user = {"Name": name}
        if args:
            if "@" in args[0]:  
                user["Email"] = args[0]  
                user["Category"] = args[1] if len(args) > 1 else None  
            else:  
                user["Email"] = None
                user["Category"] = args[0]
        user.update(kwargs)
        self.user_database.append(user)
        print(f"\n\n**********************  Registration for {name}  **********************\n")
        print(f"{name} | Created with success | Email: {user.get("Email")}. | Category: {user.get("Category")}")
        for key, value in kwargs.items():
            print(f"{key} - {value}", end=" | ")


    def update_user(self, name, new_email, new_category, **kwargs):
        for user in self.user_database:
            if user.get("Name") == name:
                user["Email"] = new_email
                user["Category"] = new_category
                user.update(kwargs)
                print(f"\n\n**********************  {name} Profile Update  **********************\n")
                print(f"{name} | Updated with success | Email: {user.get("Email")}. | Category: {user.get("Category")}")
                for key, value in kwargs.items():
                    print(f"{key} - {value}", end=" | ")

            else:
                print("Not found.")

    def remove_user(self, name):
        for user in self.user_database:
            if user.get("Name") == name:
                self.user_database.remove(user)
                print(f"\n\n**********************  Deleting {name} Profile  **********************\n")
                print("Deleted with success.")
                print(self.user_database)
            else:
                print("Not found.")
        

new_register = UserRegistration()
new_register.register_user("Adrien", "adrien.dejonc@gmail.com", "Student", Age=31, Nationality="fr", Gender="male")
new_register.register_user("Huniity", "huniity@gmail.com", "Gamer", Age=157, Nationality="en", Gender="goblin")
new_register.update_user("Adrien", "adrien_dejonc@eticalgarve.com", "Mentor", Age=32, Nationality="fr", Gender="male")
new_register.remove_user("Adrien")
