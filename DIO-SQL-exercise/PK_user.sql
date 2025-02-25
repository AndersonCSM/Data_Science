
-- 2. Renomear a coluna 'id' antiga para 'old_id'
ALTER TABLE usuarios RENAME COLUMN id TO old_id;

-- 3. Adicionar a nova coluna 'id' como 'SERIAL'
ALTER TABLE usuarios ADD COLUMN id SERIAL;

-- 4. Copiar dados da coluna 'old_id' para a nova coluna 'id'
UPDATE usuarios SET id = old_id;

-- 5. Definir a nova coluna 'id' como chave primária
ALTER TABLE usuarios ADD PRIMARY KEY (id);

-- 6. Remover a coluna 'old_id' se não for mais necessária
ALTER TABLE usuarios DROP COLUMN old_id;
