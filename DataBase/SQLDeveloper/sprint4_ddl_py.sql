CREATE TABLE bicicleta (
    id_bicicleta  INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
    marca         VARCHAR2(50),
    modelo        VARCHAR2(50),
    valor         FLOAT(2) NOT NULL,
    cliente_email VARCHAR2(255) NOT NULL
);

ALTER TABLE bicicleta ADD CONSTRAINT bicicleta_pk PRIMARY KEY ( id_bicicleta );

CREATE TABLE cliente (
    email                VARCHAR2(255) NOT NULL,
    nome                 VARCHAR2(100) NOT NULL,
    telefone             VARCHAR2(9) NOT NULL,
    senha                VARCHAR2(50) NOT NULL,
    endereco_id_endereco INTEGER NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( email );

CREATE TABLE endereco (
    id_endereco INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
    cep         VARCHAR2(8) NOT NULL,
    rua         VARCHAR2(255) NOT NULL,
    numero      INTEGER NOT NULL,
    complemento VARCHAR2(10),
    estado      VARCHAR2(2),
    cidade      VARCHAR2(25)
);

ALTER TABLE endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( id_endereco );

CREATE TABLE fisica (
    cpf           VARCHAR2(14) NOT NULL,
    rg            VARCHAR2(12),
    cliente_email VARCHAR2(255) NOT NULL
);

ALTER TABLE fisica ADD CONSTRAINT fisica_pk PRIMARY KEY ( cpf );

CREATE TABLE judicial (
    cnpj          VARCHAR2(18) NOT NULL,
    cliente_email VARCHAR2(255) NOT NULL
);

ALTER TABLE judicial ADD CONSTRAINT judicial_pk PRIMARY KEY ( cnpj );

CREATE TABLE seguros (
    id_seguro              INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
    seguro                 VARCHAR2(50) NOT NULL,
    bicicleta_id_bicicleta INTEGER NOT NULL
);

ALTER TABLE seguros ADD CONSTRAINT seguros_pk PRIMARY KEY ( id_seguro );

COMMIT;


ALTER TABLE bicicleta
    ADD CONSTRAINT bicicleta_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_endereco_fk FOREIGN KEY ( endereco_id_endereco )
        REFERENCES endereco ( id_endereco );

ALTER TABLE fisica
    ADD CONSTRAINT fisica_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE judicial
    ADD CONSTRAINT judicial_cliente_fk FOREIGN KEY ( cliente_email )
        REFERENCES cliente ( email );

ALTER TABLE seguros
    ADD CONSTRAINT seguros_bicicleta_fk FOREIGN KEY ( bicicleta_id_bicicleta )
        REFERENCES bicicleta ( id_bicicleta );

COMMIT;

INSERT INTO seguros 
    VALUES ();
