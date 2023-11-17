from django.db import models
import uuid
# Create your models here.
class MasterRoom(models.Model):
    meeting_id=models.CharField(blank=False,null=False,unique=True,default=uuid.uuid4,editable=False,max_length=10000)
    Rooms_name=models.CharField(blank=False,null=False,max_length=1000)
    def __str__(self):
        return self.Rooms_name
    
class BookingDates(models.Model):
    Booking_Room=models.ForeignKey(MasterRoom,on_delete=models.CASCADE)
    Bookingname=models.CharField(blank=False,null=False,max_length=1000)
    Starting_Time=models.DateTimeField(blank=False,null=False)
    Ending_Time=models.DateTimeField(blank=False,null=False)
    Purpose_of_meeting=models.CharField(blank=False,null=False,max_length=1000)

    def __str__(self):
        return f"{self.Booking_Room} - {self.Bookingname}"