from machine import Pin
import time
import network
import urequests


def conecta_wifi(ssid, password):
    print("Connecting to WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.1)
    print(" Connected!")


SSID = "Wokwi-GUEST"
PASSWORD = ""
conecta_wifi(SSID, PASSWORD)

PINO_SLIDE_SWITCH = 21
# Bounce desativado no componente
switch = Pin(PINO_SLIDE_SWITCH, Pin.IN, Pin.PULL_UP)
cont = {0: 0}


def manda_sinal():
    try:
        response = urequests.get("https://httpbin.org/get")
        print("Sinal enviado!\nResposta:", response.text)
        response.close()
    except Exception as e:
        print("Erro ao enviar sinal:", e)


def dispara_alarme(pin):
    cont[0] += 1
    print("-" * 45)
    print(f"  ALERTA: O SWITCH FOI ACIONADO PELA {cont[0]}a VEZ!")
    print("-" * 45)
    manda_sinal()


switch.irq(trigger=Pin.IRQ_RISING, handler=dispara_alarme)

print("[SIMULADOR INICIADO]")

while True:
    time.sleep(1)
