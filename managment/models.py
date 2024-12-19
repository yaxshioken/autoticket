from django.db.models import Model, CharField, IntegerField, DateTimeField, ForeignKey, CASCADE, SET_NULL, DecimalField, \
    EmailField
from django.db.models.enums import TextChoices
from phonenumber_field.modelfields import PhoneNumberField

from apps.models import Region


class Admin(Model):
    class RoleAdminChoices(TextChoices):
        superadmin = "superadmin", "SUPERADMIN"
        moderator = "moderator", "MODERATOR"
        driver = "driver", "DRIVER"
        operator = "operator", "OPERATOR"
        user = "user", "USER"
        practioner = "practioner", "PRACTIONER"

    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone_number = PhoneNumberField(region='UZ', max_length=100)
    username = CharField(max_length=100)
    email = EmailField(max_length=100)
    password = CharField(max_length=255)
    role = CharField(max_length=100, choices=RoleAdminChoices.choices, default=RoleAdminChoices.user)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Transport(Model):
    class TransportChoices(TextChoices):
        bus = "bus", "BUS"
        train = "train", "TRAIN"
        plane = "plane", "PLANE"

    type = CharField(max_length=100, choices=TransportChoices.choices)
    name = CharField(max_length=500)
    capacity = IntegerField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transport(Model):
    class TransportChoices(TextChoices):
        bus = "bus", "BUS"
        train = "train", "TRAIN"
        plane = "plane", "PLANE"

    type = CharField(max_length=100, choices=TransportChoices.choices)
    name = CharField(max_length=500)
    capacity = IntegerField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Station(Model):
    class TypeChoice(TextChoices):
        bus_station = "bus_station", "BUS_STATION"
        airport_station = "airport_station", "AIRPORT_STATION"
        train_station = "train_station", "TRAIN_STATION"

    name = CharField(max_length=100)
    location = CharField(max_length=100)
    type = CharField(max_length=50, choices=TypeChoice.choices)
    region_id = ForeignKey(Region, CASCADE, related_name="stations")

    def __str__(self):
        return self.bus_station


class Route(Model):
    transport = ForeignKey(Transport, SET_NULL, "routes")
    start_location = ForeignKey(Station, SET_NULL, 'routes')
    end_location = ForeignKey(Station, SET_NULL, 'routes')
    departure_time = DateTimeField(auto_now_add=True)
    arrival_time = DateTimeField(auto_now_add=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    platform_number = IntegerField()
    driver_id = ForeignKey(Admin, SET_NULL, 'routes')

    def __str__(self):
        return f"{self.start_location}-{self.end_location}"


class Route_Stations(Model):
    route_id = ForeignKey(Route, SET_NULL, 'route_stations')
    station_id = ForeignKey(Station, SET_NULL, 'route_stations')
    arrival_time = DateTimeField(auto_now=True)
    departure_time = DateTimeField(auto_now=True)

    def __str__(self):
        return self.route_id
