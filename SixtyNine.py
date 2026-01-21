class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book has {self.pages} pages"

b = Book(120)
print(b)
