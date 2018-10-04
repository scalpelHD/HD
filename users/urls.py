# 为应用程序users定义URL模式
from django.urls import path
# 导入视图类
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'

# 修改模板路径
LoginView.template_name = 'users/login.html'
urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(), name='login'),
    # 注销
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]