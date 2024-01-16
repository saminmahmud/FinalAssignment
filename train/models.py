from django.db import models
from passenger.models import UserAccount
from station.models import Station


class Train(models.Model):
    name = models.CharField(max_length=100)
    start_station = models.ForeignKey(Station, related_name="start_station" , null=True, blank=True, on_delete=models.CASCADE)
    end_station =  models.ForeignKey(Station, related_name="end_station" , null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    def __str__(self) :
        return self.name
    
class Seat(models.Model):
    train = models.ForeignKey(Train, null=True, blank=True, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=3)
    active = models.BooleanField(default=False)
    def __str__(self) :
        return f"{self.train.name} - {self.seat_number} - {self.active}"

class Shedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    train_date = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.train.name} - {self.train_date}"
    
class Review(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviews by {self.name}"


# class BuyTicket(models.Model):
#     train = models.ForeignKey(Train, on_delete=models.CASCADE)
#     account = models.ForeignKey(UserAccount,  on_delete = models.CASCADE)
#     seat = models.ManyToManyField(Seat)

#     def __str__(self):
#         return f"Reviews by {self.account.id} __ {self.train.name}"

# STAR_CHOICES = [
#     ('⭐', '⭐'),
#     ('⭐⭐', '⭐⭐'),
#     ('⭐⭐⭐', '⭐⭐⭐'),
#     ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
#     ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
# ]
# class ReviewAgain(models.Model):
#     train = models.ForeignKey(Train, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    