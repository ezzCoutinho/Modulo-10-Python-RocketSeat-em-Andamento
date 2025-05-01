## 23/04

Hoje vimos a diferença de banco de dados nosql para sql, onde a principal diferença é: Bancos de dados SQL são ideais para aplicações que exigem transações complexas e garantem a integridade dos dados, enquanto bancos de dados NoSQL são mais adequados para lidar com grandes volumes de dados não estruturados, permitindo maior flexibilidade em sua utilização. Adionamos uma nova lib ao pip `pylint`.


## 24/04

Hoje, adicionamos novas bibliotecas ao nosso módulo: pytest, dotenv e pymongo. Implementamos um gerenciador de conexão com o banco de dados MongoDB utilizando o pymongo. Além disso, criamos um repositório de pedidos (OrdersRepository) com quatro métodos: um para inserir um pedido (documento), outro para inserir vários pedidos (documentos), um para selecionar vários pedidos (documentos) e um para selecionar apenas um pedido (documento). Também realizamos testes unitários com o pytest, utilizando os quatro métodos do OrdersRepository.


## 28/04

Hoje, implementamos novos métodos de seleção, edição e exclusão no OrdersRepository. Os métodos adicionados foram:

select_many_with_properties: Este método não retornará os documentos que tiverem valores iguais a 0 (inteiro) nas propriedades especificadas na consulta.

select_if_property_exists: Como o nome sugere, este método retorna os documentos que possuem o campo especificado.

select_by_object_id: Este método permite selecionar um documento com base no seu _id. Utilizamos o bson para realizar consultas no MongoDB.

edit_registry: Com o operador "$set", conseguimos atualizar um campo específico em um documento. É possível acessar campos dentro de objetos, por exemplo: {"itens.pizza.tipo": "Frango-Catupiry"}.

edit_many_registries: Este método permite realizar várias edições em documentos de uma só vez.

edit_registry_with_increment: Com este método, conseguimos incrementar valores em nossos documentos no MongoDB utilizando o operador "$inc". Ele permite incrementar tanto inteiros quanto floats.

delete_registry: Este método permite deletar um item específico da tabela, após realizar uma seleção.

delete_many_registries: Com este método, é possível deletar múltiplos itens da tabela de uma só vez.

Além disso, realizamos testes unitários, incluindo o teste para o método insert_document.


## 29/04

Hoje finalizamos os testes unitários utilizando o mock find, onde testamos a função select_many_with_properties. Em seguida, criamos um arquivo de interface para o nosso repositório. Também desenvolvemos a aplicação principal usando uma nova biblioteca, o Flask, onde registramos nossas rotas. Até agora, registramos apenas uma nova rota para testar a conexão.


## 30/04

Não vamos utilizar o padrão convencional de Model, View e Controller. Em vez disso, vamos adotar a arquitetura de User Case para o nosso projeto."


## 01/05

Hoje finalizamos o módulo 10.
Fizemos as seguintes implementações:
Adicionamos a classe RegistryOrder, que agora retorna respostas HTTP, assim como fizemos com RegistryFinder e RegistryUpdater.
Estabelecemos a conexão com o nosso banco de dados MongoDB antes da inicialização do servidor.
Tornamos a classe DBConnectionHandler privada, exportando apenas o objeto que a instancia.
Implementamos os composers para cada rota do projeto: registry_find_composer, registry_order_composer e registry_updater_composer.
Criamos nossos próprios erros personalizados, NotFound e Unprocessable, juntamente com o controlador para gerenciá-los.
Passamos a utilizar o pacote Cerberus, que nos permite validar o corpo da requisição e o tipo de dados que o usuário fornece. Essa validação foi aplicada nas rotas registry_order e registry_update.
Realizamos testes unitários para ambas as rotas.
No total, existem três tipos de rotas neste projeto: registry_order, que cria pedidos; registry_finder, que busca pedidos utilizando o ID; e registry_updater, que atualiza pedidos.