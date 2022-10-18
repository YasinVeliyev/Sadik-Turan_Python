class Class:
    def __init__(self, id: int, name: str, techer_id: int):
        self.name = name
        self.teacher_id = techer_id
        self.id = id

    @classmethod
    def create_class(cls, classes):
        return [Class(*class_) for class_ in classes]
