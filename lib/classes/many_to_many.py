class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) and not 5 <= len(title) <= 50:
            raise Exception("Invalid input")
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, title):
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise Exception("Invalid input")
        self._title = title

class Author:
    def __init__(self, name):
        if not isinstance(name, str) and not len(name) > 0:
            raise Exception("Invalid input")
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not len(name) > 0:
            raise Exception("Invalid input")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        article1 = Article(self ,magazine,title)
        self.articles().append(article1)
        return article1

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines())) if self.articles() else None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) and not 2 <= len(name) <= 16:
            raise Exception("Invalid input")
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise Exception("Invalid input")
        self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and category:
            self._category = category
        return None

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author
          for article in self.articles()))


    def article_titles(self):
        article_list = list(article.title for article in self.articles())
        return article_list if self.articles() else None

    def contributing_authors(self):
        publishing_authors = list(article.author for article in self.articles())
        authors_with_more_than_two_artcicles = list(set(author for author in publishing_authors if publishing_authors.count(author) > 2))
        return authors_with_more_than_two_artcicles if authors_with_more_than_two_artcicles else None