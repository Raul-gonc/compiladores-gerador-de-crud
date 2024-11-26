import os
from antlr4 import InputStream, CommonTokenStream
from DatabaseModelLexer import DatabaseModelLexer
from DatabaseModelParser import DatabaseModelParser

# Função para gerar arquivos SQLAlchemy, Repositórios, Serviços e Schemas
def generate_fastapi_files(parsed_data):
    os.makedirs(f"output/models", exist_ok=True)
    os.makedirs(f"output/repositories", exist_ok=True)
    os.makedirs(f"output/services", exist_ok=True)
    os.makedirs(f"output/schemas", exist_ok=True)
    for table_name, table_data in parsed_data.items():
        #os.makedirs(f"output/{table_name}", exist_ok=True)

        # Gerar o Modelo SQLAlchemy
        generate_sqlalchemy_model(table_name, table_data)

        # Gerar o Repositório
        generate_repository(table_name)

        # Gerar o Serviço
        generate_service(table_name)

        # Gerar o Schema (Pydantic)
        generate_schema(table_name, table_data)

def generate_sqlalchemy_model(table_name, table_data):
    relations = table_data["relations"]
    lowName = table_name.lower()
    with open(f"output/models/{table_name}.py", "w") as model_file:
        model_file.write("from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey\n")
        model_file.write("from sqlalchemy.orm import relationship\n")
        model_file.write("from config.database import Base\n\n")

        model_file.write(f"class {table_name.capitalize()}(Base):\n")
        model_file.write(f"    __tablename__ = '{lowName}s'\n")

        # Gerar colunas
        columns = table_data["columns"]
        for column_name, column_type in columns.items():
            column_type_sqlalchemy = {
                "int": "Integer",
                "string": "String",
                "float": "Float",
                "datetime": "DateTime"
            }.get(column_type, "String")
            primary_key = "" if column_name != "id" else ", primary_key=True, index=True"
            model_file.write(f"    {column_name} = Column({column_type_sqlalchemy}{primary_key})\n")

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

def generate_repository(table_name):
    with open(f"output/repositories/{table_name}.py", "w") as repo_file:
        repo_file.write(f"""
from .models import {table_name.capitalize()}
from sqlalchemy.orm import Session

def get_all(db: Session):
    return db.query({table_name.capitalize()}).all()

def get_by_id(db: Session, item_id: int):
    return db.query({table_name.capitalize()}).filter({table_name.capitalize()}.id == item_id).first()

def create(db: Session, item_data: dict):
    item = {table_name.capitalize()}(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, item_id: int):
    item = db.query({table_name.capitalize()}).filter({table_name.capitalize()}.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None
""")

def generate_service(table_name):
    with open(f"output/services/{table_name}.py", "w") as service_file:
        service_file.write(f"""
from .repository import get_all, get_by_id, create, delete
from .models import {table_name.capitalize()}

def get_all_{table_name}s(db):
    return get_all(db)

def get_{table_name}(db, item_id: int):
    return get_by_id(db, item_id)

def create_{table_name}(db, item_data: dict):
    return create(db, item_data)

def delete_{table_name}(db, item_id: int):
    return delete(db, item_id)
""")

def generate_schema(table_name, table_data):
    with open(f"output/schemas/{table_name}.py", "w") as schema_file:
        schema_file.write("from pydantic import BaseModel\n")
        schema_file.write("from typing import List, Optional\n")
        schema_file.write("from datetime import datetime\n\n")

        # Definir o Schema Base
        schema_file.write(f"class {table_name.capitalize()}Base(BaseModel):\n")
        columns = table_data["columns"]
        for column_name, column_type in columns.items():
            python_type = {
                "int": "int",
                "string": "str",
                "float": "float",
                "datetime": "datetime"
            }.get(column_type, "str")
            schema_file.write(f"    {column_name}: {python_type}\n")

        # Definir o Schema Completo
        schema_file.write(f"\nclass {table_name.capitalize()}({table_name.capitalize()}Base):\n")
        schema_file.write(f"    id: int\n")
        schema_file.write(f"    created_at: datetime\n")
        schema_file.write(f"    updated_at: datetime\n")
        schema_file.write("\n    class Config:\n")
        schema_file.write("        orm_mode = True\n")

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
        events one-to-many Event
    }

    table Event {
        id int
        title string
        date datetime
        organizer one-to-one User
    }
    """
    parsed_data = parse_input(input_data)
    generate_fastapi_files(parsed_data)