from django.urls import path


from actsuser import views

urlpatterns = (

    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),


)