# The SOLID Principles


### 1. Single Responsiblity Principle (SRP)

Each class must have a single responsibility.

### 2. Open/Closed Principle (OCP)

Code should be open for extension but closed for modification.

### 3. Liskov Substitution Principle (LSP)

Subtypes must be substitutable for their base types without altering the correctness of the program.

### 4. Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use.

### 5. Dependency Inversion Principle (DIP)

Abstractions should not depend on details. Details should depend on abstractions.



### 1. Single Responsibility Principle (SRP)

**Before Adhering (Single `FileManager` Class):**

```python
from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

This code presents a single `FileManager` class that manages file operations and ZIP archiving. However, it violates the
SRP because it has multiple responsibilities. It reads/writes files and handles ZIP compression/decompression, which
should be separate concerns.

**After Adhering (Separated Classes `FileManager` and `ZipFileManager`):**

```python
from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

In this improved code, the responsibilities are separated into two classes. `FileManager` is responsible for reading and
writing files, while `ZipFileManager` handles ZIP compression and decompression. This adheres to the SRP, making the
code more focused and maintainable.

### 2. Open/Closed Principle (OCP)

**Before Adhering (`Shape` Class with Conditional Logic):**

```python
from math import pi


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius ** 2
```

The initial `Shape` class contains conditional logic to differentiate between shapes (e.g., rectangles and circles) and
calculate their areas. This design is not closed for modification, violating the OCP, as adding new shapes would require
changing the class.
**After Adhering (Abstract Base Class `Shape` and Concrete Subclasses):**

```python
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
```

After refactoring, an abstract base class `Shape` is introduced. It defines a common interface for shapes but leaves the
specific area calculation to subclasses. New shapes like `Circle` and `Rectangle` inherit from `Shape`, allowing for
easy extension without modifying existing code, adhering to the OCP.

### 3. Liskov Substitution Principle (LSP)

**Before Adhering (`Square` Class Inheriting from `Rectangle`):**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value
```

Initially, a `Square` class inherits from `Rectangle`, implying that a `Square` is a type of `Rectangle`. However, this
violates the Liskov Substitution Principle because changing the dimensions of a `Square` object in a way that would be
valid for a `Rectangle` might lead to unexpected behavior.

**After Adhering (Common Abstract Base Class `Shape`):**

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
```

The improved design introduces a common abstract base class `Shape` for both `Rectangle` and `Square`. They share a
common interface for area calculation, but they are not related through inheritance. This adheres to the LSP because
now `Rectangle` and `Square` are treated as separate entities with shared behavior.

### 4. Interface Segregation Principle (ISP)

**Before Adhering (`Printer` Interface with Unused Methods):**

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

The initial code defines a single large `Printer` interface with three methods: `print`, `fax`, and `scan`. However, not
all printer implementations need all these methods, causing clients to depend on methods they don't use, violating the
ISP.

**After Adhering (Segregated Interfaces `Printer`, `Fax`, and `Scanner`):**

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

In the improved code, interfaces (`Printer`, `Fax`, and `Scanner`) are segregated into smaller, more focused interfaces.
Classes can implement only the interfaces they need, adhering to the ISP. This design promotes flexibility and avoids
forcing classes to implement unnecessary methods.

### 5. Dependency Inversion Principle (DIP)

**Before Adhering (Direct Dependency in `FrontEnd`):**

```python
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
```

The initial code has a `FrontEnd` class directly dependent on the concrete `BackEnd` class. This tight coupling makes it
challenging to extend or replace components without modifying `FrontEnd`, violating the DIP.
**After Adhering (Dependency on Abstractions with `DataSource`):**

```python
from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, data_source: "DataSource"):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"
```

In the improved code, the `FrontEnd` class depends on the abstract `DataSource` interface instead of a concrete class.
This adheres to the DIP, promoting loose coupling and allowing for different data sources (`Database` and `API`) to be
used interchangeably without modifying `FrontEnd`.

---
