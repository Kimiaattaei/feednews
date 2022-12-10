from rest_framework import serializers
from .models import News, Agency


class NewsSerializerList(serializers.ModelSerializer):
    class Meta:
        model = News
        ordering = ('createdate',)
        fields = ["createdate", "summary", "title", "agency"]


class AgencySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ["name", "id", "logo"]
