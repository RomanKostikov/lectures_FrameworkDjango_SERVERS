# Использование QuerySet для получения данных из
# базы данных
# Для получения данных из базы данных мы можем использовать QuerySet,
# который позволяет выполнить различные операции над набором объектов
# модели. Например, чтобы получить все посты, написанные определенным
# автором, мы можем использовать следующий код в файле
# myapp2/management/commands/get_post_by_author_id.py:
from django.core.management.base import BaseCommand
from myapp_2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)
    #         intro = f'All posts of {author.name}\n'
    #         text = '\n'.join(post.content for post in posts)
    #         self.stdout.write(f'{intro}{text}')
    # Здесь мы получаем автора по его id и фильтруем все посты, чтобы получить
    # только те, которые были написаны им.
    # А если нам не нужно имя автора в строке intro, можем изменить запрос к базе
    # данных. Фильтруем посты по автору непосредственно из модели пост:
    # ...
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        # text = '\n'.join(post.content for post in posts)  # old code
        text = '\n'.join(post.get_summary() for post in posts)  # new code
        self.stdout.write(f'{intro}{text}')
# Мы просим найти посты где у поля автор первичный ключ равен pk.
