from django.contrib import admin
from headlines import models
# Register your models here.
class HeadlineAdmin(admin.ModelAdmin):

    list_display = ['headline', 'dateposted']

admin.site.register(models.Headline)
