from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')


class B2BPaymentAPIView(APIView):
    def post(self, request, *args, **kwargs):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.MPESA_BEARER_TOKEN}'
        }
        payload = request.data

        response = requests.post(
            'https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest',
            headers=headers,
            json=payload
        )
        return Response(response.json())
