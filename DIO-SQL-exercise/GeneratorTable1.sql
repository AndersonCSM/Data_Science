CREATE TABLE usuarios(
    id INT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    endereco VARCHAR(50) NOT NULL,
    data_nascimento DATE NOT NULL
);

COMMENT ON COLUMN usuarios.nome IS 'Nome do usuário';
COMMENT ON COLUMN usuarios.email IS 'E-mail usuário';
COMMENT ON COLUMN usuarios.endereco IS 'Endereço usuário';
COMMENT ON COLUMN usuarios.data_nascimento IS 'Data nascimento';