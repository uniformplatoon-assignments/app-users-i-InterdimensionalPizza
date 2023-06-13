class Users:
    def __init__(self, name, email_address, drivers_license_num ):
        self.name = name
        self.email_address = email_address
        self.drivers_license_num = drivers_license_num
    
    def __str__(self):
        return f'{self.name} {self.email_address} {self.drivers_license_num}'
    
Greg = Users('Greg', 'greg@codeplatoon.org', '123456789')
Matt = Users('Matt', 'matt@hotmail.com', '1234567')

print(Greg)
print(Matt)
