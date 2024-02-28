from app import db
from app.models import Article, Author, Comment

try:
    db.create_all()

    # Creaza un autor
    author = Author(name="John Doe")
    db.session.add(author)
    db.session.commit()  # Pt.obtinere ID autor

    # Creaza un articol
    article = Article(title="Exemplu de Articol", content="Acesta este conținutul articolului.", author_id=author.id)
    db.session.add(article)
    db.session.commit()  # obtinere ID articol

    # Creaza un comentariu
    comment = Comment(content="Acesta este un comentariu.", article_id=article.id)
    db.session.add(comment)
    db.session.commit()

    print("Migration script executed successfully.")
except Exception as e:
    print("An error occurred during migration:", str(e))
    db.session.rollback()  # Rollback se schimba daca apare o eroare
finally:
    db.session.close()  # Inchide sesiunea



