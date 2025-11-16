class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return all Article instances written by this author"""
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        """Return unique magazines this author has written for"""
        mags = [a.magazine for a in self.articles()]
        return list(dict.fromkeys(mags))

    def add_article(self, magazine, title):
        """Creates a new article for this author"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return unique topic areas for all magazines the author has written for"""
        areas = [m.category for m in self.magazines()]
        return list(dict.fromkeys(areas)) if areas else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """Name must be string length 2–16; invalid assignment ignored"""
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        """Category must be string length >0; invalid assignment ignored"""
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        """Return all articles written for this magazine"""
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        """Return unique authors who have written for this magazine, or None"""
        authors = {a.author for a in self.articles()}
        return list(authors) if authors else None

    def article_titles(self):
        """Return list of titles of articles written for this magazine, or None"""
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """Return authors with more than 2 articles in this magazine, or None"""
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        result = [author for author, c in counts.items() if c > 2]
        return result if result else None
