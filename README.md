## 23/04

Hoje vimos a diferença de banco de dados nosql para sql, onde a principal diferença é: Bancos de dados SQL são ideais para aplicações que exigem transações complexas e garantem a integridade dos dados, enquanto bancos de dados NoSQL são mais adequados para lidar com grandes volumes de dados não estruturados, permitindo maior flexibilidade em sua utilização. Adionamos uma nova lib ao pip `pylint`.


## 24/04

Hoje, adicionamos novas bibliotecas ao nosso módulo: pytest, dotenv e pymongo. Implementamos um gerenciador de conexão com o banco de dados MongoDB utilizando o pymongo. Além disso, criamos um repositório de pedidos (OrdersRepository) com quatro métodos: um para inserir um pedido (documento), outro para inserir vários pedidos (documentos), um para selecionar vários pedidos (documentos) e um para selecionar apenas um pedido (documento). Também realizamos testes unitários com o pytest, utilizando os quatro métodos do OrdersRepository.