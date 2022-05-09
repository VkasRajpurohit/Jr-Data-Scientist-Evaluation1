*Jr. Data Scientist | Evaluation 1*
-
---

Installing
-
For the web application [Review - Ratings](link), the code is written in python 3.9, please check [runtime.txt](link) for python version information.

- Create new environment.
- Install all the required packages and libraries using below command -  
```bash
pip install -r requirements.txt
```


# PART1

---
Part 1 Q1 :
-
---
### Write a regex to extract all the numbers with orange color background from the below text in italics.

```bash
data = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
```
**Solution** - Wrote a class with exception handling. For code, please click here [Part1 Q1](part1Q1link)




Part 1 Q2 :
-
---

### Here’s the list of reviews of Chrome apps - scraped from Playstore.  [DataSet Link](https://drive.google.com/file/d/1SuiFw4MYxOBlqsRgyXLfch28-gzx8bX6/view)

```python
## Problem Statement 

There are times when a user writes **Good, Nice App or any other positive text**, in the review and gives 1-star rating. 
- Your goal is to identify the reviews where the semantics of review text does not match rating. 

- Your goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. 

- Deploy it using - Flask/Streamlit etc and share the live link. 

## Important
In this data app - the user will upload a csv and you would be required to display the reviews where the content doesn’t match ratings. This csv will be in the same format as the DataSet Link


Bonus Points - If you deploy the app with Authentication. 
```

**Solution** - Built a web application for **Review - Ratings**. User will upload a csv file and hit Process file. It will show result in table with columns - Row indices, Text, Positive review & 1-star rating.

###Tools & Technology used: 

```
- Python | Flask-API | HTML | AWS S3 Bucket
- OS : Windows
- git : GitHub
- IDE : PyCharm
- Also, maintaining logs
```
## Useful links

### GitHub Folder - [app.py](git)

### Deployed link - [Review - Ratings](uploading soon)

  
- Demo model **deployed with Heroku**, different-different cloud platforms have different-different requirement files.
- For Heroku, need files mentioned below -
  - Procfile : Contains the command to run the flask application once deployed on the server.
    ```python
    web: gunicorn main:app
    ```
  - Create a requirements.txt using below command -
    ```python 
    pip freeze > requirements.txt
    ```
  - Create a runtime.txt using below command -  
    ```python
     python-3.9.7
     ```

Heroku Deployment Steps:
-
---
![img_1.png](imgs\img_1.png)
-
---




Demo Screen-Shot
-
---
#### Home-page
![Home-page.png](imgs\img.png)

#### Result-page
![img_5.png](imgs\img_5.png)

---

Demo Video
-
---
https://www.youtube.com/watch?v=VweY5Y37BNk
---



Part 1  Q3 :
-
---
Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute. Here’s the [dataset](https://drive.google.com/file/d/1yuDyU7EjJ8Nai83FDdIF2w4inm17NzBF/view). 
-
**Solution**  - For better understanding the co-relation among the variables, written a module, in this first preprocessed the data & then visualized with heatmap using Spearman's rank correlation coefficient. For code & heatmap, please click here [Part1 Q3](part1Q3link)

```python
# Self written module
from preprocessor import DataPreprocessing
from preprocessor import DisplayCorrelation
```
- For module code, please click here [preprocessor](link)

## Suggested Questions:

---
### 1. Is there any co-relation between short description, long description and ranking? Does the placement of keyword (for example using a keyword in the first 10 words - have any co-relation with the ranking)?

- Short Description & Long Descriptions are the most negatively correlated with each other.
- Short Description do not have a significant monotonically correlation with Rank.
- Rank & Keyword are weak monotonically negatively correlated, using a keyword in the first 10 words would not have a significantly major monotonically correlation with Rank, however it will impact somewhat negatively correlated.


### 2. Does App ID (Also known as package name) play any role in ranking?  

- Rank is most positively correlated with App ID among all the features, these are significantly positivey corrrelated with each other and change in one will significantly change other i.e. increment in App ID will increase Rank.


### 3. Any other pattern or good questions that you can think of and answer?

- What are the most negatively correlated features??
  - Short Description & Long Descriptions.
  - These are the most negatively correlated features, this may be becuase of these are sentiment based.


# PART 2

---
## Part 2  Q1 :

## Check if the sentence is Grammatically correct: 

- Please use any pre-trained model or use text from open datasets. 
- Once done, please evaluate the English Grammar in the text column of the below dataset.
- [DataSet Link](https://drive.google.com/file/d/1LTI5KNqPrtxrYRgJk2AxI30KgYyNcRpD/view)


**Solution**  - For the task, used [language-tool-python](https://pypi.org/project/language-tool-python/). It checks all the english grammar & spelling rules and correct them. First checked, if sentence is correct or not & assigned it as a new column, then given data for correction & assigned this data to a new column and showed the difference. For the code, please click here [Part2 Q1](link)

# Question:

---
### Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution).

- I have observed personally, people are good at programming, however sometimes lagging in understanding the business.
- In one of our project, at the initial stage we were facing problem to understand the business and to get start with the solution, at that time I have created & represented HLD, LLD and Wireframe with all my related research, after getting approval we started working on it.
- This is one of the incident, I have contributed in so many such scenarios.