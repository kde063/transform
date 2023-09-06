from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Tlqkf  djRRkgkwlak
f = open('write.txt','a', encoding = 'UTF-8')
wr = csv.writer(f)

a = 1
b = 0
text_list1 = []
url = 'http://www.cgv.co.kr/movies/detail-view/?midx=87175'
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
links_selector = "#movie_point_list_container > li > div.box-comment > p"
driver.get(url)
while (a<12):
    x = driver.find_element(By.CSS_SELECTOR, '#paging_point > li:nth-child('+str(a)+')').click()
    time.sleep(1)
    links = driver.find_elements(By.CSS_SELECTOR, links_selector) 
    for i in links:
    # print(i.text)
        text_list1.append(i.text)
    print(text_list1[-1])
    a+=1
a = 3
while (a<14 and b < 1):
    x = driver.find_element(By.CSS_SELECTOR, '#paging_point > li:nth-child('+str(a)+')').click()
    time.sleep(1)
    links = driver.find_elements(By.CSS_SELECTOR, links_selector) 
    for i in links:
    # print(i.text)
        text_list1.append(i.text)
    print(text_list1[-1])
    if a == 14:
        b += 1
        a = 2
    a+=1
# url = 'http://www.cgv.co.kr/movies/detail-view/?midx=87175#1'
# driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
# links_selector = "#movie_point_list_container > li > div.box-comment > p"
# driver.get(url)
# links = driver.find_elements(By.CSS_SELECTOR, links_selector)

    
print(text_list1)
for i in text_list1:
    wr.writerow([i])
    # print(i)


f.close()