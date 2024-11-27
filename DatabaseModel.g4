grammar DatabaseModel;

database: table+;

table: 'table' tableName=ID '{' (column | relation)+ '}';

column: columnName=ID columnType=TYPE PROP* PV;

relation: relationName=ID relationType=REL_TYPE relatedTable=ID PV;

TYPE: 'int' | 'string' | 'float' | 'boolean' | 'datetime';

PV: ';';

PROP: 'PRIMARY' | 'UNIQUE' | 'NOT NULL';

REL_TYPE: 'one-to-one' | 'one-to-many' | 'many-to-one';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;
