from django.conf.urls      import url
from django.urls           import path
from django.views.generic  import TemplateView , ListView
from .import views


urlpatterns = [
    path(r''        , views.Main      , name='main'),
    path('result'   , views.Result    , name='result'),
 ]