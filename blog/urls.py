from django.urls import path,include
import blog.views as views

urlpatterns = [
    path("",views.show_home,name="home"),
    path("register/",views.register,name="register"),
    path("diary/",views.show_diary,name="diary"),
    path("fortune/",views.show_fortune,name="fortune"),
]


