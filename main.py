import pandas as pd


# Reading Dataset

dataset = pd.read_csv('scores 2.csv')

# Data Exploration

print(dataset.describe)



# List of items

features = dataset.columns.tolist()
print("Available features:")
print(dataset.dtypes)

sample_dataset = dataset.head(5)
print(sample_dataset)

# Data Cleaning

school_Data = pd.DataFrame(dataset)
school_Data.fillna('null')

school_Data.dropna(inplace=True)
print(school_Data)


# Calculate Avarage

def calculate_avarage(school_Data):
    column = input('Enter column:')
    avg = school_Data[column].mean()


def calculate_min_max(school_Data):
    column = input('Enter column:')
    min = school_Data[column].min()
    column = input('Enter column:')
    max = school_Data[column].max()

    return min, max


print(f" Mode: {calculate_avarage(school_Data)}")
print(f" Mean:{calculate_min_max(school_Data)}")

