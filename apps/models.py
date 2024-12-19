from django.db.models import IntegerField, DateTimeField, Model, ForeignKey, SET_NULL, TextField, BooleanField, CASCADE
from django.db.models.enums import TextChoices
from django.forms.fields import CharField
from parler.models import TranslatableModel

from managment.models import Route
from payment.models import Orders


class Discount(Model,TranslatableModel):
    class DiscountType(TextChoices):
        PERCENTAGE = 'percentage', 'PERCENTAGE'
        FIXED = "fixed", "FIXED"

    code = CharField(max_length=50)
    discount_type = CharField(choices=DiscountType.choices)
    discount_value = IntegerField()
    valid_from = DateTimeField(auto_now_add=True)
    valid_to = DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.discount_type
    def __str__(self):
        return self.safe_translation_getter(('code','discount_type'), any_language=True)

class Region(Model,TranslatableModel):
    name = CharField(max_length=100)

    # def __str__(self):
    #     return self.name
    def __str__(self):
        return self.safe_translation_getter('name',any_language=True)


class Notifications(Model,TranslatableModel):
    class MessageChoices(TextChoices):
        user = "user", "USER"
        order = "order", "ORDER"

    order_id = ForeignKey(Orders, CASCADE, related_name='notifications')
    type = CharField(max_length=100, choices=MessageChoices, )
    message = TextField()
    created_at = DateTimeField()
    is_read = BooleanField(default=False)

    # def __str__(self):
    #     return self.type
    def __str__(self):
        return self.safe_translation_getter(('type', 'message'), any_language=True)


class Review(Model,TranslatableModel):
    route_id = ForeignKey(Route, SET_NULL, 'reviews')
    ratings = ForeignKey(Route, SET_NULL, 'reviews')
    comment = TextField()
    created_at = DateTimeField(auto_now_add=True)
    order_id = ForeignKey(Orders, SET_NULL, 'reviews')

    def __str__(self):
        return self.safe_translation_getter('comment',any_language=True)
