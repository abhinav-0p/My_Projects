# 📊 Instagram Analytics — Exploratory Data Analysis (EDA)

A beginner-friendly Exploratory Data Analysis (EDA) project using Python to explore Instagram post performance, engagement, reach, and content categories.

The project uses an Instagram analytics dataset containing approximately 30,000 records. The goal is to understand the data, explore patterns, and visualize relationships between different Instagram performance metrics.

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📂 Project Structure

```text
Instagram-Analytics/
│
├── Instagram_EDA.ipynb
├── Instagram_Analytics.csv
└── README.md
```

## 🔍 Project Workflow

### 1. Data Inspection
- Loaded the dataset using Pandas.
- Checked the first and last rows.
- Examined dataset dimensions and column names.
- Inspected data types and statistical summaries.

### 2. Data Cleaning and Preparation
- Removed unnecessary columns such as `post_id` and `account_id`.
- Checked for missing values and filled missing numerical values using column means.
- Checked for duplicate records.
- Converted date-related columns to datetime format.
- Grouped columns by data type for further exploration.

### 3. Exploratory Data Analysis
- Examined categorical value counts.
- Checked unique values in each column.
- Explored correlations between numerical variables.
- Checked numerical columns for potential outliers.

### 4. Data Visualization

- 📈 Distribution of Instagram likes
- 📊 Number of posts by media type
- ❤️ Average likes by media type
- 📉 Average engagement rate by content category
- 🚦 Number of posts by traffic source
- 🔗 Relationship between reach and impressions
- 🕒 Average engagement rate by posting hour
- 📦 Distribution of reach by media type
- 🔥 Correlation heatmap of numerical variables
- 📊 Box plots for outlier exploration

## 📌 Key Objectives

- Understand the structure and quality of Instagram analytics data.
- Explore engagement metrics such as likes, comments, shares, saves, and engagement rate.
- Compare performance across different media types and content categories.
- Explore the relationship between reach and impressions.
- Examine how engagement varies by posting hour.
- Practice creating meaningful visualizations using Python.

## 📚 What I Learned

Through this project, I practiced:

- Data inspection using Pandas
- Handling missing numerical values
- Working with datetime columns
- Exploring categorical and numerical variables
- Correlation analysis
- Outlier detection using box plots
- Creating visualizations with Matplotlib and Seaborn
- Performing EDA step by step in a Jupyter Notebook

## 👨‍💻 About the Project

This project is part of my learning journey in Python and Data Science. It helped me gain practical experience in exploring datasets, identifying patterns, and visualizing data.

More projects coming soon! 🚀

⭐ Feel free to explore the repository.