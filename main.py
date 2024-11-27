import sys
from fastapiGenerator import generate_fastapi_files
from antlr4 import InputStream, CommonTokenStream
from DatabaseModelLexer import DatabaseModelLexer
from DatabaseModelParser import DatabaseModelParser
tables = {}

def parse_columns(table_column):
    columns = {}
    for column in table_column:
        column_name = column.columnName.text
        column_type = column.columnType.text
        column_props = []

        for prop in column.PROP():
            column_props.append(prop.getText())

        if not column_name:
            raise Exception("A coluna não possui nome")
        if not column_type:
            raise Exception(f"A coluna '{column_name}' não possui um tipo definido.")

        columns[column_name] = {"type": column_type, "props": column_props}
    return columns


def parse_relations(table_relations):
    relations = []
    for relation in table_relations:
        relation_name = relation.relationName.text
        relation_type = relation.relationType.text
        related_table = relation.relatedTable.text

        if not relation_name:
            raise Exception("A relação não possui nome")
        if not relation_type:
            raise Exception(f"A relação '{relation_name}' não possui um tipo definido")
        if not related_table:
            raise Exception(f"A relação '{relation_name}' não possui uma tabela relacionada")

        relations.append({"name": relation_name, "type": relation_type, "table": related_table, "back_name": None})
    return relations

def parse_table(table):
    table_name = table.tableName.text
    table_count = 0

    if not table_name:
        raise Exception("A tabela não possui nome")
    for current_table_name, _ in tables.items():
        if current_table_name == table_name:
            table_count += 1
        if table_count > 1:
            raise Exception("Já existe uma tabela com esse nome")

    columns = parse_columns(table.column())
    relations = parse_relations(table.relation())

    return {"columns": columns, "relations": relations}

def check_inverse_relation():
    for table_name, table_data in tables.items():
        for relation in table_data["relations"]:
            related_table_name = relation["table"]
            inverse_relation_name = ""

            if relation["type"] == "one-to-many":
                inverse_relation_name = "many-to-one"
            elif relation["type"] == "many-to-one":
                inverse_relation_name = "one-to-many"

            if inverse_relation_name != "":
                inverse_relation_found = False
                for related_relation in tables[related_table_name]["relations"]:
                    if related_relation["type"] == inverse_relation_name and related_relation["table"] == table_name:
                        relation["back_name"] = related_relation["name"]
                        inverse_relation_found = True
                        break

                if not inverse_relation_found:
                    raise Exception(
                        f"A tabela {related_table_name} não possui uma relação inversa do tipo {inverse_relation_name} para {table_name}, necessária como inversa da relação '{relation['name']}' em {table_name}"
                    )

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = DatabaseModelLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatabaseModelParser(token_stream)
    tree = parser.database()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("O código tem um erro sintático")
        sys.exit(1)

    for table in tree.table():
        table_name = table.tableName.text
        tables[table_name] = parse_table(table)
    
    check_inverse_relation()

    return tables

if __name__ == "__main__":
    input_data = """
    table User {
        id int PRIMARY UNIQUE;
        name string NOT NULL ;
        email string NOT NULL ;
        events one-to-many Event ;
    }

    table Event {
        id int PRIMARY ;
        title string NOT NULL ;
        date datetime NOT NULL ;
        descricao string ;
        organizer many-to-one User ;
    }
    """
    parsed_data = parse_input(input_data)
    generate_fastapi_files(parsed_data)