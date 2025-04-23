class Aluno:
    def __init__(self, matricula, nome, email, senha, completed=False) -> None:
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.completed = completed
        self.senha = senha
    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "completed": self.completed
        }
