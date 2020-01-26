from django.conf.urls           import url
from django.urls                import path
from .import views
from .models                    import Profile


urlpatterns = [

    path('register'   , views.Regstform , name='register'),
    path('login' , views.Loginform , name='login'),
]

