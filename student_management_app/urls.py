from django.urls import path
from . import views
from . import HodViews

urlpatterns = [
  path('darshbord', views.showDemoPage, name="demo"),
  path('', views.ShowLoginPage, name="login"),
  path('doLogin', views.doLogin),
  path('get_user_details', views.GetUserDetails),
  path('logout_user', views.logout_user),
  path('admin_home',HodViews.admin_home)
]
