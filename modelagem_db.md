erDiagram
    usuarios {
        int matricula PK
        string nome
        string email
        string departamento
        boolean is_operador
        boolean is_admin
        datetime created_at
    }

    chamados {
        int id PK
        int usuario_id FK
        string motivo_categoria
        text descricao
        datetime data_abertura
        enum status
        enum situacao
        datetime data_fechamento
        datetime updated_at
    }

    respostas {
        int id PK
        int chamado_id FK
        int operador_id FK
        text conclusao
        datetime data_resposta
    }

    usuarios ||--o{ chamados : "abre"
    usuarios ||--o{ respostas : "responde"
    chamados ||--o{ respostas : "possui"