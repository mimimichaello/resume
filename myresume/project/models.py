from django.db import models

class Project(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    url = models.URLField('URL')
    date = models.DateTimeField('Дата Публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
