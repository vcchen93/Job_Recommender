#!/usr/bin/env python
# coding: utf-8

# In[44]:


import getpass
import pandas as pd
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def linkedin_crawler(url,uname,pword):
    

    
    #開啟chrome driver
    driver = webdriver.Chrome('chromedriver')        
    
    #抓下來的資料存df
    df = pd.DataFrame(columns=['Location','About',                               'Position_1', 'Location_Employed_1', 'Job_Description_1',                               'Position_2', 'Location_Employed_2', 'Job_Description_2',                               'Position_3', 'Location_Employed_3', 'Job_Description_3',                               'School_Name_1', 'Degree_Name_1', 'Degree_Description_1',                                'School_Name_2', 'Degree_Name_2', 'Degree_Description_2',                                'School_Name_3', 'Degree_Name_3', 'Degree_Description_3',                                'Certification_Name_1', 'Certification_Auth_1',                               'Certification_Name_2', 'Certification_Auth_2',                               'Certification_Name_3', 'Certification_Auth_3',                               'Skill_1', 'Skill_2', 'Skill_3'])

    
    driver.get('https://www.linkedin.com/')
    username = driver.find_element_by_name('session_key')
    username.send_keys(uname)
    sleep(0.2)
    password = driver.find_element_by_name('session_password')
    password.send_keys(pword)
    sleep(0.2)
    password.send_keys(Keys.RETURN)
    sleep(2)
    
    
    driver.get(url)
    sleep(1)

    #讓他滾7下，資訊才會都顯示
    for i in range(9):
        driver.execute_script("var action=document.documentElement.scrollTop={}".format(i*400))
        sleep(0.1)
        
    sel = Selector(text = driver.page_source)

    #Location
    try:
        location = ' '.join(sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first().split())
        df.loc[0,'Location'] = location
        #print(location)
    except Exception as e:
        #print(e)
        location = None

    #About
    try:
        about_button = driver.find_element_by_id('line-clamp-show-more-button')
        driver.execute_script("arguments[0].click();", about_button)
        sel = Selector(text = driver.page_source)
        about = sel.xpath('//*[@class = "lt-line-clamp__raw-line"]/text()').extract()
        about = ' '.join(about)
        df.loc[0,'About'] = about
        #print(about)
    except Exception as e:
        #print(e)
        about = None

    #Experience-Section
    for i in range(1,4):
        try:
            position = sel.xpath('(//section[@id = "experience-section"]//section)[{}]//*[@class = "t-16 t-black t-bold"]/text()'.format(i)).extract_first()
            df.loc[0,'Position_{}'.format(i)] = position
            #print(position)
        except Exception as e:
            #print(e)
            position = None

        try:
            loc_employed = sel.xpath('(//section[@id = "experience-section"]//section)[{}]//*[contains(@class,"pv-entity__location")]//span/text()'.format(i)).extract()[1]
            df.loc[0,'Location_Employed_{}'.format(i)] = loc_employed
            #print(loc_employed)
        except Exception as e:
            #print(e)
            loc_employed = None

        try:
            description = sel.xpath('(//section[@id = "experience-section"]//section)[{}]//*[contains(@class,"pv-entity__description")]/text()'.format(i)).extract()
            description = ' '.join(description)
            df.loc[0,'Job_Description_{}'.format(i)] = description
            #print(description)
        except Exception as e:
            #print(e)
            description = None

    #print('-----------------------------')        

    #Education-Section
    for i in range(3):

        try:
            school_name = sel.xpath('//*[contains(@class,"pv-entity__school-name")]/text()').extract()[i]
            df.loc[0,'School_Name_{}'.format(i+1)] = school_name
            #print(school_name)
        except Exception as e:
            #print(e)
            school_name = None

        try:
            degree_name = sel.xpath('(//*[contains(@class,"pv-entity__secondary-title pv-entity")])[{}]/span[@class="pv-entity__comma-item"]/text()'.format(i+1)).extract()
            degree_name = ' '.join(degree_name)
            df.loc[0,'Degree_Name_{}'.format(i+1)] = degree_name
            #print(degree_name)
        except Exception as e:
            #print(e)
            degree_name = None    

        try:
            degree_description = sel.xpath('(//*[contains(@class,"pv-entity__description")])[{}]/text()'.format(i+1)).extract()
            degree_description = ' '.join(degree_description)
            df.loc[0,"Degree_Description_{}".format(i+1)] = degree_description
            #print(degree_description)
        except Exception as e:
            #print(e)
            degree_description = None

    #Certifications-Section
    for i in range(1,4):
        try:
            cert_name = sel.xpath('(//section[@id = "certifications-section"]//li)[{}]//*[@class = "t-16 t-bold"]/text()'.format(i)).extract_first()
            df.loc[0,'Certification_Name_{}'.format(i)] = cert_name
            #print(cert_name)
        except Exception as e:
            #print(e)
            cert_name = None    

        try:
            cert_auth = sel.xpath('(//section[@id = "certifications-section"]//li)[{}]//*[@class = "t-14"]/span/text()'.format(i)).extract()[1]
            df.loc[0,'Certification_Auth_{}'.format(i)] = cert_auth
            #print(cert_auth)
        except Exception as e:
            #print(e)
            cert_auth = None    

    #Skills-Section
    for i in range(1,4):
        try:
            skill = sel.xpath('(//*[@class = "pv-skill-category-entity__name-text t-16 t-black t-bold"])[{}]/text()'.format(i)).extract()
            skill = ''.join(skill[0].split())
            df.loc[0,'Skill_{}'.format(i)] = skill
            #print(skill)
        except Exception as e:
            #print(e)
            skill = None    
                    
    driver.quit()
    
    df = df.astype('str')
    text = df.apply(' '.join, axis=1)[0]
    
    return text


# In[45]:


if __name__ == '__main__':
    linkedin_crawler(url,uname,pword)

