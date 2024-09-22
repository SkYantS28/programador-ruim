from programa_programador_ruim import Pessoa
from programa_programador_ruim import Aluno
from programa_programador_ruim import Professor
from programa_programador_ruim import Disciplina
from programa_programador_ruim import Escola

rep = 0
pessoa = Pessoa()
escola = Escola()

while rep >= 0:
    print("--- Sistema de Gerenciamento Escolar ---")
    desejo = input("\n Escolha uma opção: \n \n 0. Sair \n 1. Adicionar aluno \n 2. Adicionar professor \n 3. Adicionar disciplina \n 4. Exibir alunos \n 5. Exibir professores \n 6. Exibir disciplinas \n ")

    if desejo == '0': #encerrar
        print("Saindo do Sistema...")
        break

    elif desejo == '1': #adicionar aluno
        novo_aluno = Aluno().criarAluno()
        escola.adicionar_aluno(novo_aluno)

    elif desejo == '2': #adicionar professor
        novo_professor = Professor().criarProfessor()
        escola.adicionar_professor(novo_professor)

    elif desejo == '3': #adicionar disciplina
        nova_disciplina = Disciplina().criarDisciplina(escola.professores)
        if nova_disciplina:
            escola.adicionar_disciplina(nova_disciplina)
    
    elif desejo == '4': #exibir alunos
        escola.exibir_dados_alunos()

    elif desejo == '5': #exibir professores
        escola.exibir_dados_professores()

    elif desejo == '6': #exibir disciplinas
        escola.exibir_dados_disciplinas()

    else: #erro
        print("Opção inválida! Tente novamente.")