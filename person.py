class Student:
    def __init__(self, name, last_name, email) -> None:
        self.name = name
        self.last_name = last_name
        self.email = email

    def info(self):
        return f"{self.name}, {self.last_name}, {self.email}"
