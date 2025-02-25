-- Migrando os dados --

INSERT INTO usuarios_nova (id, nome, email, endereco, data_nascimento)
SELECT id, nome, email, endereco, data_nascimento
from usuarios;