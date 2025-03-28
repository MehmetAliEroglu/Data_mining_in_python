#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#FIRSTLY WE HAVE TO INSTALL SELENIUM
pip install selenium


# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#AT BELOW (WHERE *** LOCATED) YOU HAVE TO PUT YOUR CHROMEDRIVER'S PATH IN LOCAL PC
#(OTHER DRIVERS CAN ALSO BE USED WITH SELENIUM BUT I PREFER CHROME)
service = Service(executable_path = r" *** ")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = options)

driver.get("https://x.com/home?lang=tr")
#IN EARLY VERSIONS OF THE X YOU DON'T HAVE TO ENTER ANY ACCOUNT INFO WHEN YOU TRY TO ENTER BUT NEWER VERSIONS NEED US TO ENTER AN ACCOUNT


# In[ ]:


while True:
    decision = "yes"

    decision = input("To search enter 'yes' or to exit enter 'no': ")
    
    if (decision == "yes" or decision == "Yes" or decision == "YES"):
        fileName = input("Please enter a name for a file name: ")
        
        newData = input("Please enter a key to search: ")
        
        driver.get("https://x.com/search?q=" + newData + "&src=typed_query&f=live")

        time.sleep(2)

        res = []#FOR STORİNG THE EVERY DATA


#-------------------------------WHERE THE GİVEN KEY SEARCHED FROM X-----------------------------------

#The section assigned to the bottom of the page, as vertical scrolling movements are used on the opened page.
        
        last = driver.execute_script("return document.documentElement.scrollHeight")
        counter = 0
        while True:
            if counter > 2 :
                break
            driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            new = driver.execute_script("return document.documentElement.scrollHeight")
            if last == new :
                break
            last = new
            counter += 1
            tweet = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")#FINDING TWEETS USING 'XPATH' 
            time.sleep(2)
            print("------------------------------\n" + str(len(tweet)) + " tweets have been found \n------------------------------")
            for i in tweet:
                res.append(i.text)#ADDING ONLY THE TEXT PART 
        

#WHERE ALL THE DATA STORED IN THE TXT FİLE WITH THE GIVEN NAME
        num = 1
        with open(f"{fileName}.txt","w",encoding = "UTF-8") as file :
            for a in res :
                file.write(f"{num} - {a}\n")
                num += 1
        print("Tweets has been saved successfully with name" + fileName + ".txt")

    else:
        break


# In[ ]:


with open(f"{fileName}.txt", 'r', encoding = "UTF-8") as tweets:
    lines = tweets.readlines()
    for item in lines :
        print(item)

