from rest_framework import serializers
from posts import models as posts_models

class QnABaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts_models.QnA
        fields = "__all__"
        depth = 1

class CommentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts_models.Comment
        fields = "__all__"

class QnASerializer(QnABaseSerializer):
    class Meta(QnABaseSerializer.Meta):
        fields = ["id","writer","created","title","category","message","email","comment"]

class FAQBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts_models.FAQ
        fields = "__all__"




