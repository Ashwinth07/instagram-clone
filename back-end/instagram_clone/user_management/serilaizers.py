from .models import User, Comments
from rest_framework import serializers



class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comments
        fields = ["id","user"]

