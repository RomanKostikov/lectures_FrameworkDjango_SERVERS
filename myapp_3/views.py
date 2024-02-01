from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Post, Author


# Create your views here.
# Представления на основе функций
# Функциональное представление — это функция Python, которая принимает объект
# запроса и возвращает объект ответа. Она может быть определена как обычная
# функция или декоратор. Пример функционального представления:

def hello(request):
    return HttpResponse("Hello World from function!")


# В этом примере мы импортируем класс HttpResponse из модуля django.http и
# определяем функцию hello, которая принимает объект запроса request и
# возвращает объект ответа HttpResponse с текстом "Hello, World!".
# Представления на основе классов
# Классовое представление – это класс Python, который наследуется от базового
# класса View и реализует один или несколько методов для обработки запросов.
# Пример классового представления:


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


# В этом примере мы импортируем базовый класс View из модуля django.views и
# определяем класс HelloView, который наследуется от него. Метод get() класса
# HelloView обрабатывает GET-запросы и возвращает объект ответа HttpResponse с
# текстом "Hello, World!".
# В Django существует множество других типов представлений, таких как шаблонные
# представления, которые используют шаблоны HTML для отображения данных, или
# API-представления, которые возвращают данные в формате JSON или XML. Однако
# функциональные и классовые представления являются наиболее
# распространенными и простыми в использовании.
# Далее в рамках лекции будем использовать различные варианты представлений,
# чтобы на примерах закрепить навыки по их созданию. В реальных проектах стоит
# выбрать единую концепцию для всех представлений вашего проекта.

def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month} / {year} < br > {text}")


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем,"
                   "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp_3/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "myapp_3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp_3/templ_for.html', context)


# В данном примере мы создаем функцию view_for, которая передает список my_list и
# словарь my_dict в контекст шаблона и вызывает рендеринг шаблона
# myapp3/templ_for.html. В шаблоне мы можем использовать тег for для вывода
# элементов списка.

def index(request):
    return render(request, 'myapp_3/index.html')


def about(request):
    return render(request, 'myapp_3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp_3/author_posts.html', {'author': author, 'posts': posts})


# Новая функция get_object_or_404 работает аналогично get, т.е. делает select запрос
# к базе данных. Но если запрос не вернёт строку из таблицы БД, представление
# отрисует страницу с ошибкой 404.
# Также обратите внимание на метод order_by('-id'). После фильтрации статей по
# автору, мы сортируем их на основе id по убыванию. Об этом говорит знак минус
# перед именем. Далее питоновский срез формирует список из пяти статей с
# максимальными идентификаторами.
# Словарь с контекстом в виде автора и списка статей пробрасываются в шаблон
# myapp3/author_posts.html.
# Представление статьи
# Второе представление должно возвращать шаблон с полным текстом статьи:
def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp_3/post_full.html', {'post': post})
# Сделав select запрос к таблице с постами мы передаём в шаблон
# myapp3/post_full.html контекст в виде одной статьи.
