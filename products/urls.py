from django.urls import path

from products import views

urlpatterns=[

    path('', views.addproduct, name='addproduct'),
    path('<int:myprod_id>', views.pdetails, name= 'pdetails'),
    path('<int:myprod_id>/vote', views.hitlike, name='hitlike'),
    path('<int:myprod_id>/disvote', views.hitdislike, name='hitdislike'),
    path('<int:myprod_id>/delete', views.prodDelete, name='delete'),
    path('about/', views.about, name='about'),
]