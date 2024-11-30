# Stock-Movement-Prediction-Based-on-Social-Media-Sentiment

This project predicts stock price movements using sentiment analysis of social media discussions (e.g., Twitter). The pipeline includes:
- Data scraping using `tweepy`.
- Text cleaning and sentiment analysis using `NLTK`.
- Predictive modeling with `scikit-learn`.

---

## Setup Instructions

### 1. Clone the Repository
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/stock-movement-prediction.git
cd stock-movement-prediction
```
### 2. Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
### 3. Add API Keys
Set up your Twitter API credentials:

Create a .env file in the root directory. Add your API keys in the following format:
```makefile
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```
### 4. Run the Scripts
Use the following commands to execute the pipeline:
To scrape tweets:
```bash
python app.py
```
