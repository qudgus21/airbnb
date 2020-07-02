from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):
    """ Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    commuication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.commuication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 1)
        ##둘째자리까지 반올림(내장)
        # admin에 rating_average등록해주는 것과 같은 기능 ==  여기다가 rating_average.short_description  = "AVG"

