from django.urls import path, include
from . import views
from django.conf import settings
from .views import B2BPaymentAPIView, PaymentAPIView
from django.conf.urls.static import static 

urlpatterns = [
    path('mpesa-payment/', PaymentAPIView.as_view(), name='mpesa_payment'),
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('asset/', views.asset, name='asset'),
    path('client/', views.client, name='client'),
    path('stk/', views.stk, name='stk'),
    path('adddebtor/', views.adddebtor, name='adddebtor'),
    path('api/b2b/payment/', B2BPaymentAPIView.as_view(), name='b2b_payment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)