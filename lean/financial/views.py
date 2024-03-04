import os
import uuid
from django.shortcuts import render
from rest_framework import status
from .utils import MpesaGateWay
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import logging 
logger = logging.getLogger(__name__)
# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')


def asset(request):
    return render(request, 'assetmanagement.html')

def client(request):
    return render(request, 'client-detail.html')

def adddebtor(request):
    return render(request, 'add-client.html')

def stk(request):
    return render(request, 'mpesa-payment.html')


class PaymentAPIView(APIView):
 

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        amount = request.data.get('amount', 0)
        account_reference = 'Lean'
        transaction_desc = 'Payment of X'
        callback_url = os.environ.get('MPESA_CALLBACK_URL', 'https://mydomain.com/path')
        
       

        if not phone_number:
            return Response({'message': 'Phone number is missing'}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     phone_number = PhoneNumberField().to_internal_value(phone_number).as_e164
        # except ValidationError:
        #     return Response({'message': 'Phone number is invalid'}, status=status.HTTP_400_BAD_REQUEST)

        #converting the amount to integer
        try:
            amount = int(amount)
        except ValueError:
            return Response({'message': 'Invalid amount format'}, status=status.HTTP_400_BAD_REQUEST)

        if not amount or amount <= 0:
            return Response({'message': 'Amount should be greater than 0'}, status=status.HTTP_400_BAD_REQUEST)

        cl = MpesaGateWay()

        try:
            response = cl.stk_push(phone_number=phone_number, amount=amount, account_reference=account_reference, transaction_desc=transaction_desc, callback_url=callback_url)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error processing Mpesa payment: {e}")
            return Response({'message': 'Error processing payment'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@method_decorator(csrf_exempt, name='dispatch')
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
