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
