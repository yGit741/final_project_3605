import os
import pandas as pd
from prettytable import PrettyTable

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from wordcloud import WordCloud

import nltk
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def analysis_report(df):
    print("Insights from data:")

    # number of unique authors
    print("\nNumber of unique authors: ", df['author'].nunique())

    # top 5 most frequent authors
    top_authors = df['author'].value_counts().head(5)
    top_authors_table = PrettyTable(['Author', 'Count'])
    for index, value in top_authors.items():
        top_authors_table.add_row([index, value])

    print("\nTop 5 most frequent authors:\n")
    print(top_authors_table)

    # Number of tweets per language
    tweets_per_lang = df['language'].value_counts()
    tweets_per_lang_table = PrettyTable(['Language', 'Count'])
    for index, value in tweets_per_lang.items():
        tweets_per_lang_table.add_row([index, value])

    print("\nNumber of tweets per language:\n")
    print(tweets_per_lang_table)

    # Average number of likes and shares
    print("\nAverage number of likes: ", df['number_of_likes'].mean())
    print("Average number of shares: ", df['number_of_shares'].mean())

    # Correlation between number of likes and shares
    print("\nCorrelation between number of likes and shares: ", df['number_of_likes'].corr(df['number_of_shares']))


def time_plot(processed_data):
    # Extracting time series data for likes and shares
    processed_data['date_time'] = pd.to_datetime(processed_data['date_time'])

    # Aggregate data by month
    monthly_data = processed_data.resample('M', on='date_time').sum()

    # Extract time series data for likes and shares
    dates = monthly_data.index
    likes = monthly_data['number_of_likes']
    shares = monthly_data['number_of_shares']

    # Plotting time series for likes and shares
    plt.figure(figsize=(10, 5))
    plt.plot(dates, likes, label='Likes', color='blue')
    plt.plot(dates, shares, label='Shares', color='green')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Monthly Time Series of Likes and Shares')
    plt.legend()
    time_series = plt.show()


def tweets_words_cloud(processed_data):
    # read the csv data
    df = processed_data.sample(1000)

    # combine all content into a single string
    all_text = ' '.join(df['content'])

    # tokenize the text
    words = nltk.word_tokenize(all_text.lower())

    # filter out non-alphanumeric words
    words = [word for word in words if word.isalnum()]

    # filter out stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # combine filtered words into a single string
    filtered_text = ' '.join(filtered_words)

    # generate the word cloud
    wordcloud = WordCloud(stopwords=stop_words, max_font_size=50, max_words=100, background_color='white').generate(filtered_text)

    # display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    return plt


def regression_length_like(df):

    # calculate the length of each tweet
    df['tweet_length'] = df['content'].str.len()

    # selecting features and target variable
    X = df[['tweet_length']]  # feature: tweet length
    y = df['number_of_likes']  # target variable: number of likes

    # splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # creating and fitting the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # predicting on the testing set
    y_pred = model.predict(X_test)

    # plotting the regression line
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='actual data')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='regression line')
    plt.xlabel('tweet length')
    plt.ylabel('number of likes')
    plt.title('linear regression: tweet length vs. number of likes')
    plt.legend()
    plt.show()


def visualize_date(processed_data):
    # TODO complete this function

    time_series = time_plot(processed_data)

    words_cloud = tweets_words_cloud(processed_data)

    another_graph = regression_length_like(processed_data)

    return time_series, words_cloud, another_graph


def run():
    data = pd.read_csv(os.path.join("data", "tweets_df_processed.csv"))
    analysis_report(data)
    time_plot(data)
    tweets_words_cloud(data)
    regression_length_like(data)

if __name__ == "__main__":
    run()