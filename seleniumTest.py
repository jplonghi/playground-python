from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options
from getpass import getpass
import pandas as pd
import time

options = Options()
#options.headless = True
options.add_argument("--window-size=800,600")
options.add_argument("--disable-extensions")

usr = input("Usuario: ")
pwd= getpass()
last4 = input("Tarjeta: ")

driver = webdriver.Edge(options=options)
driver.get("https://www1.sucursalelectronica.com/redir/showLogin.go")

usrElement = driver.find_element(By.ID, "productId")
usrElement.send_keys(usr)

pwdElement = driver.find_element(By.ID, "pass")
pwdElement.send_keys(pwd)

btnLogin = driver.find_element(By.ID, "confirm")
btnLogin.click()

time.sleep(2)

driver.get("https://www1.sucursalelectronica.com/ebac/module/accountbalance/accountBalance.go")
driver.find_element(By.ID, "productIdLabel").click()

for i in range(len(driver.find_element(By.ID, "productIdList").find_elements(By.TAG_NAME, "li"))):
    if last4 in driver.find_element(By.ID, "productIdList").find_elements(By.TAG_NAME, "li")[i].text:
        driver.find_element(By.ID, "productIdList").find_elements(By.TAG_NAME, "li")[i].click()
        break
time.sleep(2)

def dayFirstConvert (cell):
    return pd.to_datetime(cell, dayfirst=True)


all_tables = pd.read_html(driver.page_source, attrs={'id': 'creditCardRecentMovementsTable'}, converters={'Fecha': dayFirstConvert})
df = all_tables[0]
#pd.to_datetime(df['Fecha'], dayfirst=True)

df.to_json("mov.json", orient = 'records', date_format='iso', indent=4)

exit = driver.find_element(By.XPATH ,"/html/body/div[1]/div[1]/div[2]/ul/li[3]/a")
exit.click()
driver.close()
