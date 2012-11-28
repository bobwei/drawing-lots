from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django import forms
from models import Item

from time import mktime
from datetime import datetime

from StringIO import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ("game", "picture")


