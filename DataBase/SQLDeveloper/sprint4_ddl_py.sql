CREATE TABLE bicicleta (
    id_bicicleta  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    marca         VARCHAR2(50),
    modelo        VARCHAR2(50),
    valor         FLOAT(2) NOT NULL,
    cliente_email VARCHAR2(255) NOT NULL
);

CREATE TABLE cliente (
    email                VARCHAR2(255) PRIMARY KEY,
    nome                 VARCHAR2(100) NOT NULL,
    telefone             VARCHAR2(11) NOT NULL,
    senha                VARCHAR2(50) NOT NULL
);

CREATE TABLE endereco (
    id_endereco        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cep                VARCHAR2(8) NOT NULL,
    logradouro         VARCHAR2(255) NOT NULL,
    numero             INTEGER NOT NULL,
    complemento        VARCHAR2(25),
    estado             VARCHAR2(2),
    cidade             VARCHAR2(25),
    cliente_email      VARCHAR2(255) NOT NULL
);

CREATE TABLE fisica (
    cpf           VARCHAR2(14) PRIMARY KEY,
    rg            VARCHAR2(12),
    cliente_email VARCHAR2(255) NOT NULL
);

CREATE TABLE judicial (
    cnpj          VARCHAR2(18) PRIMARY KEY,
    cliente_email VARCHAR2(255) NOT NULL
);

CREATE TABLE seguros (
    id_seguro              INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    seguro                 VARCHAR2(50) NOT NULL,
    id_bicicleta INTEGER NOT NULL
);

COMMIT;

ALTER TABLE bicicleta
    ADD CONSTRAINT bicicleta_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE fisica
    ADD CONSTRAINT fisica_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE judicial
    ADD CONSTRAINT judicial_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE seguros
    ADD CONSTRAINT seguros_bicicleta_fk FOREIGN KEY ( id_bicicleta )
        REFERENCES bicicleta ( id_bicicleta );
COMMIT;
