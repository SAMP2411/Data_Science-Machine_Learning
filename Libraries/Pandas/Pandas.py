import numpy as np
import pandas as pd


def change():
    print("-" * 50)


change()

# Creating a series with list or array
lst1 = [1, 2, 3, 4, 5]
lst2 = np.array([1, 2, 3, 4, 5])
print(pd.Series(lst1))
print(pd.Series(lst2))

# How to provide your own index
print(pd.Series(data=["a", "b", "c"], index=[1, 2, 3]))

# Series through dictionary
steps = {"1": 1000, "2": 2000, "3": 2100}
print(pd.Series(steps))

# Using repeat function with proper index using reset_index(drop=True) otherwise same index would be printed for each element
print(pd.Series(5).repeat(5).reset_index(drop=True))

s = pd.Series([10, 20]).repeat([5, 2]).reset_index(drop=True)
print(s)
# Prints element with index as 6
print(s[6])
# Prints whole Series
print(s[:])

change()

# Aggregate Functions
sr = pd.Series([1, 2, 3, 4, 5, 6, 7])
print(sr.agg([min, max, sum]))

# Abs function converts -ve to +ve
sr = pd.Series([1, 2, -3, 4, -5, -6, 7])
print(sr.abs())

change()
# Appending Series
sr1 = pd.Series([1, 2, 3, 4, 5, 6, 7])
sr2 = pd.Series([1, 2, -3, 4, -5, -6, 7])
print(sr1._append(sr2))

# Convert datatype of the elements
print(sr1.astype("float"))

# Returns true for only elements in the given range
print(sr1.between(5, 7))


# Operations on string as Series elements
ser = pd.Series(["ah be   ", "    jfeej k", "sdfes g", "sdfs@ df"])

print(ser.str.upper())
print(ser.str.lower())

for i in ser:
    print(i, len(i))

ser = ser.str.strip()
for i in ser:
    print(i, len(i))

ser = ser.str.split()
print(ser)

# Checks if any element contains the character and if yes return true for that index
print(ser.str.contains("@"))

print(ser.str.replace("@", "new_str"))

print(ser.str.count("a"))

print(ser.str.endswith("f"))
print(ser.str.startswith("a"))
print(ser.str.find("eej"))

# Converting Series into list
print(ser.to_list())

change()
change()
change()

# Detailed Coding implementaion on Pandas DataFrame
data = {
    "Name": ["Jai", "Princi", "Gaurav", "Anuj"],
    "Age": [27, 24, 22, 32],
    "Address": ["Delhi", "Kanpur", "Allahabad", "Kannauj"],
    "Qualification": ["Msc", "MA", "MCA", "Phd"],
}

df = pd.DataFrame(data)
print(df)
print(df[["Name", "Qualification"]])
