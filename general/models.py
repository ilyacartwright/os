from django.db import models
from django.utils.translation import gettext_lazy as _

class Courses(models.Model):
    name = models.CharField(_("Название"), max_length=50)
    name_abbreviated = models.CharField(_("Название сокращенное"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Level(models.Model):
    courses = models.ForeignKey("general.Courses", verbose_name=_("Курс"), on_delete=models.CASCADE)
    name = models.CharField(_("Название"), max_length=50)
    number = models.IntegerField(_("Номер"))


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'
        ordering = ['number']


class Themes(models.Model):
    courses = models.ForeignKey("general.Courses", verbose_name=_("Курс"), on_delete=models.CASCADE)
    level = models.ForeignKey("general.Level", verbose_name=_("Уровень"), on_delete=models.CASCADE)
    name = models.CharField(_("Название темы"), max_length=50)
    number = models.IntegerField(_("Номер"))
    quantity = models.IntegerField(_("Количество занятий"))
    text_1 = models.TextField(_("Обратная связь 1"))
    text_2 = models.TextField(_("Обратная связь 2"))
    text_3 = models.TextField(_("Обратная связь 3"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['number']



