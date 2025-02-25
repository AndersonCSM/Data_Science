SELECT nome, (SELECT COUNT (*) FROM reservas WHERE id_usuario = usuarios.id) 
as total_reservas from usuarios;