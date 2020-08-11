# Job_Recommender

### This is a job recommender written in python for Taiwanese.

## Introduction

### Data Source
Information of jobs were scraped from www.104.com.tw. It contains 167,730 different jobs from the website.

### Data Processing
[CKIP](https://github.com/ckiplab/ckiptagger) was used to do text segmentation.

### Model
[gensim Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) was used to convert CKIPed information of jobs into eigenvectors.

### Usage
To use the recommender, run Job_Recommender.py.
LinkedIn.py is to provide the web crawler function.

After starting the recommender, you can either 
1. copy-paste/type your resume into the input block
2. let the recommender get information from your LinkedIn profile. Please note that LinkedIn requires the user to login to view profiles, so username and password will be needed.  
