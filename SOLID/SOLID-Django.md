# SOLID Django Samples

### [1. Single Responsiblity Principle (SRP)](#1-srp)

Each class must have a single responsibility.

### [2. Open/Closed Principle (OCP)](#2-ocp)

Code should be open for extension but closed for modification.

### [3. Liskov Substitution Principle (LSP)](#3-lsp)

Subtypes must be substitutable for their base types without altering the correctness of the program.

### [4. Interface Segregation Principle (ISP)](#4-isp)

Clients should not be forced to depend on interfaces they do not use.

### [5. Dependency Inversion Principle (DIP)](#5-dip)

Abstractions should not depend on details. Details should depend on abstractions.

#### 1. SRP

```python
# views.py
from django.shortcuts import render
from django.views import View
from .models import Article

class ArticleListView(View):
    template_name = 'articles/list.html'

    def get(self, request):
        articles = Article.objects.all()
        return render(request, self.template_name, {'articles': articles})

```

The `ArticleListView` class adheres to SRP by having a single responsibility: handling the presentation logic for listing articles. It retrieves articles from the `ArticleRepository` and renders them in a template. This focused responsibility makes the code easier to understand, maintain, and test, as it doesn't mix unrelated concerns.

#### 2. OCP

```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)
```

The Open/Closed Principle is illustrated by the introduction of the `PublishedArticle` model. The original `Article` model remains closed for modification, preserving its structure. To extend the behavior with filtering by publication status, a new model, `PublishedArticle`, is created as a subclass, adhering to the open/closed principle. This allows for seamless extension without altering existing code.

#### 3. LSP

```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class PublishedArticle(Article):
    objects = PublishedArticleManager()

    class Meta:
        proxy = True

```

The Liskov Substitution Principle is applied correctly between the `Article` and `PublishedArticle` models. `PublishedArticle` is a subtype of `Article` and is substitutable for the base type. This means that you can use a `PublishedArticle` instance wherever an `Article` instance is expected, without compromising the program's correctness. The inheritance relationship ensures a smooth substitution.

#### 4. ISP

```python
# interfaces.py
from abc import ABC, abstractmethod

class ArticleRepositoryInterface(ABC):
    @abstractmethod
    def get_all_articles(self):
        pass


# repositories.py
from .models import Article

class ArticleRepository(ArticleRepositoryInterface):
    def get_all_articles(self):
        return Article.objects.all()

```

The `ArticleRepositoryInterface` adheres to the Interface Segregation Principle by defining a minimal interface with a single method, `get_all_articles()`. This design ensures that clients, such as the `ArticleListView`, are not forced to depend on interfaces they do not use. The view only depends on the specific method it needs from the repository interface, promoting clean separation of concerns.

#### 5. DIP

```python
# views.py
from django.shortcuts import render
from django.views import View
from .repositories import ArticleRepository, ArticleRepositoryInterface

class ArticleListView(View):
    template_name = 'articles/list.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.article_repository: ArticleRepositoryInterface = ArticleRepository()

    def get(self, request):
        articles = self.article_repository.get_all_articles()
        return render(request, self.template_name, {'articles': articles})

```

Instead of directly depending on a concrete `ArticleRepository`, the `ArticleListView` depends on the `ArticleRepositoryInterface`, an abstraction. This inversion of dependencies decouples the high-level module (`ArticleListView`) from the low-level module (`ArticleRepository`), aligning with DIP. It allows for flexibility in choosing different repository implementations without altering the view, improving code extensibility and maintainability.
