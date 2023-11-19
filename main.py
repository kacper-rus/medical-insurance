import pandas as pd
import matplotlib.pyplot as plt


file_path = 'insurance.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

print(df.head())

avg_age = df['age'].mean()
region_counts = df['region'].value_counts()
print("Where are they from?")
print(region_counts)


# Group the data by the 'smoker' column
grouped_data = df.groupby('smoker')['charges']

# Calculate the mean and median for each group
mean_costs = grouped_data.mean()
median_costs = grouped_data.median()

# Display the results
print("Mean costs:")
print(mean_costs)

print("\nMedian costs:")
print(median_costs)

# Filter the DataFrame to include only individuals with at least one child
df_with_children = df[df['children'] > 0]

# Calculate the average age for individuals with at least one child
average_age_with_children = df_with_children['age'].mean()

print(f'The average age for someone with at least one child is: {average_age_with_children:.2f}')

# plt.plot(df['age'], df['bmi'])
# plt.title('Your Plot Title')
# plt.xlabel('age')
# plt.ylabel('bmi')
# plt.show()




