INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) VALUES 
(2, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
(3, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
(4, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

INSERT INTO destinos (id, nome, descricao) VALUES 
(2, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
(3, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(4, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

INSERT INTO reservas (id, id_usuario, id_destino, data, status) VALUES 
(2, 1, 2, '2023-07-10', 'confirmada'),
(3, 2, 1, '2023-08-05', 'pendente'),
(4, 3, 3, '2023-09-20', 'cancelada');