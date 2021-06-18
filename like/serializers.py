from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        field = "__all__"
