import pandas as pd
import os
# Create an empty list to store the DataFrames
df_list = []

#Loop through the files and change their names
# for alpha in ['a','c', 'd', 'e', 'f', 'g', 'h', 'l', 'p', 'r']:
#     for i in range(1, 501):
#         old_file_name = alpha + str(i)
#         new_file_name = alpha + str(i) + '.txt'
#         os.rename(old_file_name, new_file_name)



# Loop through the files and read them in 
for alpha in ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'l', 'p', 'r']:
    for i in range(1, 501):
        file_name = 'test//'+alpha + str(i) + '.txt'
        df = pd.read_fwf(file_name , sep="  ", header=None)
        

        first_value = df.iloc[0,0]

        # Get last value of the file
        last_value = df.iloc[-1,-1]
        
        # Drop first 3 columns and last column
        df = df.drop(df.columns[:3], axis=1)
        
        df = df.drop(df.columns[-1], axis=1)
        
        #if has less than 8 rows, add rows of 0
        if df.shape[0] < 8:
            for i in range(8-df.shape[0]):
                df.loc[df.shape[0]] = 0
                
        # Concatenate all rows into one single row
        big_row = df.values.flatten().tolist()

        # Insert first value and last value at the beginning and end of the big row
        big_row.insert(0, first_value)
        big_row.insert(len(big_row), last_value)
        df_list.append(big_row)
        # print(df_list)
    

# Create a DataFrame from the list of lists
df_final = pd.DataFrame(df_list)
# Write the final DataFrame to a CSV file
df_final.to_csv('test.csv', index=False)

