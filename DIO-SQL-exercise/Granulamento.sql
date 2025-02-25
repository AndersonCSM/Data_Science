UPDATE usuarios
SET rua = split_part(endereco, ',', 1),
    numero = split_part(endereco, ',', 2),
    cidade = split_part(endereco, ',', 3),
    estado = split_part(endereco, ',', 4);
