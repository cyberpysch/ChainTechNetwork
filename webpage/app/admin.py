from django.contrib import admin
from .models import OfferLetter
# Register your models here.

@admin.register(OfferLetter)
class OfferLetterAdmin(admin.ModelAdmin):
    list_display=['role','KRA','phone','salary']