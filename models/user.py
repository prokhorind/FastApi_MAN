class User:
    def __init__(self, user_id, name, surname, age):
        self.id = user_id
        self.name = name
        self.surname = surname
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get("id"),
            name=data.get("name"),
            surname=data.get("surname"),
            age=data.get("age")
        )
