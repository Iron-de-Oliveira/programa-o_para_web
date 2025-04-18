class Aluno:
    def __init__(self, id, nome, description, completed=False) -> None:
        self.id = id
        self.nome = nome
        self.description = description
        self.completed = completed
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "description": self.description,
            "completed": self.completed
        }
