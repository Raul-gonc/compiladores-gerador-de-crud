grammar DatabaseModel;

database: table+;

table: 'table' tableName=ID '{' (column | relation)+ '}';

column: columnName=ID columnType=TYPE;

relation: relationName=ID relationType=REL_TYPE relatedTable=ID;

TYPE: 'int' | 'string' | 'float' | 'boolean' | 'datetime';

REL_TYPE: 'one-to-one' | 'one-to-many' | 'many-to-many';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;
