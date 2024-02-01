# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world!")
#
#
# def about(request):
#     return HttpResponse("About us")

# Примеры использования логирования в Django
# Для использования логирования в Django необходимо импортировать модуль
# logging и создать объект логгера.
# Пример двух view функций Django с использованием логирования:
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")
# В первой функции index мы просто записываем в лог информацию о том, что
# страница была запрошена. Мы используем логгер info. Сообщение будет
# выведено на консоль.
# Во второй функции about мы используем логгер exception и debug. Если код
# выполняется без ошибок, мы записываем в лог информацию о том, что
# страница была запрошена. Если происходит ошибка, мы записываем в лог
# информацию об ошибке с помощью метода exception, который автоматически
# добавляет трассировку стека. Затем мы возвращаем пользователю сообщение
# об ошибке.
