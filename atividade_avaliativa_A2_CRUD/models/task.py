class Aluno:
    def __init__(self, id_aluno, nome, email, senha, completed=False) -> None:
        self.id_aluno = id_aluno
        self.nome = nome
        self.email = email
        self.completed = completed
        self.senha = senha
    def to_dict(self):
        return {
            "id_Aluno": self.id_aluno,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "completed": self.completed
        } 