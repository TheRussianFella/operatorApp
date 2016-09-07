from django.conf.urls import url



from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/get_orders', views.return_orders, name='get_orders'),
]
