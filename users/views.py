from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from utils.response import success_response, error_response  # assuming this is where your helpers are

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success_response("User registered successfully!", serializer.data, status.HTTP_201_CREATED),
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            error_response("User registration failed!", serializer.errors, status.HTTP_400_BAD_REQUEST),
            status=status.HTTP_400_BAD_REQUEST
        )
