#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().system(' pip install selenium')


# In[33]:


pwd


# In[37]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:/Users/JM' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)

url = "https://hello-ming.tistory.com/"
driver.get(url)


# In[53]:


from selenium import webdriver
import datetime
# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:/Users/JM' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(1)
driver.get('https://extranet.mandieselturbo.com/garmlod/')
driver.implicitly_wait(1)


# In[61]:


import requests

# 로그인 정보
LOGIN_URL = '<https://loginpartner.man-es.com>'
USERNAME = 'jimyeung@hhi.co.kr'
PASSWORD = 'Chlwlaud1561@'

# 세션 유지
session = requests.Session()

# 로그인 요청
login_data = {
    'username': USERNAME,
    'password': PASSWORD
}
response = session.post(LOGIN_URL, data=login_data)

# 로그인 정보 유지
if response.status_code == 200:
    print('로그인 성공')
else:
    print('로그인 실패')

# 크롤링
CRAWLING_URL = '<https://example.com/crawling>'
response = session.get(CRAWLING_URL)

# HTML 출력
print(response.content)


# In[60]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:/Users/JM' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)

chrome_path = "...\\chromedriver_win32\\chromedriver.exe"
url_login = "https://loginpartner.man-es.com/adfs/ls/?SAMLRequest=fdBNT8MwDAbgv1Llno%2BmgYWorTRpl0lwAcSBC%2FLadKvUJF2cCsSvJ3QgsQtHv9Zjy64R3CRns13SyT%2Fa82IxFR9u8mgunYYs0ZsAOKLx4Cya1Jmn7cO9kUyYOYYUujCRv%2BZ%2FAog2pjF4Uux3DXnTAgYptKXiVguqbAn07iA1HXK8UQJ0JSUpXmzEbBqSR2SIuNi9xwQ%2B5UjIiooNLfVzKU1VGqVYdSPVplKvpNjli0YPadWnlGY0nE%2FhOPoZYvI2MgeeWmRdcBz6AfmEnLT1eopZN8X21x0hOjrTkHpkrqdZssP4yb%2Frd7xMrfmV%2FCmvP9x%2BAQAAAAAAAAAAAAAAAA%3D%3D&RelayState=ReturnUrl%3Dhttps%253A%252F%252Fextranet.mandieselturbo.com%252Fgarmlod%252F&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=C9arCae%2FyCfKCXiEP5xhryJnAB%2BXvEQXIMidlWdkIWKarZqyiD0nwDpwvMSWlI3x%2BGnHDUWmjpUBjr%2B3iwWSuFaTjUv2w8Rp0CRh6YN92EtnYlYtmnFDcIho8EU7wD2jsFeGGBMihzS1yKtwc4kCMUmGOEAbzc3wBEdSqUBCl7spRNax7UviCzDRes9XjHwaAwkfEVi%2BfestVKqVSZh7Y%2F%2F2JN9vhcQ7e%2FwqjBPwH3GY0h0rLsr%2F1XkUCvw3xkuTMLzJKnmqsPTX%2BAKB9Wt0LP6ofCM3qVZKol07jbjhrIXpmY1fUolUENtFYxhmhxaGQ8YmnKcZFFMZAKHJRU%2FUxg%3D%3D&client-request-id=71a4076c-c233-4ab8-2b02-0080020000d7&RedirectToIdentityProvider=AD+AUTHORITY"
url_shopping = "https://extranet.mandieselturbo.com/garmlod/"

driver.get(url_login)
time.sleep(1)

# id, pw 입력할 곳을 찾기
tag_id = driver.find_element_by_name('<input id="userNameInput" name="UserName" type="email" value="" tabindex="1" class="text fullWidth" spellcheck="false" placeholder="E-Mail" autocomplete="off">')
tag_pw = driver.find_element_by_name('<input id="passwordInput" name="Password" type="password" tabindex="2" class="text fullWidth" placeholder="비밀번호" autocomplete="off">')
tag_id.clear()
tag_pw.clear()
time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy('jimyeung@hhi.co.kr')
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy('Chlwlaud1561@')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element_by_id('log.login')
login_btn.click()

#바로 하면 페이지 이동이 안될 수 있다.
time.sleep(3)

#쇼핑페이지 데이터 가져오기
driver.get(url_shopping)

#쇼핑목록 출력 
products = driver.find_elements_by_css_selector("p.name")

