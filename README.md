# Táxi Autônomo

Projeto acadêmico de Estrutura de Dados e Programação

Autores: 
Fabio Gustavo Gomes Vaz,
Felipe Fernandes Rojas,
Henrique Sanchez Fraga.

Contextualização: Nosso projeto consiste em uma simulação de táxi autônomo, 
como alternativa de transporte individual, a preço subsidiado para pessoas 
de baixa renda ou grupos sociais específicos (ex.: pessoas com deficiência 
e idosos) que coletaria e forneceria dados sobre o trânsito em tempo real. 
O jogo simula uma situação de trânsito urbano, com o táxi ocupando o lugar 
do Pac-Man. O labirinto é composto por ruas com divisórias, com mão e contra-mão,
e o agente evita os fantasmas (congestionamentos e colisões com outros 
veículos e pedestres). O código original do Pac-Man foi desenvolvido por nosso
professor, Jefferson de Oliveira Silva.

Questão Dirigida: Como o famoso jogo Pac-Man pode ser alterado a fim de 
representar ruas, simular o trânsito urbano e controlar o funcionamento de um 
táxi autônomo?

Limitações e melhorias futuras: O agente ainda não sabe diferenciar mão e 
contramão e não consegue identificar outros possíveis obstáculos além de 
veículos. A partir do algoritmo A*, com funções mais rígidas de caminho, o táxi 
poderia percorrer mão e contramão da forma correta, e com informações de 
câmeras externas ao agente, identificar pedestres, buracos, animais e outros que
inviabilizam o trânsito automático. Com essas informações, o agente receberia
ordens de freio crescente (sem freadas bruscas, a não ser que o "fantasma" 
esteja muito próximo, o que o algoritmo saberia medir).

Conclusão: A simulação do trânsito como labirinto viabilizaria tranquilamente
o funcionamento de um veículo autônomo, com uma direção segura e que saiba 
identificar obstáculos com muita eficiência, priorizando segurança ao invés de
velocidade. Algoritmos que impedem colisões são muito poderosos neste quesito.
As movimentações do agente (por padrão, o Pac-Man) permitem que o veículo vagueie
sem rumo, pare, percorra um ou mais destinos pré-definidos ou aleatórios e não
colida com fantasmas, sendo uma ferramenta muito poderosa para a representação 
do trânsito.
