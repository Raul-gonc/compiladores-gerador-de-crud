# CompiladoresTurma2024.2
Exemplo de Projeto utilizando ANTLR para a turma da disciplina de compiladores no semestre 2024.2


1 - Instalação
     > wget https://www.antlr.org/download/antlr-4.13.2-complete.jar
     > mv antlr-4.13.2-complete.jar antlr.jar
     > pip install antlr4-python3-runtime

2 - Crie um arquivo de descrição de linguagem:

    Extensão g4 este arquivo deve possuir o mesmo nome da linguagem;

3 - Executar o ANTLR

    ```java -jar antlr.jar -Dlanguage=Python3 Expressoes.g4```

4 - Executar o analisador:
```
    import sys
    from antlr4 import *
    from ExpressoesLexer import ExpressoesLexer
    from ExpressoesParser import ExpressoesParser

    input_stream = FileStream(sys.argv[1])
    lexer = ExpressoesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExpressoesParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors()==0:
        print("ok")
        print(tree.toStringTree(recog=parser))
    else:
        print("erro sintático")
```

5 - Interpretar a árvore sintática....