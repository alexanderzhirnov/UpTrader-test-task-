from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse, NoReverseMatch
from django.utils.text import slugify


class Menu(models.Model):
    """Модель для хранения меню"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Название меню')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Уникальный идентификатор')
    
    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """Модель для пунктов меню"""
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='Меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, 
                             related_name='children', verbose_name='Родительский пункт')
    title = models.CharField(max_length=100, verbose_name='Заголовок пункта')
    url = models.CharField(max_length=255, blank=True, verbose_name='Ссылка')
    named_url = models.CharField(max_length=100, blank=True, verbose_name='Именованная ссылка')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    
    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if self.url and self.named_url:
            raise ValidationError('Заполните только одно из полей: URL или именованный URL')
    
    def get_url(self):
        """Возвращает URL для пункта меню"""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'