import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Obtain data
    udemyDF = pd.read_csv("data/udemy1.csv")

    # print columns for reference
    print("Columns: " + str(list(udemyDF.columns)) + "\n")

    # 1.
    print("1. How many null values are there in each column?")
    print(udemyDF.isnull().sum().to_string() + "\n")

    # 2.
    print("2. Fill in the null values of price and rating to be 0")
    udemyDF['price'].fillna(0, inplace=True)
    udemyDF['rating'].fillna(0, inplace=True)
    print(udemyDF.isnull().sum().to_string() + "\n")

    # 3.
    print("3. Create a scatter of plot with the title of rating vs price and with red dots. What does this scatter "
          "plot tell us about these two variables?\n")
    # Convert price String to Float
    udemyDF['price'] = udemyDF['price'].str.replace('$', '')
    udemyDF['price'].fillna(0, inplace=True)
    udemyDF['price'] = udemyDF['price'].astype(float)
    # Create scatter plot rating vs price
    udemyDF.plot.scatter(x="rating", y="price", color='red')
    plt.title("rating vs price")
    plt.show()
    print("Answer: From rating 1 to 4 not much change in price (exception of a few outlier). Around 4 rating or "
          "higher you start to see an increase in price.\n")

    print("4. Create a graph showing the top 10 most popular categories by number of courses. What is the top "
          "category and the number of courses in it?")
    # Print top 10 popular categories
    print(udemyDF['category'].value_counts().nlargest(10))
    # Convert column category from type obj to string
    udemyDF['category'] = udemyDF['category'].convert_dtypes()
    top_10_categories = udemyDF['category'].value_counts().nlargest(10)

    # Create bar chart of top 10 Categories by number of courses.
    plt.bar(top_10_categories.index, top_10_categories.values)
    plt.xlabel('Category')
    plt.ylabel('Courses')
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               ['AWS Cert', 'Dev -> Web Dev', 'Amazon AWS', 'other -> Web Dev', 'other -> CSS', 'Web Dev -> HTML',
                'No-Code Dev -> Web Dev', 'Net&Sec -> AWS Cert', 'Web Dev -> HTML5', 'Web Dev -> WordPress'],
               rotation="horizontal", fontsize=5)
    plt.title('Top 10 Categories by number of courses')
    plt.show()
    print("Most Popular Category and number of courses in it: " + udemyDF['category'].value_counts().nlargest(1)
          .to_string() + " Courses\n")

    print("5. Add the following data into the dataframe ['EA > Assessment Training', 'Python Assessment Training', "
          "'Learn how to do the python EA assessment', 10.0, '0 students', 100, 'BAH', 'English', '11/2/2022',"
          "999.999, '1 hour', 'Student will learn how to use python and notebooks to answer various questions',"
          "'localhost:8888']")
    # Add data to dataframe
    # First fix all NaN's to have values
    udemyDF['category'].fillna("", inplace=True)
    udemyDF['title'].fillna("", inplace=True)
    udemyDF['short_decs'].fillna("", inplace=True)
    udemyDF['student_num'].fillna("", inplace=True)
    udemyDF['points'].fillna(0, inplace=True)
    udemyDF['creator'].fillna("", inplace=True)
    udemyDF['language'].fillna("", inplace=True)
    udemyDF['last_update'].fillna("", inplace=True)
    udemyDF['duration'].fillna("", inplace=True)
    udemyDF['long_desc'].fillna("", inplace=True)
    udemyDF['url'].fillna("", inplace=True)
    # create new row you want to add
    new_row = {'EA > Assessment Training', 'Python Assessment Training', 'Learn how to do the python EA assessment',
               10.0, '0 students', 100, 'BAH', 'English', '11/2/2022', 999.999, '1 hour',
               'Student will learn how to use python and notebooks to answer various questions',
               'localhost:8888'}
    # convert to list so you can add it to DF
    new_row = list(new_row)
    # convert all columns to appropriate data types
    udemyDF['title'] = udemyDF['title'].astype(str)
    udemyDF['short_decs'] = udemyDF['short_decs'].astype(str)
    udemyDF['student_num'] = udemyDF['student_num'].astype(str)
    udemyDF['points'] = udemyDF['points'].convert_dtypes()
    udemyDF['creator'] = udemyDF['creator'].astype(str)
    udemyDF['language'] = udemyDF['language'].astype(str)
    udemyDF['last_update'] = udemyDF['last_update'].astype(str)
    udemyDF['price'] = udemyDF['price'].convert_dtypes()
    udemyDF['duration'] = udemyDF['duration'].astype(str)
    udemyDF['long_desc'] = udemyDF['long_desc'].astype(str)
    udemyDF['url'] = udemyDF['url'].convert_dtypes()
    # Add row to data frame
    udemyDF = udemyDF.append(new_row, ignore_index=True)
    print("New row of data added\n")

    print("6. Create a new dataframe that shows the average and count for each category’s rating and price. Which "
          "category has the top mean rating and top mean price and how many courses were offered?")
    newDF = udemyDF.groupby(['category']).mean()
    print(newDF)


if __name__ == "__main__":
    main()
