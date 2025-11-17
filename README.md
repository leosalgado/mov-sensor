# Sistema de Segurança Anti-Invasão

Firmware em MicroPython para ESP32 feito para monitorar um interruptor (slide switch) e disparar um alarme via requisição HTTP quando o interruptor é acionado. Simulação diponível em: **[Wokwi](https://wokwi.com/projects/447136346765274113).**

## Requisitos

- ESP32

- Conexão à internet

- IDE para rodar Micropython no ESP32 (ex: Thonny)

## Utilização

- Troque o SSID e senha para o correspondente à rede desejada.

- Depois da configuração da IDE Thonny com o ESP32 conectado, selecione e rode o arquivo "main.py".

> [!TIP]
> Caso não possua maneira de simular o mecanismo de slide switch, utlizar "botao.py"!

## Vantagens de Utilizar Interrupção em Relação a um Loop Infinito

- **Uso otimizado do processador:** Monitorar eventos sem a necessidade do processador.

- **Menor consumo de energia:** o microcontrolador pode entrar em modo de baixo consumo de energia enquanto não está sendo utilizado.

- **Precisão:** eliminar risco do momento da execução da leitura não sincronizar com sinal de entrada.
