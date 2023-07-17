# API de Gestão de Estoque usando Django
Este é um projeto de API desenvolvido em Python usando o framework Django para gestão de estoque. A API permite cadastrar, atualizar, excluir e listar produtos em estoque, além de realizar vendas e compras. Também inclui funcionalidades de cadastro e autenticação de usuários e funcionários, bem como controle de folha de ponto.

Requisitos
Python 3.x
Django 3.x
Banco de Dados (SQLite, MySQL ou outro compatível com Django)
Instalação

Clone o repositório para sua máquina local:
git clone https://github.com/seu-usuario/nome-do-repositorio.git

Acesse o diretório do projeto:
cd nome-do-repositorio

Instale as dependências usando o pip:
pip install -r requirements.txt

Execute as migrações para criar o banco de dados:
python manage.py migrate

Inicie o servidor de desenvolvimento:
python manage.py runserver

Agora a API estará disponível em http://localhost:8000/.

Endpoints Disponíveis
Cadastro de Usuário
Endpoint: /cadastro/usuario/
Método: POST
Parâmetros: JSON contendo informações do usuário a ser cadastrado (cpf, nome, senha, idade, email, login).
Retorno: JSON com o status do cadastro ou mensagem de erro.
Cadastro de Funcionário
Endpoint: /rh/cadastro/
Método: POST
Parâmetros: JSON contendo informações do funcionário a ser cadastrado (cpf, nome, cargo, salario, carga_horaria, senha, tipo_acesso).
Retorno: JSON com o status do cadastro ou mensagem de erro.
Cadastro de Produto
Endpoint: /gestao-estoque/cadastro/produto/
Método: POST
Parâmetros: JSON contendo informações do produto a ser cadastrado (qtd_estoque, descricao, nome, preco, categoria, tipo).
Retorno: JSON com o status do cadastro ou mensagem de erro.
Listar Produtos em Estoque
Endpoint: /gestao-estoque/quantidade-prod/
Método: GET
Retorno: JSON contendo uma lista de produtos em estoque.
Excluir Produto
Endpoint: /gestao-estoque/excluir-prod/
Método: DELETE
Parâmetros: JSON contendo id do produto a ser excluído, cpf e senha do funcionário.
Retorno: JSON com o status da exclusão ou mensagem de erro.
Realizar Venda
Endpoint: /gestao-estoque/venda/
Método: POST
Parâmetros: JSON contendo cpf do usuário e lista de produtos com suas respectivas quantidades a serem vendidas.
Retorno: JSON com o status da venda ou mensagem de erro.
Realizar Compra
Endpoint: /gestao-estoque/comprar/
Método: PUT
Parâmetros: JSON contendo cpf do funcionário, senha, tipo de acesso e lista de produtos com suas respectivas quantidades a serem compradas.
Retorno: JSON com o status da compra ou mensagem de erro.
Registro de Entrada na Folha de Ponto
Endpoint: /ponto/folhapontochegada/
Método: POST
Parâmetros: JSON contendo cpf do funcionário.
Retorno: JSON com o status do registro de entrada ou mensagem de erro.
Registro de Saída na Folha de Ponto
Endpoint: /ponto/folhapontosaida/
Método: POST
Parâmetros: JSON contendo cpf do funcionário.
Retorno: JSON com o status do registro de saída ou mensagem de erro.
Login do Usuário
Endpoint: /login/
Método: POST
Parâmetros: JSON contendo login e senha do usuário.
Retorno: JSON com o status do login ou mensagem de erro.
Login do Funcionário
Endpoint: /rh/login/
Método: POST
Parâmetros: JSON contendo login e senha do funcionário.
Retorno: JSON com o status do login ou mensagem de erro.
Recuperação de Senha
Endpoint: /login/esquecisenha/
Método: POST
Parâmetros: JSON contendo cpf, email, nova senha e login do usuário.
Retorno: JSON com o status da alteração de senha ou mensagem de erro.
Observações
Lembre-se de configurar as permissões adequadas para os endpoints de acordo com as regras do seu negócio.
Contribuindo
Se desejar contribuir para este projeto, sinta-se à vontade para enviar pull requests ou abrir issues.
