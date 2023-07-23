from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', ComicsHome.as_view(), name='home'),
	path('about/', about, name='about'),
	path('contact/', ContactFormView.as_view(), name='contact'),
	path('news/', news, name='news'),
	path('login/', LoginUser.as_view(), name='login'),
	path('logout/', logoutUser, name='logout'),
	path('register/', RegisterUser.as_view(), name='register'),
	path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
	path('category/<slug:cat_slug>/', ComicsCategory.as_view(), name='category'),

]