from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login

from .models import *
from .utils  import *
from .forms  import *





class ComicsHome(DataMixin, ListView):
	paginate_by = 1
	models = Comics
	template_name = 'comics/index.html'
	context_object_name = 'posts'
	

	def get_context_data(self, *, object_list=None, **kawrgs):
		context = super().get_context_data(**kawrgs)
		c_def = self.get_user_context(title='Интернет комиксы')
		return dict(list(context.items()) + list(c_def.items()))

	def get_queryset(self):
		return Comics.objects.filter(is_published=True).select_related('cat')




# def index(request):
# 	posts = Comics.objects.all()
	
# 	context = {
# 		'posts': posts,
# 		'menu': menu,
# 		'title': 'Интернет комиксы',
# 		'cat_selected': 0,
# 	}


# 	return render(request, 'comics/index.html', context=context)

def about(request):
	ontact_list = Comics.objects.all()
	paginator = Paginator(ontact_list, 2)
	
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'comics/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


class ContactFormView(DataMixin, FormView):
	form_class = ContactForm
	template_name = 'comics/contact.html'
	success_url = reverse_lazy('home')


	def get_context_data(self, *, object_list=None, **kawrgs):
		context = super().get_context_data(**kawrgs)
		c_def = self.get_user_context(title='Обратная связь')
		return dict(list(context.items()) + list(c_def.items()))

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('home')




# def contact(request):
# 	return HttpResponse("Контакты")

def news(request):
	return HttpResponse("Новости")

# def login(request):
# 	return HttpResponse("Авторизация")


def pageNotFound(request, exception):
	return HttpResponse('<h1>Страница не найдена</h1>')





class ComicsCategory(DataMixin, ListView):
	model = Comics
	template_name = 'comics/index.html'
	context_object_name = 'posts'
	allow_empty = False

	def get_queryset(self):
		return Comics.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


	def get_context_data(self, *, object_list=None, **kawrgs):
		context = super().get_context_data(**kawrgs)
		c = Category.objects.get(slug=self.kwargs['cat_slug'])
		c_def = self.get_user_context(title='Категория - ' + str(c.name),
									  cat_selected=c.pk)
		return dict(list(context.items()) + list(c_def.items()))




	# def get_context_data(self, *, object_list=None, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['menu'] = menu
	# 	context['title'] = 'Категория - ' + str(context['posts'][0].cat)
	# 	context['cat_selected'] = context['posts'][0].cat_id
	# 	return context


# def show_category(request, cat_id):
# 	posts = Comics.objects.filter(cat_id=cat_id)
	

# 	if len(posts) == 0:
# 		raise Http404()

# 	context = {
# 		'posts': posts,
# 		'menu' : menu,
# 		'title': "Отображение страниц комикса",
# 		'cat_selected': cat_id

# 	}

# 	return render(request, 'comics/index.html', context=context)


class ShowPost(DataMixin, DetailView):
	model = Comics
	template_name = 'comics/posts.html'
	slug_url_kwarg = 'post_slug'
	context_object_name = 'post'


	def get_context_data(self, *, object_list=None, **kawrgs):
		context = super().get_context_data(**kawrgs)
		c_def = self.get_user_context(title=context['post'])
		return dict(list(context.items()) + list(c_def.items()))


	# def get_context_data(self, *, object_list=None, **kawrgs):
	# 	context = super().get_context_data(**kawrgs)
	# 	context['menu'] = menu
	# 	context['title'] = context['post']
	# 	return context










# def show_post(request, post_slug):
# 	posts = get_object_or_404(Comics, slug=post_slug)
	



# 	context = {
# 		'post': posts,
# 		'menu' : menu,
# 		'title': posts.title,
# 		'cat_selected': posts.cat_id
# 	}

# 	return render(request, 'comics/posts.html', context=context)


class RegisterUser(DataMixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'comics/register.html'
	success_url = reverse_lazy('login')

	def get_context_data(self, *, object_list=None, **kawrgs):
		context = super().get_context_data(**kawrgs)
		c_def = self.get_user_context(title='Регистрация')
		return dict(list(context.items()) + list(c_def.items()))

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('home')



class LoginUser(DataMixin, LoginView):
	form_class = LoginUserForm
	template_name = 'comics/login.html'
	success_url = reverse_lazy('login')

	def get_context_data(self, *, object_list=None, **kawrgs):
		context = super().get_context_data(**kawrgs)
		c_def = self.get_user_context(title='Регистрация')
		return dict(list(context.items()) + list(c_def.items()))

	def get_success_url(self):
		return reverse_lazy('home')


def logoutUser(request):
	logout(request)
	return redirect('login')