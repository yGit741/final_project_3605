import tweepy
import os
import configparser
import pandas as pd
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scripts import authentication
