from django.db import models
from django.urls import reverse

class Comics(models.Model):
	title = models.CharField(max_length=100, verbose_name='Заголовок')
	slug = models.SlugField(max_length=255,unique=True, db_index=True, verbose_name='URL')
	photo = models.ImageField(upload_to="picture/%y/%m/%d/", verbose_name='Фотография')
	file_pdf = models.FileField(upload_to="file/%y/%m/%d/", verbose_name='Файлы')
	content = models.TextField(blank=True, verbose_name='Описание')
	time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновление')
	time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
	is_published = models.BooleanField(default=True, verbose_name='Существует/Несуществует')
	cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})

	class Meta:
		verbose_name = 'Комиксы'
		verbose_name_plural = 'Комиксы'
		ordering = ['id']


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
	slug = models.SlugField(max_length=255,unique=True, db_index=True, verbose_name='URL')
 
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_slug': self.slug})

	class Meta:
		verbose_name = 'Категории'
		verbose_name_plural = 'Категории'
		ordering = ['id']



