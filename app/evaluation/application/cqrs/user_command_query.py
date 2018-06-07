class FindUserQuery:
    def __init__(self, id):
        self.id = id


class CreateUserCommand:
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name


class UpdateUserCommand:
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name
