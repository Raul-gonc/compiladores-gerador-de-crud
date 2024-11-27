import os
import shutil

def generate_fastapi_files(parsed_data):
    os.makedirs(f"output/models", exist_ok=True)
    os.makedirs(f"output/repositories", exist_ok=True)
    os.makedirs(f"output/services", exist_ok=True)
    os.makedirs(f"output/controllers", exist_ok=True)
    os.makedirs(f"output/schemas", exist_ok=True)
    shutil.copytree("base-fastapi", "output", dirs_exist_ok=True)
    for table_name, table_data in parsed_data.items():
        generate_sqlalchemy_model(table_name, table_data)
        generate_repository(table_name)
        generate_service(table_name)
        generate_controller(table_name)
        generate_schema(table_name, table_data)

def generate_sqlalchemy_model(table_name, table_data):
    relations = table_data["relations"]
    low_name = table_name.lower()
    with open(f"output/models/{table_name}.py", "w") as model_file:
        model_file.write("from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func\n")
        model_file.write("from sqlalchemy.orm import relationship\n")
        model_file.write("from config.database import Base\n\n")

        model_file.write(f"class {table_name.capitalize()}(Base):\n")
        model_file.write(f"    __tablename__ = '{low_name}s'\n")

        # Gerar colunas
        columns = table_data["columns"]
        for column_name, column_data in columns.items():
            column_type_sqlalchemy = {
                "int": "Integer",
                "string": "String",
                "float": "Float",
                "datetime": "DateTime"
            }.get(column_data["type"], "String")

            # Verificar propriedades
            props = column_data["props"]
            primary_key = "primary_key=True" if "PRIMARY" in props else ""
            nullable = "nullable=False" if "NOT NULL" in props else ""
            unique = "unique=True" if "UNIQUE" in props else ""
            options = [primary_key, nullable, unique]
            options = list(filter(None, options)) 

            if options:
                model_file.write(f"    {column_name} = Column({column_type_sqlalchemy}, {', '.join(options)})\n")
            else:
                model_file.write(f"    {column_name} = Column({column_type_sqlalchemy})\n")

        for relation in relations:
            relation_name = relation["name"]
            relation_type = relation["type"]
            related_table = relation["table"]
            related_table_lower = relation["table"]
            related_table_lower = related_table_lower.lower()
            back_related_table = relation["back_name"]

            if relation_type == "one-to-many":
                model_file.write(f"    {relation_name} = relationship('{related_table.capitalize()}', back_populates='{back_related_table}')\n")
            elif relation_type == "many-to-one":
                model_file.write(f"    {relation_name}_id = Column(Integer, ForeignKey('{related_table_lower}s.id'))\n")
                model_file.write(f"    {relation_name} = relationship('{related_table.capitalize()}', back_populates='{back_related_table}')\n")
            elif relation_type == "one-to-one":
                model_file.write(f"    {relation_name}_id = Column(Integer, ForeignKey('{related_table_lower}s.id'))\n")
                model_file.write(f"    {relation_name} = relationship('{related_table.capitalize()}')\n")

        model_file.write("\n    created_at = Column(DateTime, default=func.now())\n")
        model_file.write("    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())\n")

def generate_repository(table_name):
    with open(f"output/repositories/{table_name}.py", "w") as repo_file:
        repo_file.write(f"""
from models.{table_name} import {table_name.capitalize()}
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
        
def generate_controller(table_name):
    with open(f"output/controllers/{table_name}.py", "w") as controller_file:
        controller_file.write(f"""
from fastapi import APIRouter, HTTPException
from models.{table_name} import {table_name.capitalize()}
from services.{table_name} import get_all_{table_name.lower()}s, get_{table_name.lower()}, create_{table_name.lower()}, delete_{table_name.lower()}

router = APIRouter()

@router.get("{table_name}/")
def read_items():
    return get_all_{table_name.lower()}s()

@router.get("{table_name}/{{id}}")
def read_item({table_name.lower()}_id: int):
    item = get_{table_name.lower()}({table_name.lower()}_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("{table_name}/")
def create_item(item: {table_name.capitalize()}):
    return create_{table_name.lower()}(item)

@router.delete("{table_name}/{{id}}")
def delete_item({table_name.lower()}_id: int):
    delete_{table_name.lower()}({table_name.lower()}_id)
    return {{"message": "Deleted"}}
""")

def generate_service(table_name):
    with open(f"output/services/{table_name}.py", "w") as service_file:
        service_file.write(f"""
from repositories.{table_name} import get_all, get_by_id, create, delete
from models.{table_name} import {table_name.capitalize()}

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
        for column_name, column_data in columns.items():
            column_type = column_data["type"]
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