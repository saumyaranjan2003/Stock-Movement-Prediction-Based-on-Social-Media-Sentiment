import re
import pandas as pd
import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import os  # For environment variables

# Download NLTK resources
nltk.download('vader_lexicon')

# Load Twitter API keys from environment variables
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

if not TWITTER_BEARER_TOKEN:
    raise ValueError("Twitter API keys not found. Set them in environment variables.")

# Initialize Tweepy client for API v2
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

# Function to scrape tweets
def scrape_tweets_v2(query, max_results=100):
    tweets = []
    response = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=max_results)
    if response.data:
        for tweet in response.data:
            tweets.append({'text': tweet.text, 'created_at': tweet.created_at})
    return pd.DataFrame(tweets)

# Function to clean tweet text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'RT\s+', '', text)  # Remove RT prefix
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text

# Function to analyze sentiment
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)['compound']

# Main pipeline
def main():
    # Step 1: Scrape tweets (Example: Tesla)
    print("Scraping tweets...")
    query_term = input("Enter a search term (e.g., company name): ")
    tweets_df = scrape_tweets_v2(query_term, max_results=100)

    if tweets_df.empty:
        print("No tweets found. Exiting.")
        return

    # Step 2: Clean tweets
    print("Cleaning tweets...")
    tweets_df['cleaned_text'] = tweets_df['text'].apply(clean_text)

    # Step 3: Perform sentiment analysis
    print("Analyzing sentiment...")
    tweets_df['sentiment_score'] = tweets_df['cleaned_text'].apply(analyze_sentiment)

    # Step 4: Visualize sentiment distribution
    print("Visualizing sentiment distribution...")
    sns.histplot(tweets_df['sentiment_score'], kde=True, bins=20)
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

    # Print sample results
    print("Sample tweets with sentiment scores:")
    print(tweets_df[['cleaned_text', 'sentiment_score']].head())

# Run the main function
if __name__ == "__main__":
    main()
