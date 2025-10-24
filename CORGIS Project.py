#!/usr/bin/env python
# coding: utf-8

# # CORGIS Paper Summary and Project by Naufal Alavi

# Paper Summary:
#     
#     CORGIS is a library of data sets that was developed to cater to the needs of data science students from various disciplines at the introductory level. CORGIS’ incubation process involved the use of educational theory, particularly the MUSIC model of academic motivation which differentiates between a student’s situational interest and their perceived usefulness of what they’re doing. It also involves the calculation of appropriate successes, the sense of empowerment achieved through those successes as well as the level of care in instructors towards their students. CORGIS operates in a similar way to the RealTimeWeb project where the data is being constantly updated, with the difference being that CORGIS provides a large collection of local data sets rather than a small collection of web-based ones. CORGIS provides multiple data sets for each major academic discipline, and it is organized in a very efficient manner into language libraries, visualizers, explorers, raw data files and the CORGIS gallery. The data sets allow for a great deal of exploratory and large-scale data analysis. In addition, CORGIS provides practice problems for students in the context of its data sets, and also allows for data mapping. When this paper was written, the CORGIS library had over 40 data sets. In general, numeric and string types are the most frequent classes of variables in these data sets. CORGIS was utilized in a computational thinking course for non-computer science majors with 50 students, and a survey done after the course revealed correlations between students’ interest in learning about real-world data in their respective fields and desire to continue learning computing in the future. While CORGIS is an appreciable effort to provide useful data sets to introductory computing students, there needs to be a lot of further research done on the motivation and learning of students in order to improve this library. All CORGIS data sets are currently open access, and the creators want to explore the possibility of generating artificial data sets that are based on previous knowledge and patterns of real-world data sets. However, further research needs to be done to conclude if this is technically viable. 

# In[1]:


import graduates
grad_major = graduates.get_grad_major()
grad_major

'''This dataset contains information about employment numbers and salaries based on students' majors.
Some of the key categories in the dataset are year, education major, highest and lowest salaries, and employment
numbers. I chose this dataset because as a college student, this information is extremely relevant and useful for me
while choosing career paths. An analysis of this dataset can give me crucial insight into what I could expect 
in the future with my major, which majors earn the highest salaries and which markets are saturated. As seen below, 
the dataset is formatted as a list of dictionaries, in which year, demographics, education, salaries, and employment are
the main 5 keys and there are more keys within each key.'''


# In[2]:


'''I chose to work with the dataset as a data frame, as it is the easiest to read and interpret as well as doing analysis.
Data frames are most effectively visually organized and displays information in a very convenient manner. The CORGIS website
description of this dataset states that many majors were not available before 2010, so their values have been recorded as 0.
To fix this, I removed all rows which had any zeroes so that they do not affect averages.'''

import numpy as np
import pandas as pd
graduates = pd.read_csv('graduates.csv')
graduates = graduates[graduates['Demographics.Total'] != 0]
graduates


# In[3]:


print(graduates.isnull().sum())

'''Apart from the ones already removed, none of these columns have any missing values.'''


# In[4]:


'''I want to look at which major had the highest average salary. Since only the most recent data is relevant to me,
I filtered by year and only looked at the highest average salary in 2015. It looks like graduates in Operations Research
were earning the most in 2015, with their average salary being almost $117,085.'''

maxmeansalary = graduates.loc[graduates['Year'] == 2015, 'Salaries.Mean'].max()
maxmeansalary
max_index = graduates.loc[graduates['Year'] == 2015, 'Salaries.Mean'].idxmax()
maxrow = graduates.loc[max_index]
maxrow


# In[5]:


'''As an international student from Asia, I wanted to see which major had the highest proportion
of Asians in 2015. After running the program below, I found out that Botany had the highest proportion
of people with Asian ethnicities in 2015. There were 10,319 Asian Botany students in a total student body of 29,224 
included in this sample. So in 2015, a little more than 35% of the student population of Botany students identified
as Asian.'''

asians = 'Demographics.Ethnicity.Asians'
total = 'Demographics.Total'
year = 'Year'
year_2015 = 2015 

graduates_asians = graduates[graduates[year] == year_2015]
proportion = graduates_asians[asians] / graduates_asians[total]
graduates_asians['proportion'] = proportion
print(proportion.max())

maxprop = graduates_asians['proportion'].idxmax()
maxproprow = graduates_asians.loc[maxprop]
print(maxproprow)


# In[6]:


