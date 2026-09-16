# 🐍 Programador Ruim

## 📚 Sistema de Gerenciamento Escolar

Projeto desenvolvido a partir de um **Sistema de Gerenciamento Escolar originalmente escrito em JavaScript**.

O objetivo da atividade é **reformular o código para Python**, corrigindo os problemas existentes na implementação original e aplicando conceitos de **Programação Orientada a Objetos (POO)**.

## 🎯 Objetivo

A aplicação permite gerenciar informações básicas de uma escola através de um sistema executado pelo terminal.

O sistema possibilita:

* 👨‍🎓 Adicionar alunos;
* 👨‍🏫 Adicionar professores;
* 📚 Adicionar disciplinas;
* 📋 Exibir alunos cadastrados;
* 📋 Exibir professores cadastrados;
* 📋 Exibir disciplinas cadastradas;
* 🚪 Encerrar o sistema.

## 🧩 Estrutura do projeto

O projeto é dividido em dois arquivos Python:

```text
programador-ruim/
│
├── programador_ruim.py
├── programa_programador_ruim.py
└── README.md
```

### `programa_programador_ruim.py`

Contém as classes responsáveis pela estrutura do sistema:

* `Pessoa`
* `Aluno`
* `Professor`
* `Disciplina`
* `Escola`

### `programador_ruim.py`

Contém o **menu principal** e a interação com o usuário através do terminal.

## 🏗️ Conceitos de POO utilizados

### `Pessoa`

Classe base que armazena informações comuns:

* Nome
* Idade
* CPF

### `Aluno`

Herda da classe `Pessoa` e adiciona informações específicas do aluno:

* Matrícula
* Disciplinas

### `Professor`

Herda da classe `Pessoa` e adiciona:

* Salário

### `Disciplina`

Armazena:

* Nome
* Código
* Professor responsável
* Alunos matriculados

### `Escola`

Responsável por administrar:

* Alunos
* Professores
* Disciplinas

## 🔄 Funcionamento

Ao executar o programa, é apresentado um menu no terminal:

```text
--- Sistema de Gerenciamento Escolar ---

0. Sair
1. Adicionar aluno
2. Adicionar professor
3. Adicionar disciplina
4. Exibir alunos
5. Exibir professores
6. Exibir disciplinas
```

O usuário escolhe uma opção e o sistema executa a operação correspondente.

Para cadastrar uma disciplina, é necessário que exista pelo menos um professor cadastrado. O sistema apresenta os professores disponíveis para que o usuário escolha o responsável pela disciplina.

## 🛠️ Tecnologias utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Terminal/Console

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/SkYantS28/programador-ruim.git
```

Entre na pasta:

```bash
cd programador-ruim
```

Execute o programa:

```bash
python programador_ruim.py
```

## 📌 Objetivo acadêmico

Este projeto foi desenvolvido como atividade acadêmica para praticar **Programação Orientada a Objetos em Python**, trabalhando conceitos como:

* Classes e objetos;
* Herança;
* Construtores;
* Métodos;
* Encapsulamento de dados;
* Relacionamento entre classes;
* Listas de objetos;
* Entrada e saída de dados;
* Estruturas condicionais e de repetição.

## 👩‍💻 Desenvolvido por

**Sky Crizosti**

Estudante de Engenharia de Software.
