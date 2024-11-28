# Gerador de CRUD
A equipe é formada por Arthur Almeida, Max Jose e Raul Angelo, tendo como principal motivação facilitar o processo de inicializar um projeto, sem desperdiçar tempo com a criação de arquivos básicos necessários para o funcionamento do mesmo. Queremos oferecer uma solução prática para criar a base de um projeto utilizando algum framework, como por exemplo o fastAPI.
A nossa linguagem, foi projetada para simplificar e automatizar a configuração inicial de projetos, eliminando tarefas repetitivas e manuais na criação de estruturas básicas. Com ela, você pode criar rapidamente a base de um projeto funcional utilizando frameworks como FastAPI, se preocupando apenas com a produtividade desde o início.

## 1 - Instalação
     > wget https://www.antlr.org/download/antlr-4.13.2-complete.jar
     > mv antlr-4.13.2-complete.jar antlr.jar
     > pip install antlr4-python3-runtime

## 2 - Para compilar o ANTLR (Em caso de Mudanças na gramática)

    java -jar antlr.jar -Dlanguage=Python3 DatabaseModel.g4

## 3 - Exemplos de configuração do arquivo input.teste, é necessário definir os métodos que você quer criar (GET POST PUT DELETE) para gerar o projeto:

### Exemplo 1:

    table User(GET POST PUT DELETE) {
        id int PRIMARY UNIQUE;
        name string NOT NULL ;
        email string NOT NULL ;
        events one-to-many Event ;
    }

    table Event(GET POST) {
        id int PRIMARY ;
        title string NOT NULL ;
        date datetime NOT NULL ;
        descricao string ;
        organizer many-to-one User ;
    }

### Exemplo 2:

    table Category(GET POST PUT DELETE) {
        id int PRIMARY UNIQUE;
        name string NOT NULL;
        description string;
        products one-to-many Product;
    }

    table Product(GET POST PUT DELETE) {
        id int PRIMARY UNIQUE;
        name string NOT NULL;
        price float NOT NULL;
        stock int NOT NULL;
        category many-to-one Category;
    }

### Exemplo 3:

    table Student(GET POST PUT DELETE) {
        id int PRIMARY UNIQUE;
        name string NOT NULL;
        email string UNIQUE NOT NULL;
        enrollments one-to-many Enrollment;
    }

    table Course(GET POST PUT DELETE) {
        id int PRIMARY UNIQUE;
        name string NOT NULL;
        description string;
        start_date datetime NOT NULL;
        enrollments one-to-many Enrollment;
    }

    table Enrollment(GET POST) {
        id int PRIMARY UNIQUE;
        enrollment_date datetime NOT NULL;
        student many-to-one Student;
        course many-to-one Course;
    }

## 4 - Executar o analisador:

    python main.py arquivo

Exemplo:

    python main.py input.teste

## O código gerado pode ser encontrado na pasta output.

### Grupo: