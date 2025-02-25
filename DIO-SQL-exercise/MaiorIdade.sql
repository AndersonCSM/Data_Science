SELECT MAX(EXTRACT(YEAR FROM AGE(CURRENT_DATE, data_nascimento))) AS maior_idade
FROM usuarios;
