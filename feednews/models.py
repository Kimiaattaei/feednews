from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=1000)
    logo = models.ImageField()
    url = models.URLField(max_length=1000)
    datetime_format = models.CharField(max_length=1000)


class News(models.Model):
    createdate = models.DateTimeField()
    summary = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=1000)
    agency = models.ForeignKey(to=Agency, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        ordering = ('createdate',)
