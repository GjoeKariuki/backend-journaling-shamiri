from django.urls import path
from knox import views as knox_views
from users.views import Registration, Login
from users.views import user_list,user_detail,change_password





urlpatterns = [
    path('register/',Registration.as_views()),
    path('login/', Login.as_view()),
    path('logout/',knox_views.LogoutView.as_view()),
    path('user/', user_list),
    path('user/<str:pk>/',user_detail),
    path('change-password', change_password),

]