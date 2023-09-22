#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp")

time.sleep(5)
driver.quit()