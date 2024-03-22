import os
import pandas
import pandas as pd

def data_processor ():
    data_dir = os.path.join('.', 'data', 'tweets_df.csv')
    data = pd.read_csv(data_dir)

    # TODO complete this function

    # put your code here!
    # put your code here!
    # put your code here!
    # put your code here!
    # put your code here!
    processed_data = data

    # write the new processed data to ..\data directory
    processed_file_dir = os.path.join('.', 'data', 'tweets_df_processed.csv')

    if os.path.exists(processed_file_dir):
        os.remove(processed_file_dir)
    processed_data.to_csv(processed_file_dir, index=False)

    return processed_data

