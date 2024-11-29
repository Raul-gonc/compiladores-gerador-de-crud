# Gerador de CRUD
Esta linguagem tem como finalidade receber especificações de tabelas e gerar as configurações iniciais e métodos básicos de um projeto em FastAPI. A nossa principal motivação é facilitar o processo de inicializar um projeto, sem desperdiçar tempo com a criação de arquivos básicos necessários para o funcionamento do mesmo. Queremos oferecer uma solução prática para criar a base de um projeto utilizando um framework.

## 1 - Instalação
     > wget https://www.antlr.org/download/antlr-4.13.2-complete.jar
     > mv antlr-4.13.2-complete.jar antlr.jar
     > pip install antlr4-python3-runtime

## 2 - Para compilar o ANTLR (Em caso de Mudanças na gramática)

    java -jar antlr.jar -Dlanguage=Python3 DatabaseModel.g4

## 3 - Especificações da linguagem:

### Definir tabela:

    table nome_tabela(operações) {
        nome_coluna tipo_coluna props;
        nome_relação tipo_relação tabela_relacionada;
    }

     operações disponíveis: POST,PUT,GET,DELETE
     tipos disponíveis: string,int,float,datetime,boolean
     props disponíveis: UNIQUE, PRIMARY, NOT NULL
     tipos de relação: one-to-one,one-to-many,many-to-one,many-to-many

## 4 - Exemplos de configuração do arquivo input.teste, é necessário definir os métodos que você quer criar (GET POST PUT DELETE) para gerar o projeto:

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
        enrollments one-to-one Enrollment;
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
        student one-to-one Student;
        course many-to-one Course;
    }

## 5 - Executar o analisador:

    python main.py arquivo

Exemplo:

    python main.py input.teste

## O código gerado pode ser encontrado na pasta output.

### Grupo:
Arthur Almeida - aas13@poli.br <br/>
Max José - mjan@poli.br <br/>
Raul Angelo - rags@poli.br