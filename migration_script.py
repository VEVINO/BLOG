# from app import db
from app.models import Article

try:
    # Interogare pentru a obține toate articolele
    articles = Article.query.all()

    # Iterează prin articole și afișează ID-urile lor
    for article in articles:
        print(f"Article ID: {article.id}")

except Exception as e:
    print("An error occurred:", str(e))
