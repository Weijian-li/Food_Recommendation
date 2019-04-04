# Food_Recommendation
This repo contains my fun work on building a food recommendation system. It's currently an ongoing project. I'll keep updating it.

## How to use
Currently, we have a preprocessing file for the ta-feng dataset. Since none of the previous work clearly mention the preprocessing steps, we reimplemented the steps to get the same User/Item distribution as they stated in their papers.

## Ta-Feng dataset
Ta-Feng is a grocery shopping dataset released by ACM RecSys, it covers products from food, office supplies to furniture. 
The dataset collected users transaction data of 4 months, from November 2000 to February 2001. The total count of transactions in this dataset is 817741, which belong to 32266 users and 23812 products. (http://www.bigdatalab.ac.cn/benchmark/bm/dd?data=Ta-Feng)

The original dataset link is disappeared, so we use the dataset in this link: https://sites.google.com/site/dataminingcourse2009/spring2016/annoucement2016/assignment3/D11-02.ZIP

We merged all four transaction files into a single one by simply concatenating them together. Headers of each file are removed. The concatenated data file is the input to the preprocessing file. The preprocessing takes several runs. So we need to feed the output file in last step as the input file in this step. This can be done by changing the input file path in the first few lines. After the preprocessing, we will get our data that contains 9238 users and 7973 items.
