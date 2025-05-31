from django.shortcuts import render
from .models import Feedback
from rest_framework import generics
from .serializers import FeedbackSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dotenv import load_dotenv
import os

load_dotenv()
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer

    def post(self, request):
        data = request.data
        response = supabase.table('feedback').insert(data).execute()

        print(response)

        if(response):
            return Response({"message" : "Feedback added successfully"}, status = 201)
        else:
            return Response({"error": response.json()}, status = 400)
