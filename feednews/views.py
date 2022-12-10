from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News, Agency
import feedparser
from datetime import datetime
from .serializers import NewsSerializerList, AgencySerializerList
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter


@api_view(["POST"])
def update(request):
    agencies = Agency.objects.all()
    for agency in agencies:
        data = feedparser.parse(agency.url)
        data = data["entries"]
        for i in data:
            published = i["published"]
            summary = i.get("summary")
            title = i["title"]
            published = datetime.strptime(published, agency.datetime_format)
            news = News(createdate=published, summary=summary, title=title, agency=agency)
            news.save()
    return Response()


class NewsFilter(filters.FilterSet):

    createdate_big = filters.DateTimeFilter(field_name="createdate", lookup_expr='gte')
    createdate_small = filters.DateTimeFilter(field_name="createdate", lookup_expr='lte')

    class Meta:
        model = News
        fields = ['title', 'agency_id', "createdate"]


class NewsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializerList
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = NewsFilter
    ordering_fields = ['title', 'agency_id', "createdate"]
    ordering = ['createdate']
    search_fields = ['title', "agency__name"]


class AgencyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializerList
    permission_classes = [AllowAny]
