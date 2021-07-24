from django.urls import path, include
from .views import IndexTemplateView, ContactFormView, ThankYouTemplateView

app_name = 'core'

urlpatterns = [
    # path('',IndexTemplateView.as_view(), name='home'),
    # path('books/', include('books.urls'), name='books'),
    path('',include('books.urls'), name='home'),
    path('contact-us/', ContactFormView.as_view(), name='contact'),
    path('thank-you.html/', ThankYouTemplateView.as_view(), name='thank-you'),
]