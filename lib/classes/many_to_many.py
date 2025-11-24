

class Article:
    all = []

    def __init__(self, author, magazine, title):
        # check basic title rules
        if type(title) != str:
            raise Exception("Title must be string")
        if len(title) < 5 or len(title) > 50:
            raise Exception("Title length bad")

        self.title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)


class Author:
    all = []

    def __init__(self, name):
        if type(name) != str or name == "":
            raise Exception("Bad name")

        self.name = name
        Author.all.append(self)

    def articles(self):
        # collect articles written by this author
        arr = []
        for a in Article.all:
            if a.author == self:
                arr.append(a)
        return arr

    def magazines(self):
        # unique magazines the author wrote for
        mags = []
        for a in self.articles():
            if a.magazine not in mags:
                mags.append(a.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        # get categories from magazines
        areas = []
        for m in self.magazines():
            if m.category not in areas:
                areas.append(m.category)

        if len(areas) == 0:
            return None
        return areas


class Magazine:
    all = []

    def __init__(self, name, category):
        # internal values
        self._name = None
        self._category = None

        # use setters to validate
        self.name = name
        self.category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # only set if valid
        if type(value) == str and len(value) >= 2 and len(value) <= 16:
            self._name = value
        # if not valid, ignore and keep old value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) == str and len(value) > 0:
            self._category = value
        # ignore invalid values

    def articles(self):
        arr = []
        for a in Article.all:
            if a.magazine == self:
                arr.append(a)
        return arr

    def contributors(self):
        # authors who wrote at least one article
        authors = []
        for a in self.articles():
            if a.author not in authors:
                authors.append(a.author)
        if len(authors) == 0:
            return None
        return authors

    def article_titles(self):
        # titles of all articles
        titles = []
        for a in self.articles():
            titles.append(a.title)
        if len(titles) == 0:
            return None
        return titles

    def contributing_authors(self):
        # authors with more than 2 articles
        count = {}
        for a in self.articles():
            auth = a.author
            if auth not in count:
                count[auth] = 1
            else:
                count[auth] += 1

        result = []
        for author in count:
            if count[author] > 2:
                result.append(author)

        if len(result) == 0:
            return None
        return result
