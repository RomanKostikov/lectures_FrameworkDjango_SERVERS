# Изменение объектов модели, update
# Для изменения объектов модели можно использовать методы поиска get() или
# filter() в сочетании с save() экземпляра класса модели. Например, чтобы
# изменить имя пользователя с заданным id, мы можем использовать
# следующий код в файле myapp2/management/commands/update_user.py::
from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
# Выполним команду
# >python manage.py update_user 2 Smith
# Username: Smith, email: john@example.com, age: 25
# Здесь мы получаем пользователя с первичным ключом 2, изменяем его имя на
# "Smith" и сохраняем изменения в базе данных с помощью метода "save()".
