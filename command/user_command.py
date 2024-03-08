class UserCommand():
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password

    @classmethod
    def create_from_json(cls, json_data):
        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        email = json_data.get('email')
        password = json_data.get('password')
        return cls(first_name, last_name, email, password)