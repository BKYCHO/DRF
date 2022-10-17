from rest_framework import serializers
from .models import Women

class WomanSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id')