# Data_Science-Machine_Learning
Welcome to my Data Science and Machine Learning repository! This collection showcases a variety of projects I have worked on, demonstrating my skills in web scraping, data analysis, machine learning, and data handling. Each folder contains one or more projects with detailed code and, in some cases, resulting datasets and visualizations.

Table of Contents
ML Practice

Web Scraping

Data Analysis

Data Toolkit

Libraries

Technologies Used

How to Use

ML Practice
This directory contains a series of Jupyter notebooks that implement fundamental machine learning algorithms and concepts. It's a practical toolkit for understanding how different models work.

Regression Models:

1. Linear Regression.ipynb: Implements a simple linear regression model.

2. Multiple Linear Regression.ipynb: Demonstrates linear regression with multiple independent variables.

3. Linear Regression using OLS method.ipynb: An implementation of linear regression using the Ordinary Least Squares (OLS) method.

4. Polynomial Linear Regression.ipynb: Implements polynomial regression for non-linear relationships.

5. Support Vector Machine (SVR).ipynb: A notebook on Support Vector Regression for prediction tasks.

Ensemble Methods:

6. Decision Tree.ipynb: Implements a Decision Tree Regressor.

7. Random Forest.ipynb: Implements a Random Forest Regressor, an ensemble of decision trees.

Model Evaluation & Dimensionality Reduction:

K-Fold Cross Validation.ipynb: Demonstrates the K-Fold cross-validation technique to evaluate model performance robustly.

PCA.ipynb: Implements Principal Component Analysis (PCA) for dimensionality reduction.

t-SNE.ipynb: Implements t-Distributed Stochastic Neighbor Embedding (t-SNE) for visualizing high-dimensional datasets.

Web Scraping
This section contains various projects focused on extracting data from the web using Python libraries like BeautifulSoup and Selenium.

Book Scrapper
A multi-stage project to scrape book information from the website books.toscrape.com.

start.ipynb: The first script that scrapes basic book information from the main pages.

Read Book Data.ipynb: This script visits each book's individual page to scrape more detailed information like UPC, tax, and the number of reviews.

Combine CSV files.ipynb: A final script to merge the data from the previous steps into one comprehensive CSV file, All info Books.csv.

Quotes Scrapper
This project scrapes quotes, author details, and biographical information from quotes.toscrape.com.

intro.ipynb: A simple introduction to fetching a webpage's HTML content.

Scraping Quotes.ipynb & Scraping Quotes with Author Details.ipynb: Notebooks that demonstrate scraping quotes and associated author details.

Scraping Multiple Pages.ipynb: Handles pagination to scrape data from all pages on the site, resulting in Quotes.csv.

Scraping Authors.ipynb: Visits each author's page to collect biographical information and saves it.

Stock Image Scrapper
This project tackles scraping from a website with infinite scrolling (stockmages.netlify.app) using Selenium.

start.ipynb: Uses Selenium to automate browser scrolling to load all images, then scrapes image URLs, tags, likes, and comments, saving them to images.csv.

saving the dataset.ipynb: Processes the scraped data to add unique IDs and local file paths, and includes functionality to download the images, resulting in imgs_all_data.csv.

YouTube Scrapper
A project to scrape video data from the GeeksforGeeks YouTube channel.

The notebooks cover scraping video titles, view counts, upload dates, and links from the main channel page (Video Dataset Generate.ipynb) and detailed information like descriptions and likes from individual video pages (Video Data Scraper.ipynb).

The scraped data is stored in GFG.csv and Video_Info.csv.

Wikipedia Scrapper
A simple yet powerful scraper that can fetch content from any Wikipedia page by title.

Google Search Link Generator.ipynb: Generates a Google search query to find the correct Wikipedia page link for a given topic.

Wikipedia Scraping by Title.ipynb: Takes a topic, finds the corresponding Wikipedia page, and scrapes all the text content, saving it to a .txt file named after the topic.

Note: This folder contains additional web scraping projects. Feel free to explore them!

Data Analysis
This folder contains projects focused on exploratory data analysis (EDA) and visualization.

GDP Analysis
A project to analyze and visualize the GDP of various countries over the years.

gdp.csv: The dataset containing GDP information for different countries from 1960 onwards.

analysis.ipynb: The Jupyter Notebook where the data is processed, analyzed, and visualized using Plotly.

.html Files: Interactive plots generated from the analysis, such as World GDP.html and Countries GDP.html, which allow for a dynamic exploration of the data.

Data Toolkit
This folder contains practical data handling tools and mini-projects.

Inventory Management System
A simple command-line based inventory management system with two different back-end storage methods.

Inventory Mgmt. System using .JSON file.py: Manages inventory by reading from and writing to a Record.json file. Sales are recorded in Sales-json.txt.

Inventory Mgmt. System using .txt file.py: An alternative version that uses a simple Inventory.txt file for data storage, with sales logged in sales-text.txt.

analysis.ipynb: A notebook for analyzing the sales data generated by the system.

Libraries
This directory is dedicated to notebooks that explore and demonstrate the usage of popular Python libraries for data science. It serves as a practical reference for various functions and features.

Pandas: Notebooks demonstrating data manipulation, cleaning, and analysis techniques.

Matplotlib: Examples of creating various static, animated, and interactive visualizations.

Technologies Used
Language: Python

Data Manipulation: Pandas, NumPy

Data Visualization: Matplotlib, Seaborn, Plotly

Machine Learning: Scikit-learn

Web Scraping: BeautifulSoup, Selenium, Requests

How to Use
Clone the repository:

Bash

git clone https://github.com/SAMP2411/Data_Science-Machine_Learning.git
Navigate to a project folder:

Bash

cd Data_Science-Machine_Learning/ml_practice
Install dependencies: It is recommended to create a virtual environment. You can install the required libraries using pip:

Bash

pip install pandas numpy matplotlib seaborn scikit-learn plotly beautifulsoup4 selenium
Run the Jupyter Notebooks:

Bash

jupyter notebook
