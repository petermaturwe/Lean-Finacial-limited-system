from django.urls import path, include
from . import views
from django.conf import settings
from .views import B2BPaymentAPIView
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('api/b2b/payment/', B2BPaymentAPIView.as_view(), name='b2b_payment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)