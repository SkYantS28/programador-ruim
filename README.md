# programador-ruim

O seu amigo programador desenvolveu um Sistema de Gerenciamento Escolar em Javascript.

Você foi contratado para reformular o código do seu amigo, mas na linguagem Python, mas cuidado... o seu amigo parece ter cometido alguns deslizes... boa atividade!

Código:


class Pessoa {
    constructor(nome, idade, cpf) {
        nome === nome;
        idade === idade;
        cpf === cpf;
    }

    exibirInformacoes() {
        console.log(`Nome: ${this.nome}, Idade: ${idade}, CPF: ${cpf}`);
    }
}

class Aluno extends Pessoa {
    constructor(nome, idade, cpf, matricula) {
        super(nome, idade, cpf);
        this.matricula = matricula;
        this.disciplinas = [];
    }

    adicionarDisciplina(disciplina) {
        this.disciplina.push(disciplina);
    }

    exibirInformacoes() {
        super.exibirInformacoes();
        console.log(`Matrícula: ${this.matricula}`);
        console.log("Disciplinas:");
        this.disciplinas.forEach((disciplina) => {
            console.log(` - ${disciplina.nome}`);
        });
    }
}

class Professor extends Pessoa {
    constructor(nome, idade, cpf, salario) {
        super(nome, idade, cpf);
        this.salario = salario;
    }

    exibirInformacoes() {
        super.exibirInformacoes();
        console.log(`Salário: ${this.salario}`);
    }
}

class Disciplina {
    constructor(nome, codigo, professor) {
        this.nome = nome;
        this.codigo = codigo;
        this.professor = professor;
        this.alunos = [];
    }

    adicionarAluno(aluno) {
        this.alunos.add(aluno);
    }

    exibirInformacoes() {
        console.log(`Disciplina: ${this.nome}, Código: ${codigo}`);
        console.log(`Professor: ${this.professor.nome}`);
        console.log("Alunos matriculados:");
        this.alunos.forEach((aluno) => {
            console.log(` - ${aluno.nome}`);
        });
    }
}

class Escola {
    constructor(nome) {
        this.nome = nome;
        this.alunos = [];
        this.professores = [];
        this.disciplinas = [];
    }

    adicionarAluno(aluno) {
        this.alunos.push(aluno);
    }

    adicionarProfessor(professor) {
        this.professores.push(professor);
    }

    adicionarDisciplina(disciplina) {
        this.disciplina.push(disciplina);
    }

    exibirAlunos() {
        console.log("Alunos matriculados:");
        this.alunos.forEach((aluno) => {
            aluno.exibirInformacoes();
        });
    }

    exibirProfessores() {
        console.log("Professores cadastrados:");
        this.professores.forEach((professor) => {
            professor.exibirInformacoes();
        });
    }

    exibirDisciplinas() {
        console.log("Disciplinas oferecidas:");
        this.disciplinas.forEach((disciplina) => {
            disciplina.exibirInformacoes();
        });
    }
}

// Funções auxiliares
function criarAluno() {
    let nome = prompt("Nome do aluno: ");
    let idade = prompt("Idade do aluno: ");
    let cpf = prompt("CPF do aluno: ");
    let matricula = prompt("Matrícula do aluno: ");
    let aluno = new Aluno(nome, idade, cpf, matricula);
    return aluno;
}

function criarProfessor() {
    let nome = prompt("Nome do professor: ");
    let idade = prompt("Idade do professor: ");
    let cpf = prompt("CPF do professor: ");
    let salario = parseFloat(prompt("Salário do professor: "));
    let professor = new Professor(nome, idade, cpf, salario);
    return professor;
}

function criarDisciplina(professores) {
    let nome = prompt("Nome da disciplina: ");
    let codigo = prompt("Código da disciplina: ");
    let opcao = parseInt(prompt("Escolha o professor pelo índice: ")) - 1;
    if (opcao < 0 || opcao >= professores.length) {
        console.log("Professor inválido!");
        return;
    }
    let disciplina = new Disciplina(nome, codigo, professores[opcao]);
    return disciplina;
}

// Inicialização do sistema
let escola = new Escola("Escola de Javascript");

// Menu principal
while (true) {
    console.log("\n--- Sistema de Gerenciamento Escolar ---");
    console.log("1. Adicionar aluno");
    console.log("2. Adicionar professor");
    console.log("3. Adicionar disciplina");
    console.log("4. Exibir alunos");
    console.log("5. Exibir professores");
    console.log("6. Exibir disciplinas");
    console.log("0. Sair");

    let opcao = parseInt(prompt("Escolha uma opção: "));

    if (opcao === 1) {
        let aluno = criarAluno();
        escola.adicionarAluno(aluno);
    } else if (opcao === 2) {
        let professor = criarProfessor();
        escola.adicionarProfessor(professor);
    } else if (opcao === 3) {
        if (escola.professores.length === 0) {
            console.log("Não há professores cadastrados.");
        } else {
            let disciplina = criarDisciplina(escola.professores);
            escola.adicionarDisciplina(disciplina);
        }
    } else if (opcao === 4) {
        escola.exibirAlunos();
    } else if (opcao === 5) {
        escola.exibirProfessores();
    } else if (opcao === 6) {
        escola.exibirDisciplinas();
    } else if (opcao === 0) {
        console.log("Saindo do sistema...");
        break;
    } else {
        console.log("Opção inválida! Tente novamente.");
    }
}
