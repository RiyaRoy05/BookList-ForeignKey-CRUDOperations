from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path('',views.index),
    path('second', views.second),

    path('update/<int:id>', views.updateB),
    path('hUpdate/<int:id>', views.hbUp),

     path('hDel/<int:id>', views.hdel),

     path('Details/<int:id>', views.detail),
]
