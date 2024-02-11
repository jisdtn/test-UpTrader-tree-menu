from django.db import models


class Menu(models.Model):
    name = models.CharField(
        'Название', max_length=100, unique=True
    )
    description = models.TextField(
        'Описание', max_length=250, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    title = models.CharField(
        'Название элемента', max_length=100, unique=True
    )
    description = models.TextField(
        'Описание элемента', max_length=250, blank=True
    )
    url = models.SlugField(
        'Ссылка', max_length=200, db_index=True, unique=True
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        verbose_name = 'Элементы меню'
        verbose_name_plural = 'Элементы меню'
