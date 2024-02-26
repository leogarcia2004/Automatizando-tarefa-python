

import pyautogui 
import time 

pyautogui.PAUSE = 1 

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

time.sleep(3) 

pyautogui.click(548, 370)

pyautogui.write("pessoa_aleatoria@hotmail.com")

pyautogui.press("tab") 

pyautogui.write("123456")

pyautogui.click(x=676, y=534)
time.sleep(3)

import pandas 

tabela = pandas.read_csv("produtos.csv") 

for linha in tabela.index:

    pyautogui.click(x=444, y=262) 

    codigo = tabela.loc[linha, "codigo"] 

    pyautogui.write(str(codigo))
    pyautogui.press("tab") 
    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab") 
   
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "categoria"])) 

    pyautogui.press("tab") 
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab") 
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab") 
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): 
        pyautogui.write(obs)  
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)