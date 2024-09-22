class Pessoa:
    def __init__(self, nome="", idade=0, cpf=0):
        self.nome = str(nome)
        self.idade = int(idade)
        self.cpf = int(cpf)

    def exibir_dados_pessoas(self):
        print(f"\n Nome: {self.nome} \n Idade: {self.idade} \n CPF: {self.cpf}")

class Aluno(Pessoa):
    def __init__(self, nome="", idade=0, cpf=0, matricula=0, disciplinas=""):
        super().__init__(nome, idade, cpf)
        self.matricula = int(matricula)
        self.disciplinas = str(disciplinas)

    def exibir_dados_alunos(self):
        print(f"\n Nome: {self.nome} \n Idade: {self.idade} \n CPF: {self.cpf} \n Matricula: {self.matricula} \n Disciplinas: {self.disciplinas}")

    def criarAluno(self):
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        cpf = input("Digite o cpf do aluno: ")
        matricula = input("Digite a matricula do aluno: ")

        return Aluno(nome, idade, cpf, matricula)

class Professor(Pessoa):
    def __init__(self, nome="", idade=0, cpf=0, salario=0):
        super().__init__(nome, idade, cpf)
        self.salario = float(salario)

    def exibir_dados_professores(self):
        print(f"\n Nome: {self.nome} \n Idade: {self.idade} \n CPF: {self.cpf} \n Salario: {self.salario}")
        
    def criarProfessor(self):
        nome = input("Digite o nome do professor: ")
        idade = int(input("Digite a idade do professor: "))
        cpf = input("Digite o cpf do professor: ")
        salario = input("Digite o salario do professor: ")

        return Professor(nome, idade, cpf, salario)

class Disciplina:
    def __init__(self, nome="", codigo=0, professor=None):
        self.nome = str(nome)
        self.codigo = int(codigo)
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def criarDisciplina(self, professores):
        nome = input("Digite o nome da disciplina: ")
        codigo = int(input("Digite o codigo da disciplina: "))

        if len(professores) > 0:
            print("Esses são os professores disponíveis:")
            for i, professor in enumerate(professores):
                print(f"Índice {i+1} - {professor.nome}")

            opcao = int(input("Escolha o professor pelo índice: ")) - 1

            if 0 <= opcao < len(professores):
                professor_escolhido = professores[opcao]
                return Disciplina(nome, codigo, professor_escolhido)
            else:
                print("Índice inválido! Tente novamente.")
        else:
            print("Nenhum professor cadastrado")

    def exibir_dados_disciplinas(self):
        print(f"\n Nome: {self.nome} \n Código: {self.codigo} \n Professor: {self.professor.nome}")


class Escola:
    def __init__(self, nome=""):
        self.nome = str(nome)
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_dados_alunos(self):
        for aluno in self.alunos:
            aluno.exibir_dados_alunos()

    def exibir_dados_professores(self):
        for professor in self.professores:
            professor.exibir_dados_professores()

    def exibir_dados_disciplinas(self):
        for disciplina in self.disciplinas:
            disciplina.exibir_dados_disciplinas()

