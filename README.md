# Job_Recommender

### This is a job recommender written in python for Taiwanese.

## Introduction

### Data Source
Information of jobs were scraped from www.104.com.tw. It contains 167,730 different jobs from the website.

### Data Processing
[CKIP](https://github.com/ckiplab/ckiptagger) was used to do text segmentation. For this project, it works better than Jieba, as the data is in Traditional Chinese, but also significantly slower.

### Model
[gensim Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) was used to convert CKIPed information of jobs into eigenvectors.

### LinkedIn Crawler
The recommender can scrape information from LinkedIn as the source of your resume.
The crawler use [Selenium](https://github.com/SeleniumHQ/selenium)(chrome version) to get data from LinkedIn.

## Usage
To use the recommender, run Job_Recommender.py.
The recommender will suggest 3 jobs according to the resume you provide. 

After starting the recommender, you can either 
1. copy-paste/type your resume into the input block
2. let the recommender get information from your LinkedIn profile. Please note that LinkedIn requires the user to login to view profiles, so username and password will be needed.  
