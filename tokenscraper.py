import imp
from pickletools import read_uint1
from pydoc import importfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import discord


#timeframe = float(input("How long do you want the update time frame in min >> "))
#timeframe = timeframe * 60

Address = []
Sol = []


def uniquelistcheck(list1,list2):
    unique_list = []
    unique_list2 = []
    for x,y in zip(list1, list2):
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            unique_list2.append(y)

    # print list
    return unique_list,unique_list2


def Scraper(input):
    
    print("Process Started!")

    #setup
    #Headless
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    op.add_argument('--log-level=3')

    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(options=op)
    #driver = webdriver.Chrome()
    driver.get('https://solscan.io/')

    #search solscan
    search = driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div[2]/div/div/form/span/div[2]/span/input')
    search.send_keys(input)
    search.send_keys(Keys.RETURN)

    #loop each wallet
    for i in range(2,11):

        sleep(4)

        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/table/tbody/tr[' + str(i) +']/td[5]/div/a').click()

        sleep(2)

        Address.append(driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[1]/div[2]/div[2]/div/div/div/div').text)
        tempsol = (driver.find_element_by_xpath('/html/body/div/section/main/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]').text)

        splittemp = tempsol.split()

        Sol.append(splittemp[0])

        driver.back()

        print("Done: " + str(i))

    return uniquelistcheck(Address,Sol)



#print(uniquelistcheck(Address,Sol))
#print("Finished!")


