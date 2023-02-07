from rest_framework import serializers
from ..models import Money

class MoneySerializer(serializers.ModelSerializer):
  class Meta:
    model = Money
    fields = ['id', 'type', 'title', 'amount', 'date']