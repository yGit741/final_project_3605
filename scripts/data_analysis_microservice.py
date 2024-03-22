import pandas as pd
import os

def analysis_report(processed_data):
    #TODO complete this function - just print and dont return anything
    print("Insights from data:")


def visualize_date(processed_data):
    # TODO complete this function

    time_series = 1

    words_cloud = 2

    another_graph = 3

    return time_series, words_cloud, another_graph

def run():
    data_dir = os.path.join('.','data', 'tweets_df_processed.csv')

    data = pd.read_csv(data_dir)

    analysis_report(data)

    a, b, c = visualize_date(data)
    print(a)
    print(b)
    print(c)
