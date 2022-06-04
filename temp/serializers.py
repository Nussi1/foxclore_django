from rest_framework import serializers
from .models import Blog

class BlogDetailSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Blog
        fields = '__all__'