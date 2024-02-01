# Фильтрация объектов модели
# Для фильтрации объектов модели по заданным условиям можно использовать
# метод "filter()" класса модели. Метод "filter()" возвращает все объекты модели,
# удовлетворяющие заданным условиям.
# Например, чтобы получить всех пользователей старше <age> лет, мы можем
# использовать следующий код в файле
# myapp2/management/commands/get_user_age_greater.py:
from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    help = "Get user with age greater <age>."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')
# Здесь мы используем оператор "__gt" для сравнения значения поля "age" с
# заданным значением.
# Помимо оператора __gt существуют множество других. Перечислим
# некоторые часто используемые:
# ● exact - точное совпадение значения поля
# ● iexact - точное совпадение значения поля без учета регистра
# ● contains - значение поля содержит заданный подстроку
# ● icontains - значение поля содержит заданный подстроку без учета
# регистра
# ● in - значение поля находится в заданном списке значений
# ● gt - значение поля больше заданного значения
# ● gte - значение поля больше или равно заданному значению
# ● lt - значение поля меньше заданного значения
# ● lte - значение поля меньше или равно заданному значению
# ● startswith - значение поля начинается с заданной подстроки
# ● istartswith - значение поля начинается с заданной подстроки без учета
# регистра
# ● endswith - значение поля заканчивается на заданную подстроку
# ● iendswith - значение поля заканчивается на заданную подстроку без
# учета регистра
# ● range - значение поля находится в заданном диапазоне значений
# ● date - значение поля является датой, соответствующей заданной дате
# ● year - значение поля является годом, соответствующим заданному году
# Как вы догадались, приставка i означает, что поиск будет производиться без
# учета регистра символов. Например, iexact найдет записи с точным
# совпадением значения поля, но не будет учитывать регистр символов при
# поиске.
# Важно! Помните про двойное подчеркивание перед оператором. Например
# для поиска имён начинающихся с S будет использоваться запись вида:
# name__startswith='S'
# Более подробно познакомиться с возможностью фильтров для методов filter(),
# exclude() и get() можно на официальном сайте
# https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
