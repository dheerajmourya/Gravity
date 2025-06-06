from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets, permissions
from utils.response import success_response, error_response

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(success_response("Customer list fetched.", serializer.data), status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(customer)
        return Response(success_response("Customer fetched.", serializer.data), status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response("Customer created.", serializer.data), status=status.HTTP_201_CREATED)
        return Response(error_response("Customer creation failed.", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response("Customer updated.", serializer.data), status=status.HTTP_200_OK)
        return Response(error_response("Update failed.", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        self.get_object().delete()
        return Response(success_response("Customer deleted."), status=status.HTTP_204_NO_CONTENT)
