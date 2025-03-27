# models/country.py

class Country:
    def __init__(self, name, code):
        super().__init__()
        self.id = code  # Use code as the ID for simplicity
        self.name = name
        self.code = code

    def to_dict(self):
        return {"id": self.id, "name": self.name, "code": self.code}
