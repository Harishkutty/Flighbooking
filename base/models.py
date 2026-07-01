from django.db import models


class FlightModel(models.Model):
    flight_company = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_no = models.IntegerField()
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    depature_time = models.TimeField()
    depature_date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.flight_name


class BookingModel(models.Model):
    flight_company = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_no = models.IntegerField()
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    depature_time = models.TimeField()
    depature_date = models.DateField(null= True)
    price = models.IntegerField()

    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=20)
    age = models.IntegerField()
    seat_class = models.CharField(max_length=50)
    seat_no = models.IntegerField()

    def __str__(self):
        return self.passenger_name
    
class ConfirmModel(models.Model):
    flight_company = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_no = models.IntegerField()
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    depature_time = models.TimeField()
    depature_date = models.DateField(null= True)
    price = models.IntegerField()

    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=20)
    age = models.IntegerField()
    seat_class = models.CharField(max_length=50)
    seat_no = models.IntegerField()
    
