#CSFun_CW  -  00016144  00016136

import pandas as pd
import matplotlib.pyplot as plt

# Reading Dataset

dataset = pd.read_csv('scores 2.csv')

# Data Exploration

print(dataset.describe)

# List of items
def show_data(dataset):
    num_rows, num_columns = dataset.shape
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")

    features = dataset.columns.tolist()
    print("Available features:")
    print(dataset.dtypes)

#Just for checking
print(show_data(dataset))

def sample_data(dataset):
    sample_dataset = dataset.head(5)
    print(sample_dataset)



# Data Cleaning
def cleaning_dataset(dataset):
    school_Data = pd.DataFrame(dataset)
    school_Data.fillna('null')

    school_Data.dropna(inplace=True)
    return school_Data



# Calculate Average:

#Request from User - working with Data
def work_with_data(dataset):
    while True:
        user_input = input("""
        Choose what you want to do with the data:
        1 - Show brief information about the dataset
        2 - Show sample of dataset
        3 - exit this operation
        """)
        match(user_input):
            case'1':
                show_data(dataset)
            case '2':
                sample_data(dataset)
            case '3':
                break
            case _:
                print("Invalid operation! Write the number between 1 and 3")


# Calculate average and calculate min max is working properly

#Calculating Average
def calculate_avg(school_Data):
    avg_column = input('Enter column:')
    avg = school_Data[avg_column].mean()
    print(f"Average of {avg_column}: {avg}")

#Calculating Min and Max
def calculate_min_max(school_Data):
    min_column = input('Enter column:')
    min = school_Data[min_column].min()
    max_column = input('Enter column:')
    max = school_Data[max_column].max()

    print(f"The minimum value of {min_column} is: {min}")
    print(f"The maximum value of {max_column} is: {max}")



# Value counts
def count_occurrences_by_column(dataset):
    column_name = input("Which column do you want to check: ")
    if column_name not in dataset.columns:
        print(f"Column '{column_name}' - is not in this Dataset")
        return

    occurrences = dataset[column_name].value_counts()
    print()
    print(f"Counting values in a '{column_name}':")
    print(occurrences)


#Diagrams:

#Histogram
def plot_hist(dataset):
    column_hist = input('Enter column for making Histogram:')
    try:
        plt.hist(dataset[column_hist], bins=20, color='red', edgecolor='black')
        plt.title('Histogram')
        plt.xlabel(column_hist)
        plt.ylabel('Frequency')
        plt.show()
    except KeyError:
        print(f"This '{column_hist}' is not available in the Dataset!")

print(plot_hist(dataset))
#Line Graph
def perform_line_graph_analysis(dataset):
    column_line = input("Enter the Column name to make Line Graph: ")

    try:
        # Counting values of the columns
        value_counts = dataset[column_line].value_counts()

        # Line graph
        value_counts.sort_index().plot(kind='line', marker='o', color='orange')
        plt.title(f'Line Graph for {column_line}')
        plt.xlabel(column_line)
        plt.ylabel('Frequency')
        plt.show()

    except KeyError:
        print(f"This '{column_line}' is not available in the Dataset!")

print(perform_line_graph_analysis(dataset))





#just checking for pull/push/merge