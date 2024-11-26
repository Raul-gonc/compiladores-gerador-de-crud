import os
from antlr4 import InputStream, CommonTokenStream
from DatabaseModelLexer import DatabaseModelLexer
from DatabaseModelParser import DatabaseModelParser

def generate_sqlalchemy_models(parsed_data):
    for table_name, table_data in parsed_data.items():
        os.makedirs(f"output/{table_name}", exist_ok=True)

        columns = table_data["columns"]
        relations = table_data["relations"]
        lowName = table_name.lower()

        # Gerar o modelo SQLAlchemy
        with open(f"output/{table_name}/models.py", "w") as model_file:
            model_file.write("from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func\n")
            model_file.write("from sqlalchemy.orm import relationship\n")
            model_file.write("from config.database import Base\n\n")
            
            model_file.write(f"class {table_name.capitalize()}(Base):\n")
            model_file.write(f"    __tablename__ = '{lowName}s'\n\n")

            for column_name, column_type in columns.items():
                column_type_sql = {
                    "int": "Integer",
                    "string": "String",
                    "float": "Float",
                    "boolean": "Boolean",
                    "datetime": "DateTime"
                }[column_type]
                model_file.write(f"    {column_name} = Column({column_type_sql})\n")

            # Gerar relacionamentos
            for relation in relations:
                relation_name = relation["name"]
                relation_type = relation["type"]
                related_table = relation["table"]

                if relation_type == "one-to-many":
                    model_file.write(f"    {relation_name} = relationship('{related_table.capitalize()}', back_populates='{table_name}')\n")
                elif relation_type == "many-to-one":
                    model_file.write(f"    {relation_name}_id = Column(Integer, ForeignKey('{related_table}s.id'))\n")
                elif relation_type == "one-to-one":
                    model_file.write(f"    {relation_name}_id = Column(Integer, ForeignKey('{related_table}s.id'))\n")
                    model_file.write(f"    {relation_name} = relationship('{related_table.capitalize()}')\n")

            model_file.write("\n    created_at = Column(DateTime, default=func.now())\n")
            model_file.write("    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())\n")

        # Gerar repositório, service, controller (como antes)
        # Repositório
        with open(f"output/{table_name}/repository.py", "w") as repo_file:
            repo_file.write("""
data = []

def get_all():
    return data

def get_one(id: int):
    return next((item for item in data if item['id'] == id), None)

def create(item: dict):
    data.append(item)
    return item

def delete(id: int):
    global data
    data = [item for item in data if item['id'] != id]

# Relações
def get_related_{table_name.lower()}(relation_key: str, relation_value):
    return [item for item in data if item.get(relation_key) == relation_value]
""")

        # Serviço
        with open(f"output/{table_name}/service.py", "w") as service_file:
            service_file.write(f"""
from .repository import get_all, get_one, create, delete, get_related_{table_name.lower()}
from .models import {table_name.capitalize()}

def get_all_{table_name.lower()}s():
    return get_all()

def get_{table_name.lower()}(id: int):
    return get_one(id)

def create_{table_name.lower()}(item: {table_name.capitalize()}):
    return create(item.dict())

def delete_{table_name.lower()}(id: int):
    return delete(id)

def get_related_{table_name.lower()}s(relation_key: str, relation_value):
    return get_related_{table_name.lower()}(relation_key, relation_value)
""")

        # Controlador
        with open(f"output/{table_name}/controller.py", "w") as controller_file:
            controller_file.write(f"""
from fastapi import APIRouter, HTTPException
from .models import {table_name.capitalize()}
from .service import get_all_{table_name.lower()}s, get_{table_name.lower()}, create_{table_name.lower()}, delete_{table_name.lower()}

router = APIRouter()

@router.get("/")
def read_items():
    return get_all_{table_name.lower()}s()

@router.get("/{table_name.lower()}_id")
def read_item({table_name.lower()}_id: int):
    item = get_{table_name.lower()}({table_name.lower()}_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
def create_item(item: {table_name.capitalize()}):
    return create_{table_name.lower()}(item)

@router.delete("/{table_name.lower()}_id")
def delete_item({table_name.lower()}_id: int):
    delete_{table_name.lower()}({table_name.lower()}_id)
    return {{"message": "Deleted"}}
""")

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = DatabaseModelLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DatabaseModelParser(token_stream)
    tree = parser.database()

    tables = {}
    for table_ctx in tree.table():
        table_name = table_ctx.tableName.text
        columns = {}
        relations = []
        for column_ctx in table_ctx.column():
            column_name = column_ctx.columnName.text
            column_type = column_ctx.columnType.text
            columns[column_name] = column_type
        for relation_ctx in table_ctx.relation():
            relation_name = relation_ctx.relationName.text
            relation_type = relation_ctx.relationType.text
            related_table = relation_ctx.relatedTable.text
            relations.append({"name": relation_name, "type": relation_type, "table": related_table})
        tables[table_name] = {"columns": columns, "relations": relations}
    return tables

if __name__ == "__main__":
    input_data = """
    table User {
        id int
        name string
        email string
        events one-to-many Event id
    }

    table Event {
        id int
        title string
        date datetime
        organizer one-to-one User id
    }
    """
    parsed_data = parse_input(input_data)
    generate_sqlalchemy_models(parsed_data)