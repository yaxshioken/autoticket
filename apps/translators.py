from django.db import models
from django.db.models.fields import CharField, TextField
from parler.models import TranslatableModel, TranslatedFields
from rest_framework.fields import IntegerField, DateTimeField, BooleanField


class Discount(TranslatableModel):
    translations = TranslatedFields(
        discount_type=models.CharField(max_length=200),
        code=models.CharField(max_length=200)
    )
    discount_value = IntegerField()
    valid_from = DateTimeField(auto_now_add=True)
    valid_to = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.safe_translation_getter(('code','discount_type'), any_language=True)
class Region(TranslatableModel):
    translations=TranslatedFields(
        name=CharField(max_length=200)
    )
    def __str__(self):
        return self.safe_translation_getter('name',any_language=True)
class Notifications(TranslatableModel):
    translations=TranslatedFields(
        type=CharField(max_length=200),
        message=TextField()
    )
    order_id=IntegerField()
    created_at=DateTimeField()
    is_read=BooleanField()
    def __str__(self):
        return self.safe_translation_getter(('type','message'),any_language=True)
class Review(TranslatableModel):
    translations=TranslatedFields(
        comment=TextField()
    )
    route_id=IntegerField()
    ratings=IntegerField()
    created_at=DateTimeField()
    order_id=IntegerField()
