from django.db import models


class Task(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    task = models.TextField("Содержание")
    author = models.CharField("Автор", max_length=35)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