for product in products:
    print("-", product.text)


# In[51]:


pip install pyperclip


# In[57]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:/Users/JM' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
chrome_path = "...\\chromedriver_win32\\chromedriver.exe"
url_login = "https://nid.naver.com/nidlogin.login"
url_shopping = "https://order.pay.naver.com/home?tabMenu=SHOPPING"

driver.get(url_login)
time.sleep(1)

# id, pw 입력할 곳을 찾기
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()
tag_pw.clear()
time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy('내id')
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy('내비밀번호')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element_by_id('log.login')
login_btn.click()

#바로 하면 페이지 이동이 안될 수 있다.
time.sleep(3)

#쇼핑페이지 데이터 가져오기
driver.get(url_shopping)

#쇼핑목록 출력 
products = driver.find_elements_by_css_selector("p.name")

for product in products:
    print("-", product.text)


# In[66]:


from selenium import webdriver
import datetime

# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:\Chrome_Driver\chromedriver.exe' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(1)
driver.get('https://loginpartner.man-es.com/adfs/ls?wa=wsignin1.0&wtrealm=urn%3aNexusR2&wctx=https%3a%2f%2fextranet.mandieselturbo.com%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F&client-request-id=1f6c5197-11be-4d69-d01e-0080020000e2&RedirectToIdentityProvider=AD+AUTHORITY')
driver.implicitly_wait(1)


# In[81]:


from selenium import webdriver
import datetime
from time import sleep
# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:\Chrome_Driver\chromedriver.exe' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(1)
driver.get('https://loginpartner.man-es.com/adfs/ls?wa=wsignin1.0&wtrealm=urn%3aNexusR2&wctx=https%3a%2f%2fextranet.mandieselturbo.com%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F&client-request-id=1f6c5197-11be-4d69-d01e-0080020000e2&RedirectToIdentityProvider=AD+AUTHORITY')
driver.implicitly_wait(4)

time.sleep(1)
driver.find_element_by_name('userNameInput').send_keys('jimyeung@hhi.co.kr')
time.sleep(1)
driver.find_element_by_name('passwordInput').send_keys('Chlwlaud1561@')


# In[116]:


from selenium import webdriver
import datetime
from time import sleep
from selenium.webdriver.common.by import By
import openpyxl
import time
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd


# WebDriver의 경로를 설정합니다.
webdriver_path = 'C:\Chrome_Driver\chromedriver.exe' # 여기에는 실제 chromedriver가 위치한 경로를 넣으세요.

# WebDriver를 초기화합니다.
s=Service(webdriver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(1)
driver.get('https://loginpartner.man-es.com/adfs/ls?wa=wsignin1.0&wtrealm=urn%3aNexusR2&wctx=https%3a%2f%2fextranet.mandieselturbo.com%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F&client-request-id=1f6c5197-11be-4d69-d01e-0080020000e2&RedirectToIdentityProvider=AD+AUTHORITY')
driver.implicitly_wait(1)

# id, pw 입력할 곳을 찾기
tag_id = driver.find_element(By.ID,"userNameInput")
tag_pw = driver.find_element(By.ID,"passwordInput")
tag_id.clear()
tag_pw.clear()
time.sleep(1)
# id 입력
tag_id.click()
pyperclip.copy('jimyeung@hhi.co.kr')
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy('Chlwlaud1561@')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element(By.ID,"submitButton")
login_btn.click()

#바로 하면 페이지 이동이 안될 수 있다.
time.sleep(3)

#LOD 페이지 이동
driver.get('https://extranet.mandieselturbo.com/garmlod/')
time.sleep(3)

##HTTP GET Request
req=requests.get("https://extranet.mandieselturbo.com/garmlod/")
soup =BeautifulSoup(req.text,"html.parser")
data=soup.find("tabel",{'class':"mat-table cdk-table mat-sort table table-bordered"})
print(table)


# In[119]:


##HTTP GET Request
req=requests.get("https://extranet.mandieselturbo.com/garmlod/")
soup =BeautifulSoup(req.text,"html.parser")
data=soup.find("tabel",{'class':"mat-table cdk-table mat-sort table table-bordered"})
print(table)


# In[102]:


pip install openpyxl


# In[105]:


pip install selenium


# In[106]:


pip install requests


# In[107]:


pip install bs4


# In[108]:


pip install html_table_parser

