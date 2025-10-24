📊 CORGIS Stock Price Analysis

Author: Naufal Alavi

🧩 Overview

This project explores the CORGIS “Graduates” dataset, which provides information about employment, salaries, and demographics of students across different majors.
The analysis aims to uncover patterns in average salaries, ethnic composition, and employment outcomes, while providing data visualizations and simple predictive modeling.

🎯 Objectives

Clean and preprocess the dataset for analysis.

Identify the highest-paying majors in 2015.

Examine demographic composition, focusing on Asian representation across majors.

Calculate conditional probabilities for employment outcomes (e.g., likelihood of teaching positions among Economics majors).

Visualize relationships through histograms, scatterplots, and bar plots.

Implement a basic linear regression model to estimate mean salary based on dataset patterns.

🧠 Methodology

Data Loading & Cleaning

Imported CSV data into a Pandas DataFrame.

Removed rows with zeros or missing demographic totals to prevent bias.

Verified data completeness with isnull() checks.

Exploratory Analysis

Used filtering and aggregation to determine salary leaders and demographic proportions.

Analyzed 2015 data to focus on recent, relevant insights.

Statistical Computations

Calculated maximum mean salaries and highest ethnic proportions.

Estimated conditional probabilities for employment activities.

Visualization

Histogram: Mean salaries by major (2015).

Scatterplot: Salary trends for Economics majors (1990–2015).

Bar Plot: Asian representation by major (2015).

Modeling

Built a custom linear regression function to predict salaries based on major-specific text data length.

Allowed user input for salary prediction.

📈 Key Findings

Operations Research graduates earned the highest average salary in 2015 (~$117,085).

Botany had the highest Asian representation (~35% of students).

Economics majors had a 17.4% likelihood of working in teaching roles.

Salary trends for Economics showed recovery post-2008 recession.

🧰 Technologies Used

Language: Python 3

Libraries:

pandas – Data manipulation

numpy – Numerical processing

matplotlib – Visualization

graduates (CORGIS library) – Dataset source

🧪 How to Run

Install dependencies:

pip install pandas numpy matplotlib corgis


Place graduates.csv in the same directory as CORGIS Project.py.

Run the script:

python "CORGIS Project.py"


When prompted, enter a major (e.g., “Economics”) to get a predicted salary.

📊 Sample Outputs

Highest Mean Salary (2015): Operations Research – $117,085

Highest Asian Proportion: Botany – 35.3%

Economics Majors in Teaching (2015): 17.4%

Predicted Salary (Economics): $92,000 (approx., based on model)

📜 References

CORGIS Dataset Project: https://think.cs.vt.edu/corgis

MUSIC Model of Academic Motivation (Referenced in the CORGIS paper summary)
