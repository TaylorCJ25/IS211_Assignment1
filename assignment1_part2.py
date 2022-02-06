class Book:
    author =""
    title =""
    def __init__(self, titieName, authorName):
        self.title = titieName
        self.author = authorName
    def display(self):
        print(f"\'{self.title}\', written by {self.author}")
Book1 =Book("Of Mice and Men", "John Steinbeck")
Book2 =Book("To kill a Mockingbird", "Harper Lee")

Book1.display()
Book2.display()