class User:
    def __init__(self, full_name:str, username:str, password:str, email:str, is_admin:bool=False):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
        self.is_dmin = is_admin