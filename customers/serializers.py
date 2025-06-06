from rest_framework import serializers
from .models import Customer
import re

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_mobile(self, value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("Enter a valid 10-digit mobile number.")
        return value
