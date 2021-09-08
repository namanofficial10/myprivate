from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Firefox(executable_path = 'C:\\Users\\DELL\\InstaPy\\assets\\gecko\\v0.29.1\\geckodriver-v0.29.1-win64\\geckodriver.exe')



day = int(input("Enter Day: "))

tt = pd.read_excel("class.xlsx", sheet_name=f"{day}")

mail = "https://mail.google.com/mail/u/0/#inbox"
driver.get(mail)

print('''
Please login and also open meet.google.com and give peermissions.
''')
yn = input("Please login and enter any key: ")
del yn

for i in range(7):
    cp = tt.iloc[i,0]
    print(type(tt.iloc[i,0]))


    if cp == 0:
        time.sleep(3300)
        continue
    elif cp == 1:
        url = "https://classroom.google.com/u/0/c/MzgzNzE1NDU2NTQ2"
    elif cp == 2:
        url = "https://classroom.google.com/u/0/c/MzE5ODA1Mzk0NjI4"
    

    driver.get(url)
    time.sleep(15)

    a = driver.find_element_by_css_selector("a.tnRfhc")

    clink = a.get_attribute("href")

    driver.get(clink)

    time.sleep(20)

    cm = driver.find_elements_by_css_selector("div.oTVIqe")

    cm[0].click()
    cm[2].click()

    jn = driver.find_elements_by_css_selector("span.NPEfkd")[0]

    # print("Element Found")
    time.sleep(30)


    jn.click()

    time.sleep(600)

    driver.get(url)
    time.sleep(15)

    a = driver.find_element_by_css_selector("a.tnRfhc")

    clink = a.get_attribute("href")

    driver.get(clink)

    time.sleep(20)

    cm = driver.find_elements_by_css_selector("div.oTVIqe")

    cm[0].click()
    cm[2].click()

    jn = driver.find_elements_by_css_selector("span.NPEfkd")[0]

    # print("Element Found")
    time.sleep(30)


    jn.click()

    time.sleep(300)

    driver.get(url)
    time.sleep(15)

    a = driver.find_element_by_css_selector("a.tnRfhc")

    clink = a.get_attribute("href")

    driver.get(clink)

    time.sleep(20)

    cm = driver.find_elements_by_css_selector("div.oTVIqe")

    cm[0].click()
    cm[2].click()

    jn = driver.find_elements_by_css_selector("span.NPEfkd")[0]

    # print("Element Found")
    time.sleep(30)


    jn.click()

    time.sleep(2350)

    print(f"Class Joined - lecture {i+1} - class {cp}")

    


driver.close()
