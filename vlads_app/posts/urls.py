from django.urls improt path
from .views import query

urlpatterns=[
path('query',query,name='query'),
  
]
