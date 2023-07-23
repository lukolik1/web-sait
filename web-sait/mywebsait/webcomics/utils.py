from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
		{'title': "Обратная связь", 'url_name': 'contact'},
		{'title': "Новостной блок", 'url_name': 'news'},
		

]

class DataMixin:
	def get_user_context(self, **kwargs):
		context = kwargs
		cats = Category.objects.all()
		context['menu'] = menu
		context['cats'] = cats
		if 'cat_selected' not in context:
			context['cat_selected'] = 0
		return context