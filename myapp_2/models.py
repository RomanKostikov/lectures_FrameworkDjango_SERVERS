from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


# Дополнительные возможности моделей
# Связи между моделями
# Отношения между моделями в Django позволяют описывать связи между
# объектами разных моделей. Для этого используются поля моделей, такие как
# ForeignKey, ManyToManyField и OneToOneField.
# Например, у нас есть модель Post и модель Author, и каждый пост может быть
# написан только одним автором, а автор может написать много постов. Для
# этого мы можем использовать поле ForeignKey в модели Post, которое будет
# ссылаться на модель Author.
# Внесём код в models.py учебного приложения:
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'
# Здесь мы создаем модели Author и Post с полями "name", "email", "title",
# "content" и "author". Поле "author" в модели Post является ForeignKey, которое
# ссылается на модель Author.
# Внимание! Не забываем про миграции после изменения файла models.py

# Создание пользовательских методов
# Также мы можем создавать пользовательские методы и свойства для моделей,
# чтобы расширить их функциональность. Например, мы можем создать метод
# "get_summary" для модели "Post", который будет возвращать краткое
# описание поста. Внесём изменения в класс Post в файле models.py:
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'

# Здесь мы создаем метод "get_summary", который возвращает первые 12 слов
# контента поста и добавляет многоточие в конце.
# ...
# text = '\n'.join(post.get_summary() for post in posts)
# ...
# Вместо полного текста теперь можем получать первые несколько слов.
# Django не ограничивает разработчика не методы внутри моделей. Подобный
# подход, когда данные и расчёты производятся в моделях более
# предпочтителен, чем расчёты внутри представлений по выгруженным из
# модели данным. Тем более не стоит переносить расчёты в представления, о
# которых мы будем подробно говорить на следующей лекции.
