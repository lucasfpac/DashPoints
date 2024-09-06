# DashPoints Backend

### Descrição
O **DashPoints** é um sistema de gerenciamento de usuários com um sistema de pontos, permitindo que os usuários sejam cadastrados, acumulem pontos e sejam monitorados através de um dashboard.

## Instalação

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/seu-usuario/dashpoints-backend.git
    cd dashpoints-backend
    ```

2. **Crie e ative o ambiente virtual:**

    Se estiver usando `pipenv`:

    ```bash
    pipenv install
    pipenv shell
    ```

    Ou, se estiver usando `virtualenv`:

    ```bash
    virtualenv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```


5. **Migrações do banco de dados:**

    Após configurar o banco de dados, aplique as migrações para criar as tabelas:

    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário (opcional):**

    Para acessar o painel administrativo do Django, você pode criar um superusuário:

    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor:**

    Por fim, execute o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    O backend estará rodando no endereço: `http://127.0.0.1:8000/`

## Funcionalidades

- **Autenticação de Usuário**: Registre, faça login e gerencie usuários.
- **Sistema de Pontuação**: Adicione e subtraia pontos de usuários.
- **Dashboard de Monitoramento**: Exibe o ranking dos usuários com mais pontos e estatísticas gerais.
- **API REST**: Utilizando Django REST Framework para comunicação com o frontend React.

## Endpoints

A seguir estão os principais endpoints da API:

- `POST /api/register/`: Registrar um novo usuário.
- `POST /api/login/`: Fazer login.
- `GET /api/users/`: Listar todos os usuários.
- `GET /api/user/<id>/`: Detalhes de um usuário.
- `POST /api/user/<id>/add-points/`: Adicionar pontos a um usuário.
- `GET /api/dashboard/`: Exibir estatísticas do dashboard (usuário com mais pontos, média de pontos, etc.).

## Estrutura do Projeto

- `core/`: Aplicação principal.
- `users/`: Módulo responsável pelo gerenciamento de usuários.
- `points/`: Módulo responsável pelo gerenciamento do sistema de pontos.
- `dashboard/`: Lida com o cálculo e exibição de dados para o dashboard.
- `api/`: Configuração da API REST usando Django REST Framework.

## Testes

Para rodar os testes:

```bash
python manage.py test
```

## Contribuição
Se você quiser contribuir, siga estas etapas:

- Faça um fork deste repositório.
- Crie uma nova branch: git checkout -b minha-branch.
- Faça suas alterações e commit: git commit -m 'Minhas alterações'.
- Faça o push da branch: git push origin minha-branch.
- Abra um Pull Request.

## Licença
Este projeto está licenciado sob a MIT License.