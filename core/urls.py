from django.urls import path, include
from .views import IndexTemplateView

app_name = 'core'

urlpatterns = [
    # path('',IndexTemplateView.as_view(), name='home'),
    path('',include('books.urls'), name='home'),
    # path('books/', include('books.urls'), name='books'),
]