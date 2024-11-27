from fastapiGenerator import generate_fastapi_files
from antlr4 import InputStream, CommonTokenStream
from DatabaseModelLexer import DatabaseModelLexer
from DatabaseModelParser import DatabaseModelParser

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = DatabaseModelLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatabaseModelParser(token_stream)
    tree = parser.database()

    tables = {}

    for table in tree.table():
        table_name = table.tableName.text
        columns = {}
        relations = []

        for column in table.column():
            column_name = column.columnName.text
            column_type = column.columnType.text
            column_props = []
            for prop in column.PROP():
                column_props.append(prop.getText())
            columns[column_name] = {"type": column_type, "props": column_props}

        for relation in table.relation():
            relation_name = relation.relationName.text
            relation_type = relation.relationType.text
            related_table = relation.relatedTable.text
            relations.append({"name": relation_name, "type": relation_type, "table": related_table, "back_name": None})
        tables[table_name] = {"columns": columns, "relations": relations}
    
    for table_name, table_data in tables.items():
        for relation in table_data["relations"]:
            related_table_name = relation["table"]

            if relation["type"] == "one-to-many":
                for related_relation in tables[related_table_name]["relations"]:
                    if related_relation["type"] == "many-to-one" and related_relation["table"] == table_name:
                        relation["back_name"] = related_relation["name"]
                        break
            elif relation["type"] == "many-to-one":
                for related_relation in tables[related_table_name]["relations"]:
                    if related_relation["type"] == "one-to-many" and related_relation["table"] == table_name:
                        relation["back_name"] = related_relation["name"]
                        break

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