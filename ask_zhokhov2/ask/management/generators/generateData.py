from django.core.management.base import BaseCommand, CommandError

from ask.models import (
    User,
    Tag,
    Question,
    Answer,
    Like
)

import random


class Command(BaseCommand):
    GENERATION_ORDER = 1

    def handle(self, *args, **options):
        # self.generate_users()
        # self.generate_tags()
        # self.generate_questions()
        self.generate_answers()
        self.generate_likes()

    def generate_users(self):
        users = []
        for i in range(self.GENERATION_ORDER):
            u = User()
            u.username = f'User{i}'
            u.email = f'{i}@example.com'
            u.password = "123"
            users.append(u)
        User.objects.bulk_create(users)

    def generate_tags(self):
        tags = []
        for i in range(self.GENERATION_ORDER):
            t = Tag()
            t.title = f'tag{i}'
            tags.append(t)
        Tag.objects.bulk_create(tags)

    def generate_questions(self):
        questions = []
        for i in range(self.GENERATION_ORDER * 10)
            author = random.choice(User.objects.all())
            q = Question()
            q.title = f'Question {i}'
            q.text = f'How to do the {i} task?'
            q.author = author
            q.save()
            q.tags.add(random.choice(Tag.objects.all()))
            questions.append(q)
        Question.objects.bulk_create(questions)

    def generate_answers(self):
        author = random.choice(User.objects.all())
        for i in range(GENERATION_ORDER * 100):
            answer = Answer()
            answer.text = f'answer {i}'
            answer.author = author
            answer.question = random.choice(Question.objects.all())
            answer.save()

    def generate_likes(self):
        for i in range(GENERATION_ORDER * 200):
            like = Like()
