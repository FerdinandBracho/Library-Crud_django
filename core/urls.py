from django.urls import path, include
from .views import IndexTemplateView, ContactFormView, ThankYouTemplateView
from django.contrib.auth import REDIRECT_FIELD_NAME, views as auth_views

app_name = 'core'

urlpatterns = [
    # path('',IndexTemplateView.as_view(), name='home'),
    # path('books/', include('books.urls'), name='books'),
    path('',include('books.urls'), name='home'),
    path('contact-us/', ContactFormView.as_view(), name='contact'),
    path('thank-you.html/', ThankYouTemplateView.as_view(), name='thank-you'),
    path('account/', include('django.contrib.auth.urls'), name='account'),
    path('account/login', auth_views.LoginView.as_view(extra_context={'nav_text_login':'active'}), name='login'),
    path('account/logout', auth_views.LogoutView.as_view(next_page='books:list'), name='logout'),
]