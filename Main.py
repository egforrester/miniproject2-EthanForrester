# INF601 - Advanced Programming in Python
# Ethan Forrester
# Mini Project 2




import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

try:
    Path("charts").mkdir()
except FileExistsError:
    pass

#What is the number of restaurants per country
resturants = pd.read_csv( "North America Restaurants.csv", index_col=0)

Countries = resturants["country"].describe()

df = pd.DataFrame({'Countries':['US', 'CA'], 'Number of Restaurants':[829, 1500-829]})
ax = df.plot.bar(x='Countries', y='Number of Restaurants', rot=0)
plt.title("Number of Restaurants per Country")
plt.ylabel("Number of Restaurants")
plt.show()

ChartR = "charts/question1.png"
plt.savefig(ChartR)
plt.show()

#What is the number of restaurants per state
usrestaurants = pd.read_csv( "Top US Restaurants.csv" , index_col=0)

States = usrestaurants["state"].value_counts()

df = pd.DataFrame({'States':['FL', 'CA', 'WI', 'TX', 'NY', 'GA', 'PA', 'NJ', 'TN', 'SC', ], 'Number of Restaurants':[143, 68, 62, 51, 39, 38, 32, 32, 28, 24,]})
ax = df.plot.bar(x='States', y='Number of Restaurants', rot=0)
plt.title("Top 10 most Restaurants per State")
plt.ylabel("Number of Restaurants")
plt.figure(figsize=(8,8))
plt.show()

ChartS = "charts/" ".png"
plt.savefig(ChartS)
plt.show()













filename = "charts/question1.png"
plt.savefig(filename)

#


