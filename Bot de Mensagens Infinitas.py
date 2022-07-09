import pyautogui as spam
import time

limite_msg = input("Numero de Mensagens: ")
msg = input("Mensagem: ")

i = 0 

## segundo para iniciar um pouco depois de rodar o programa
time.sleep(2)

while i < int (limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")
    i+=1
