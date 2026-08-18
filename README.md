# To-Do List (linha de comando)

Aplicação simples de linha de comando para gerenciar tarefas, feita em Python puro.
As tarefas são salvas em um arquivo `tarefas.json`, então nada se perde quando o programa é fechado.

## Funcionalidades
- Adicionar tarefa
- Listar tarefas (mostrando o que já foi concluído)
- Marcar tarefa como concluída
- Remover tarefa

## Tecnologias
- Python 3
- Módulo `json` da biblioteca padrão (sem dependências externas)

## Estrutura do projeto
```
todo-cli/
├── main.py       → menu e loop principal
├── tarefas.py    → lógica de dados (carregar, salvar, adicionar, concluir, remover)
└── tarefas.json  → gerado automaticamente ao rodar
```

## Como rodar
```bash
git clone <link-do-repositorio>
cd todo-cli
python main.py
```

## Aprendizados
Este projeto foi feito para praticar:
- Manipulação de arquivos e persistência de dados com JSON
- Organização de código em funções
- Estruturas de repetição e condicionais
- Tratamento básico de erros de entrada do usuário

## Próximos passos
- [ ] Adicionar prioridade e data de prazo às tarefas
- [ ] Migrar armazenamento de JSON para SQLite
- [ ] Ordenar tarefas por prioridade
