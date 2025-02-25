CREATE TABLE destinos (
    id INT,
    nome VARCHAR(255) NOT NULL UNIQUE,
    descricao VARCHAR(255) NOT NULL
);

COMMENT ON COLUMN destinos.nome IS 'Nome do destino';
COMMENT ON COLUMN destinos.descricao IS 'Descrição do destino';

CREATE TABLE reservas (
    id INT,
    id_usuario INT,
    id_destino INT,
    data DATE,
    status VARCHAR(255) DEFAULT 'pendentes'
);

COMMENT ON COLUMN reservas.id IS 'Identificador único da reserva';
COMMENT ON COLUMN reservas.id_usuario IS 'Referência ao ID do usuário que fez a reserva';
COMMENT ON COLUMN reservas.id_destino IS 'Referência ao ID do destino de reserva';
COMMENT ON COLUMN reservas.data IS 'Data da reserva';
COMMENT ON COLUMN reservas.status IS 'Status da reserva (confirmada, pendente, cancelada, etc.)';
