# Sistema de Gerenciamento de Assinaturas

Este projeto é uma aplicação back-end simples para gerenciar assinaturas, construída utilizando Python com a biblioteca SQLModel para modelagem do banco de dados e SQLite para armazenamento.

## Visão Geral

O sistema permite:

*   Cadastrar novas assinaturas, armazenando informações como empresa, site, data de assinatura e valor.
*   Listar todas as assinaturas cadastradas.
*   Excluir assinaturas e seus pagamentos associados.
*   Registrar pagamentos para assinaturas específicas, com uma verificação para garantir que não haja pagamentos duplicados no mesmo mês.
*   Calcular o valor total de todas as assinaturas.
*   Gerar um gráfico com o valor total dos pagamentos dos últimos 12 meses.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **SQLModel:** Biblioteca para modelagem do banco de dados e interação com o SQLite.
*   **SQLite:** Banco de dados relacional simples para armazenamento das informações.
*   **matplotlib:** Biblioteca para gerar gráficos.
*   **Beekeeper Studio:** Software de gerenciamento e edição de banco de dados SQL multiplataforma.

## Configuração

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_SEU_REPOSITORIO>
    ```

2.  **Crie e ative um ambiente virtual Python (venv):**

    *   **Linux e macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    
    Este comando irá criar uma pasta `venv` no seu projeto.

    **Importante:** Certifique-se que você tem o Python instalado em seu sistema para criar o ambiente virtual.
    
3.  **Instale as dependências:**

    ```bash
    pip install sqlmodel matplotlib
    ```

4.  **Execute o script principal:**
   *  Execute o arquivo `main.py` para criar o banco e as tabelas.
    ```bash
    python main.py
    ```

## Como Usar

1.  Execute o arquivo `main.py` para inicializar o banco de dados (criar tabelas).
2. Importe e utilize o `SubscriptionService` na sua aplicação para realizar as operações de criação, listagem, exclusão e pagamento de assinaturas.

## Detalhes Adicionais

*   A classe `SubscriptionService` encapsula a lógica de negócios do sistema.
*   O banco de dados é armazenado em um arquivo chamado `database.db`.
