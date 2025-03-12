# ponderada-prog_m9s5
Este serviço simula um processo de integração entre um sistema de pedidos e um sistema de pagamentos utilizando API REST. O objetivo é garantir que, sempre que um pedido for criado, ele seja automaticamente enviado para processamento de pagamento, e o resultado seja armazenado no sistema.


## a) Identificar e descrever a estrutura de integração, indicando camadas, módulos, componentes, serviços, hardware, software, processos 

### Estrutura da Integração

#### Camadas e Componentes
1. **Camada de Apresentação**
    - Aplicação cliente

2. Camada de Serviço
    - Serviço de Pedidos
    - Serviço de Pagamento

3. Camada de Comunicação
    - API REST
    - Protocolo HTTP/HTTPS

4. Camada de Infraestrutura
    - Banco de Dados
    - Servidor em cloud

#### Fluxo de Integração
1. O usuário faz um pedido no sistema.

2. O serviço de pedidos registra o pedido e chama o serviço de pagamento.

3. O serviço de pagamento processa o pagamento e retorna o status.

4. O serviço de pedidos atualiza o banco de dados com o resultado.

A troca de informações entre esses dois sistemas separados via API REST caracteriza a integração, unindo o serviço de pedidos com o de pagamento.

## b) Mostrar como documentar e codificar o controle de qualidade de integração. O controle deve incluir tempos, protocolos, versões e tratamento de exceções. 