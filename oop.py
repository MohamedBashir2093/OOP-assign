

# Assignment 1:


class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")

# Derived Class - EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, year_published, file_size):
        super().__init__(title, author, year_published)
        self.file_size = file_size

    def download(self):
        print(f"Downloading the eBook '{self.title}' with file size {self.file_size}MB.")

    def read(self):
        print(f"Reading '{self.title}' on your e-reader...")

# Create an instance of EBook
my_ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 5)

# Accessing attributes
print(f"Title: {my_ebook.title}")
print(f"Author: {my_ebook.author}")
print(f"Year Published: {my_ebook.year_published}")
print(f"File Size: {my_ebook.file_size}MB")

# Calling methods
my_ebook.read()  # Overridden method from EBook class
my_ebook.download()




# Activity 2: 

# Base Class - Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived Class - Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Derived Class - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Derived Class - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Create objects of different vehicles
car = Car()
plane = Plane()
boat = Boat()

# Call the move() method on each object
car.move()    # "Driving"
plane.move()  # "Flying"
boat.move()   # "Sailing"
