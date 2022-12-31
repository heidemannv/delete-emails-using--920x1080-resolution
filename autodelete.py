import pyautogui
import sys
import time
import msvcrt
import random
import time
import os


# Dá os cliques para abrir a extensão e o jogo de cartas.
def abrirGmail():
    pyautogui.click(282, 188)
    time.sleep(1)
    pyautogui.click(430, 187)


def pararPrograma():
    timeout = 4
    startTime = time.time()
    inp = None
    print("Aperte qualquer tecla para continuar ou aguarde 4 segundos.")
    while True:
        if msvcrt.kbhit():
            inp = msvcrt.getch()
            break
        elif time.time() - startTime > timeout:
            break
    if inp:
        sys.exit()
    else:
        parar = False


def clear(): return os.system('cls')  # Para limpar o console.

# Daqui pra frente é o programa funcionando.


print("Abra o Gmail e deixe a janela em tela cheia. O programa iniciará em 5 segundos.")
time.sleep(5)
parar = False
while parar == False:
    abrirGmail()
    pararPrograma()
