# Job_Recommender

### This is a job recommender written in python for Taiwanese. 
Well, I always wanted to be a researcher of Social Science before 20yo, then I became a heat transfer sales representative (never even knew this exist). Now I am trying to be a data analyst/engineer. I guess there will always be jobs you never knew but actually fits you well!

## Introduction

### Data Source
Information of jobs were scrapped from www.104.com.tw. It contains 167,730 different jobs from the website.

### Data Processing
[CKIP](https://github.com/ckiplab/ckiptagger) was used to do text segmentation. For this project, it works better than Jieba, as the data is in Traditional Chinese, but also significantly slower.

### Model
[gensim Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) was used to convert CKIPed information of jobs into eigenvectors.

### LinkedIn Crawler
The recommender can scrape information from LinkedIn as the source of your resume.
The crawler use [Selenium](https://github.com/SeleniumHQ/selenium)(chrome version) to get data from LinkedIn.

### Files Needed
To use the recommender, the following files will be needed. Please download them and put them in the same folder with Job_Recommender.py.
1. [chromedriver.exe](https://drive.google.com/file/d/1N0x8tB1Hduht4S_5od2i7xp902VYatgy/view?usp=sharing) This is required by Selenium to run LinkedIn crawler.
2. [Doc2Vec_104_jobs.model](https://drive.google.com/file/d/1bwyV-SA4NgVY7Zbm7owhB77MpTzcOMLc/view?usp=sharing) This is the model for recommendation.
3. [data](https://drive.google.com/drive/folders/18MN0Bqm6Awc4AZHSF2biQW2T_mykRySW?usp=sharing) This is the models and data for CKIP. We need this to do segmentation on your resume.
4. [s104_textCombined_seg_0730.csv](https://drive.google.com/file/d/1BwZRwm4b-QGbJW_ilpx81wR-B9f1V6Pv/view?usp=sharing) This is the data of 167730 jobs scrapped from 104. The file is used to provide information of jobs recommended.

## Usage
Run
```
python Job_Recommender.py
```
The recommender will suggest 3 jobs according to the resume you provide. 

After starting the recommender, you can either 
1. copy-paste/type your resume into the input block
2. let the recommender get information from your LinkedIn profile. Please note that LinkedIn requires the user to login to view profiles, so username and password will be needed.  