'''For my final analysis, I wanted to find out the conditional probability of a student working as a
teacher in 2015 given that his or her major was Economics. I decided to do this because I am an Economics major myself
and I would like to become a professor in the future, and I want to see how likely are Economics majors to take that
route. From the calculations below, we can conclude that there was a 17.4% chance of an Economics student working as a teacher/professor
in 2015.'''

major = 'Education.Major'
total = 'Demographics.Total'
year = 'Year'
teachers = 'Employment.Work Activity.Teaching'

econ = graduates[(graduates[major] == 'Economics') & (graduates[year] == 2015)]
econ_2015 = econ[total].sum()
econ_teachers = econ[teachers].sum()
conditional_probability = econ_teachers / econ_2015
print(conditional_probability)


# In[7]:


'''For the first figure, I will draw a histogram of mean salaries of each major in 2015. This will give us
a really good visual of which majors are earning the highest salaries and by what margins as per the most
recent data available.'''

import matplotlib.pyplot as plt

major = 'Education.Major'
salary = 'Salaries.Mean'
year = 'Year'
graduates_2015 = graduates[graduates[year] == 2015]
graduates_2015_sorted = graduates_2015.sort_values(by=salary, ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(graduates_2015_sorted[major], graduates_2015_sorted[salary], color='skyblue')
plt.xlabel('Major')
plt.ylabel('Mean Salary')
plt.title('Mean Salary by Major in 2015')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()


# In[8]:


'''For my second figure, I will draw a scatterplot showing how the mean salaries of
Economics majors have changed over the years. As seen below, Economics majors were earning
the highest in 1993, and their salaries have dropped significantly since then, although 
there has been an upward trend since 2008.'''

major = 'Education.Major'
salary = 'Salaries.Mean'
year = 'Year'

economics_df = graduates[graduates[major] == 'Economics']

plt.figure(figsize=(12, 6))
plt.scatter(economics_df[year], economics_df[salary], color='blue', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Mean Salary')
plt.title('Mean Salaries of Economics Majors Over the Years')
plt.grid(True)
plt.show()


# In[9]:


'''My last figure is going to be a bar plot showing the proportion of Asians in every major
in 2015. We can clearly see that Botany had the highest proportion of people identifying as Asian in 
2015, followed by Electrical Engineering and Statistics.'''

major = 'Education.Major'
demographics = 'Demographics.Total'
asian = 'Demographics.Ethnicity.Asians'
year = 'Year'
graduates_2015 = graduates[graduates[year] == 2015]
graduates_2015['Asian_Proportion'] = graduates_2015[asian] / graduates_2015[demographics]

plt.figure(figsize=(12, 6))
plt.bar(graduates_2015[major], graduates_2015['Asian_Proportion'], color='skyblue')
plt.xlabel('Major')
plt.ylabel('Proportion of Asians')
plt.title('Proportion of Asians in Every Major in 2015')
plt.xticks(rotation=90, ha='right') 
plt.show()


# In[10]:


'''For the final part, I used a linear regression model to predict the salary of a major input by the 
user using the salary information provided in the dataset for all majors across all years.'''

major_column = 'Education.Major'
salary_columns = ['Salaries.Mean', 'Salaries.Lowest', 'Salaries.Median', 'Salaries.Highest']

graduates['salary_info'] = graduates[salary_columns].astype(str).agg(' '.join, axis=1)

def lr(X, y):
    n = len(X)
    
    # Calculate the mean of X and y
    mean_X = sum(X) / n
    mean_y = sum(y) / n
    
    # Calculate the slope (m) and intercept (b) for the line y = mx + b
    numerator = sum((X[i] - mean_X) * (y[i] - mean_y) for i in range(n))
    denominator = sum((X[i] - mean_X)**2 for i in range(n))
    m = numerator / denominator if denominator != 0 else 0
    b = mean_y - m * mean_X
    
    return m, b

X_train = graduates['salary_info'].tolist()
y_train = graduates['Salaries.Mean'].tolist()

X_train_lengths = [len(item) for item in X_train]

slope, intercept = lr(X_train_lengths, y_train)
user_input_major = input("Enter a major: ")
user_input_salary_info = ' '.join(graduates[graduates[major_column] == user_input_major]['salary_info'])
user_input_length = len(user_input_salary_info)
predicted_salary = slope * user_input_length + intercept
print(f"Predicted Salary for {user_input_major}: ${predicted_salary:.2f}")


