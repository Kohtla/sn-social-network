import os

from django.core.management.base import BaseCommand, CommandError

from project import settings


class Command(BaseCommand):
    help = 'Создание приложения с правильной архитектурой. Serializers и urls.py'

    @staticmethod
    def create_app_dir(path, dirname):
        dirpath = os.path.join(path, dirname)
        os.mkdir(dirpath)
        open(os.path.join(dirpath, '__init__.py'), 'a').close()

    def create_app(self, appname):
        path = os.path.join(settings.BASE_DIR, appname)
        os.mkdir(path)
        open(os.path.join(path, '__init__.py'), 'a').close()
        file = open(os.path.join(path, 'urls.py'), 'a')
        file.write('''from django.urls import path\n\napp_name = '%s'\n'''%(appname)
                   + '''\n\nurlpatterns = []''')
        file.close()
        file = open(os.path.join(path, 'admin.py'), 'a')
        file.write('from django.contrib import admin')
        file.close()
        file = open(os.path.join(path, 'apps.py'), 'a')
        file.write('''from django.apps import AppConfig\n\n\n'''
                   + '''class TestAppConfig(AppConfig):\n    name = '%s'\n'''%(appname))
        file.close()

        self.create_app_dir(path, 'views')
        self.create_app_dir(path, 'models')
        self.create_app_dir(path, 'serializers')
        self.create_app_dir(path, 'migrations')

    def add_arguments(self, parser):
        parser.add_argument('appname', type=str)

    def handle(self, *args, **options):
        try:
            self.create_app(options['appname'])
            self.stdout.write(self.style.SUCCESS('Приложение создано'))
        except Exception as exception:
            raise CommandError(str(exception))
