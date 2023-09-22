#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://sigedu.utdt.edu/utdt/principal/login.jsp")

username_field = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[3]/input[2]')
username_field.send_keys("46585843")
password_field = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[3]/input')
password_field.send_keys("140605843")
login_button = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[3]/td/input[1]')
login_button.click()

inscripcion = driver.find_element(By.XPATH, '//*[@id="divMenu_102"]/table/tbody/tr/td/table[1]/tbody/tr/td/a')
inscripcion.click()

buscar = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/form/table[1]/tbody/tr[2]/td/table[3]/tbody/tr[3]/td[2]/a')
buscar.click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
buscar_materia = driver.find_element(By.XPATH, '/html/body/form/input[8]')
buscar_materia.send_keys('Matematica II')


# ??? driver.get('https://sigedu.utdt.edu/utdt/principal/LOV.jsp?Z_FILTER=&Z_CALLER_URL=https%3A//sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp&Z_CONSULTAR=S&Z_TITULO=Datos%20de%20la%20Materia&Z_LABEL=Materia&Z_QUERY=select%20distinct%20id_materia%2C%20des_materia%20from%20%20vw_lov_materias%20c%20where%20n_id_alu_prog%20igual%20142878%20and%20%20%20c_tipo_curso%20igual%20%20%27COMUNES%27%20%20and%20%20%20parentesisAbre%27%27%20is%20null%20or%20seccion%20igual%20%27%27%20parentesisCierra%20and%20%20%20parentesisAbre%27%27%20is%20null%20or%20docente%20like%20%27%25%25%27%20parentesisCierra%20and%20%20%20parentesisAbre%27%27%20is%20null%20or%20dia%20igual%20%27%27%20parentesisCierra%20and%20upperparentesisAbredes_materiaparentesisCierra%20like%20upperparentesisAbre%27%23search%23%25%27parentesisCierra%20%20and%20not%20existsparentesisAbreselect%201%20from%20alumnos_cursos%20ac%20where%20ac.n_id_persona%20igual%20%2783083%27%20%20and%20ac.c_legajo%20igual%20%2723R1764%27%20%20and%20ac.n_curso%20igual%20c.n_curso%20and%20ac.c_ano_lectivo%20igual%20c.c_ano_lectivo%20and%20ac.f_baja%20is%20null%20parentesisCierraorder%20by%20saca_acentosparentesisAbredes_materiaparentesisCierra&Z_OUTCOD=document.F_PPAL.v_id_materia2&Z_OUTDESC=document.F_PPAL.materia')

time.sleep(5)
driver.quit()

