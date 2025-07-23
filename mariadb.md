CREATE TABLE usuarios (
    matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    departamento VARCHAR(100),
    is_operador BOOLEAN DEFAULT FALSE,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chamados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    motivo_categoria VARCHAR(255),
    descricao TEXT,
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('aberto', 'em_andamento', 'fechado', 'negado') DEFAULT 'aberto',
    situacao ENUM('resolvido', 'nao_resolvido') DEFAULT 'nao_resolvido',
    data_fechamento DATETIME NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(matricula)
);

CREATE TABLE respostas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    chamado_id INT NOT NULL,
    operador_id INT NOT NULL,
    conclusao TEXT NOT NULL,
    data_resposta DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chamado_id) REFERENCES chamados(id) ON DELETE CASCADE,
    FOREIGN KEY (operador_id) REFERENCES usuarios(matricula)
);