# Documentação do Projeto

Este repositório contém a biblioteca **ryo**, utilizada para automatizar tarefas relacionadas a repositórios e workflows. O arquivo `config.yml` dentro deste repositório serve como um arquivo de configuração de exemplo ou para testes internos da própria biblioteca **ryo**. Ele demonstra a estrutura esperada para configurar e executar as **tasks** utilizando a biblioteca **ryo**. Cada **task** definida neste arquivo de exemplo contém uma série de etapas denominadas **steps**, que especificam as ações a serem realizadas pela **ryo**. O arquivo é estruturado em YAML e ilustra a personalização do comportamento de cada tarefa que a biblioteca **ryo** pode automatizar.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes programas instalados:

- [Git](https://git-scm.com/downloads)
- [GitHub CLI (gh)](https://cli.github.com/)
- [Python](https://www.python.org/downloads/)

## Configurando o GitHub CLI

Para utilizar os recursos do GitHub CLI, siga os passos abaixo para autenticação:

```bash
gh auth login
-> GitHub.com
-> HTTPS
-> Authenticate with your Gihub credentials
-> Login with web browser
-> Enter para acessar a URL
-> Acessar o Link e acrescentar o código que aparecerá no terminal
```
 
## Organização do repositorio
├─ ryo/
│   └─ ryo/
│       └── src/         
│           ├── __init__.py
│           ├── cli.py
│           ├── core.py
│           ├── github.py
│           ├── runner.py
│           └── utils.py
├──── tests/
│       ├── __init__.py
│       ├── test_core.py
│       ├── test_github.py
│       ├── test_runner.py
│       ├── test_utils.py
│       └── test_cli.py
├──── setup.py
├── README.md
├── config.yml
└── .gitignore

## Como utilizar
### Estrutura do `config.yml`

O arquivo `config.yml` é onde você define as tarefas (tasks) a serem executadas. Cada task pode ter uma série de etapas (steps), cada uma com ações específicas a serem realizadas. A seguir, temos um exemplo de como o arquivo pode ser estruturado.

### Exemplo de `config.yml`

```yaml
tasks:
  example-task:
    repository: minha_lib\workflow   # Repositório no qual a task será executada
    steps:
      - action: commit_file           # Ação para fazer commit de um arquivo
        auto_commit: 'true'           # Ativa o commit automático (Opcional)
        commit_msg: "Segundo repositorio"  # Mensagem do commit (Opcional)
        repository: minha_lib\teste3\workflow   # Repositório específico para a ação de commit (Opcional)

      - action: commit_file           # Novo commit sem uma mensagem específica
        auto_commit: 'true'           # Commit automático

      - action: workflow_monitor      # Monitora o workflow  "1 - FEAT - Build and PR"
        workflow_name: "1 - FEAT - Build and PR"
        show_workflow: 'true'         # Abre uma nova aba no navegador após a finalização da execução

      - action: approve_pull_request  # Aprova o pull request da branch feature-teste para develop
        source_branch: feature-teste
        target_branch: develop

      - action: workflow_monitor      
        workflow_name: "2 - DEV - Build and Deploy"
        show_workflow: 'true'

      - action: approve_pull_request  # Aprova o pull request da branch develop para release/*
        source_branch: develop
        target_branch: release/*

      - action: workflow_monitor      # Monitora o workflow de homologação
        workflow_name: "3 - HOM - Homologacao"
        show_workflow: 'true'

      - action: approve_pull_request  # Aprova o pull request da branch release/* para main
        source_branch: release/*
        target_branch: main
```

## Parametros

|Comando|Descrição|Obrigatório|Valores Possíveis|Valor Default|
|---|---|---|---|---|
|`tasks`|Define um conjunto de **tasks** que serão executadas.|Sim|||
|`example-task`|Nome de uma task específica.|Sim|Qualquer nome válido para a task.||
|`repository`|Define o repositório onde a **task** será executada.|Sim|Caminho do repositório.||
|`steps`|Lista de etapas dentro de uma **task**.|Sim|Uma lista de etapas em YAML.||
|`action`|Define a ação que será realizada em cada etapa.|Sim|`commit_file`, `workflow_monitor`, `approve_pull_request`||
|`auto_commit`|(`commit_file`) Permite que o commit seja feito automaticamente. Caso habilitado, o commit automático será realizado no arquivo README.md e apenas se nenhuma outra alteração for encontrada.|Não|`'true'`, `'false'`|`'false'`|
|`commit_msg`|(`commit_file`)Mensagem que será associada ao commit.|Não|Qualquer texto para a mensagem do commit|`"Segundo repositorio"`, `"Atualização automática"`|
|`repository`|(`commit_file`)Repositório específico para a ação de commit.|Não|Caminho do repositório.|`minha_lib\teste3\workflow`|
|`workflow_name`|(`workflow_monitor`)Nome do workflow a ser monitorado.|Sim|Qualquer nome de workflow.|`"1 - FEAT - Build and PR"`, `"2 - DEV - Build and Deploy"`, `"3 - HOM - Homologacao"`|
|`show_workflow`|(`workflow_monitor`)Abre uma aba no navegador com a execução do workflow em caso de sucesso ou erro `'true'`.|Não|`'true'`, `'false'`|`'true'`|
|`source_branch`|(`approve_pull_request`)Define o branch de origem para o pull request.|Não|Nome de qualquer branch válido.|`"feature-teste"`, `"develop"`, `"release/*"`|
|`target_branch`|(`approve_pull_request`)Define o branch de destino para o pull request.|Não|Nome de qualquer branch válido.|`"develop"`, `"release/*"`, `"main"`|


### Observações e Regras de Utilização:

1.  **Repositório em `commit_file`:** Se nenhum repositório for especificado dentro da action `commit_file`, o workflow principal da task (`repository` definido no nível da task) será utilizado.
2.  **`auto_commit`:** Se o parâmetro `auto_commit` tiver o valor `"true"`, e caso nenhuma outra alteração seja feita dentro do repositório especificado na action, o arquivo `README.md` será alterado automaticamente com a mensagem definida em `commit_msg`.
3.  **Nomes de Workflow:** Os nomes dos workflows definidos em `workflow_name` não podem possuir caracteres especiais, como `&`.
4.  **Aprovação Automática de PR:** Na action `approve_pull_request`, apenas Pull Requests que não possuam conflitos e que já tenham recebido as aprovações necessárias serão aprovados automaticamente.
5.  **Branch para Aprovação de PR:** Na action `approve_pull_request`, apenas uma das branches (ou `source_branch` ou `target_branch`) pode utilizar o caractere curinga `*`. A outra branch deve ter um nome bem definido.