from app import db


class Article(db.Model):
    # Utilizarea clasei: Definim o nouă clasă `Article` care moștenește din `db.Model`, o clasă de bază furnizată de SQLAlchemy.
    # Aceasta este o aplicare a principiului de moștenire.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    # Încapsularea: Proprietățile modelelor sunt definite ca atribute ale clasei,
    # controlând accesul la starea internă a obiectului (în acest caz, coloanele bazei de date).
    comments = db.relationship('Comment', back_populates='article', lazy='dynamic')
    # Relație: Utilizăm principiul de asociere pentru a crea o legătură între articole și autori.
    author = db.relationship('Author', back_populates='articles')


class Comment(db.Model):
    # O clasă care moștenește din `db.Model`, demonstrând reutilizarea codului prin moștenire.
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

    # Relație: Legătura între comentarii și articole.
    article = db.relationship('Article', back_populates='comments')


class Author(db.Model):
    # Clasa `Author` definește autori care pot avea mai multe articole.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Încapsularea și asocierea: Atributele clasei sunt private și relaționeaza cu alte entități.
    articles = db.relationship('Article', back_populates='author', lazy='dynamic')
    # `lazy='dynamic'` este o opțiune de încărcare care permite încărcarea articolelor unui autor la cerere.


