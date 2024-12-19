from creditcards.models import CardNumberField
from django.db.models import ManyToManyField, Model, EmailField, DateTimeField, IntegerField, CharField, ForeignKey, \
    SET_NULL
from django.db.models.enums import TextChoices
from phonenumber_field.modelfields import PhoneNumberField

from managment.models import Route


class Orders(Model):
    class OrderStatusChoices(TextChoices):
        pending = "pending", "PENDING"
        cancelled = "cancelled", "CANCELLED"
        proccess = "proccess", "PROCCESS"
        done = "done", "DONE"

    email = EmailField()
    phone_number = PhoneNumberField(region='UZ')
    payment_date = DateTimeField(auto_now_add=True)
    card_number = CardNumberField()
    amount = IntegerField()
    status = CharField(max_length=50, choices=OrderStatusChoices.choices)
    tickets = ManyToManyField("Tickets", related_name="orders")

    def __str__(self):
        return self.phone_number


class Tickets(Model):
    class StatusChoice(TextChoices):
        booked = 'booked', "BOOKED"
        paid = "paid", "PAID"
        canceled = "canceled", "CANCELED"

    route_id = ForeignKey(Route, SET_NULL, 'tickets')
    seat_number = IntegerField()
    status = CharField(max_length=100, choices=StatusChoice.choices)
    created_at = DateTimeField(auto_now_add=True)
    orders = ManyToManyField('Orders', related_name="tickets")

    def __str__(self): return self.route_id
