
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('sign-up', views.signUp, name = 'signUp'),
    path('login', views.login_page, name = 'login'),
    path('logout', views.logout_page, name = 'logout'),
    path('predict', views.prediction_page, name='predict'),
    path('sell', views.selling_page, name='sell'),
    path('about', views.about_page, name='about'),
    path('contact', views.contact_page, name='contact'),
    # path('<int:pk>', views.deleteStu, name = 'deletepage'),
    # path('updateStudent/<int:pk>', views.updateStud, name="update")
]
