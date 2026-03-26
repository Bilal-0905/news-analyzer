
import matplotlib.pyplot as plt
import requests
from textblob import TextBlob
API_KEY = "Your key here"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
response=requests.get(url)
data=response.json()
positive=0
negative=0
neutral=0
for article in data["articles"]:
    title = article["title"]
    analysis = TextBlob(title)
    if analysis.sentiment.polarity > 0:
        sentiment="Positive"
        positive+=1
    elif analysis.sentiment.polarity < 0:
        sentiment="Negative"
        negative+=1
    else:
        sentiment="Neutral"
        neutral+=1
    print(f"{sentiment} -- {title}")
print(f"\nResults:")
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Neutral: {neutral}")
  
labels=["Positive","Negative","Neutral"]
counts=[positive,negative,neutral]
colors=["green","red","grey"]
plt.bar(labels,counts,color=colors)
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Headlines")
plt.tight_layout()
plt.savefig("sentiment_chart.png")
print("Chart saves!")
colors=["green","red","grey"]
plt.bar(labels,counts,color=colors)
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Headlines")
plt.tight_layout()
plt.savefig("sentiment_chart.png")
print("Chart saves!")

