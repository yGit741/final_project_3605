import os
import pandas as pd

def data_processor():
    # print(os.getcwd())
    # print(os.listdir('.'))
    data_dir = os.path.join('data', 'tweets_df.csv')

    # print(data_dir)
    data = pd.read_csv(data_dir)
    # print(342342342343)


    # fill missing values in numeric columns with mean
    data.fillna(data.mean(), inplace=True)

    # removing duplicates
    data.drop_duplicates(inplace=True)

    # convert text data to lowercase
    data['content'] = data['content'].str.lower()

    # check if any column contains NaN values
    if data.isnull().values.any():
        print("Warning: NaN values detected!")

    # check if likes are non-negative
    if (data['number_of_likes'] < 0).any():
        print("Error: Negative likes found!")

    # write the new processed data to ..\data directory
    processed_file_dir = os.path.join('..', 'data', 'tweets_df_processed.csv')

    if os.path.exists(processed_file_dir):
        os.remove(processed_file_dir)

    data.to_csv(data_dir, index=False)

    return data

if __name__ == "__main__":
    data_processor()