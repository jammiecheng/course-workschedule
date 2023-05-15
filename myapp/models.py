from django.db import models

class staff(models.Model):
    cId = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, null=False)
    sexes = (('M', 'Male'), ('F', 'Female'))
    cSex = models.CharField(choices=sexes,max_length=2,  null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAdd = models.CharField(max_length=255, blank=True, default='')

class time(models.Model):
    weeks = (('Mon.', 'Monday'), ('Tue.', 'Tuesday'), ('Wed.', 'Wednesday'), ('Thu.', 'Thursday'), ('Fri.', 'Friday'), ('Sat.', 'Saturday '),('Sun.', 'Sunday'))
    week = models.CharField(choices=weeks,max_length=15, null=False)
    times = (('1','8:10-9:00'), ('2','9:10-10:00'), ('3','10:20-11:10'), ('4','11:20-12:10'), ('5','12:20-13:10'), ('6','13:20-14:10'), ('7','14:20-15:10'), ('8','15:30-16:20'), ('9','16:30-17:20'))
    time = models.CharField(choices=times,max_length=15, null=False)
    stId = models.ForeignKey(to = "staff",to_field= "cId", on_delete=models.CASCADE)
    