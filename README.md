# Calculadora-Debug-VN
Calculadora que decodifica hex para as informações presentes no KIJO VN


## Descrição dos Código

0008 = 0000 0000 0000 1000

001000000000 - Controle de Secao Ativado (Se pegou o Evento)
000100000000 - Tem Mensagem da Secao vindo na CAN  vindo nos ultimos 5 seg
000010000000 - Alguma secao ligada no vetor de secao
000001000000 - Tem Mensagem do Master/Levante na CAN  vindo nos ultimos 5 seg
000000100000 - Master/Levante esta Plantando!
000000010000 - Existe a Mensagem de Sensores Agrosystem
000000001000 - Algum Sensor de Sementes Caindo Semente nesse momento (sensores Agrosystem)
000000000100 - Tem Mensagem da Populacao da CAN vindo nos ultimos 5 seg
000000000010 - Ta Travada a Populacao na CAN, vindo na CAN porem com mesmo Valor sempre
000000000001 - Tipo de Efetivo que esta sendo usado no momento, ou tipo de saida de efetivo no momento Olhar Tabela abaixo:

Global.tipoEfetivoPlanter = 1; //Saiu Efetivo, Velocidade e Re
Global.tipoEfetivoPlanter = 2; //Saiu Efetivo, Levante/Master
Global.tipoEfetivoPlanter = 3; //Sai do Efetivo de Secao + Populacao
Global.tipoEfetivoPlanter = 4; //Sai do Efetivo de Populacao
Global.tipoEfetivoPlanter = 5; //Sai do Efetivo de Sensores
Global.tipoEfetivoPlanter = 6; //Sai do Efetivo geral

Global.tipoEfetivoPlanter = 7; //Efetivo com Secao + Populacao
Global.tipoEfetivoPlanter = 8; //Efetivo com Populacao
Global.tipoEfetivoPlanter = 9; //Efetivo com Sensores
