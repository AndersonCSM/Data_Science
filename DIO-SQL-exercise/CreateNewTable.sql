CREATE TABLE usuarios_nova (
  id INT,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  data_nascimento DATE NOT NULL,
  endereco VARCHAR(100) NOT NULL
);

COMMENT ON COLUMN usuarios_nova.nome IS 'Nome do usuário';
COMMENT ON COLUMN usuarios_nova.email IS 'Endereço de e-mail do usuário';
COMMENT ON COLUMN usuarios_nova.data_nascimento IS 'Data de nascimento do usuário';
COMMENT ON COLUMN usuarios_nova.endereco IS 'Endereço do Cliente';
