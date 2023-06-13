# your User class goes here

class User:
    def __init__(self,name, email, drivers_liscence):
        self.Name=name
        self.Email=email
        self.Drivers_liscence=drivers_liscence
        

def createUsers():
    user_instances=[]
    users=[
        {"name":"John", "email":"john@email.com", "drivers_liscence":"FDUI87"},
        {"name":"Mike", "email":"mike@email.com", "drivers_liscence":"FDUI87"},
        {"name":"Zack", "email":"zack@email.com", "drivers_liscence":"FDUI87"}
    ]
    for user in users:
        user_instances.append(User(**user))
    for i in user_instances:
        print(i.Name, i.Email)

createUsers()
        