from random import choices

from django.core.management.base import BaseCommand
from myapp_3.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}',
                            email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()
