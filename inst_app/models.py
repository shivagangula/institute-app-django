from django.db import models
from multiselectfield import MultiSelectField

class RegData(models.Model):
    frist_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    username   = models.CharField(max_length=20)
    password1  = models.CharField(max_length=20)
    password2  = models.CharField(max_length=20)
    email      = models.EmailField(max_length=50)
    mobile     = models.IntegerField()
    dob        = models.DateTimeField()

class CountClickData(models.Model):
    count = models.IntegerField( default = 1)

class StudentData(models.Model):
    name           = models.CharField(max_length=20)
    mobile         = models.IntegerField()
    email          = models.EmailField(max_length=50)
    COURSE_CHOICES =(
                        ('python','PYTHON'),
                        ('django','DJANGO'),
                        ('rest API','REST API'),
                        ('UI','UI')
                                   )
    courses = MultiSelectField(max_length=200,choices=COURSE_CHOICES)
    TRAINER_CHOICES = (
                           ('sai','SAI'),
                           ('shiva','SHIVA'),
                           ('ganesh','GANESH'),
                           ('mahesh','MAHESH')
                                   )
    trainer = MultiSelectField(max_length=200,choices=TRAINER_CHOICES)
    TIMING_CHOICES = (
                           ('morning','MORNING'),
                           ('afternoon','AFTERNOON'),
                           ('evening','EVENINHG')
                                    )
    timings = MultiSelectField(max_length=200,choices=TIMING_CHOICES)
    start_date = models.DateField()


class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    time = models.DateTimeField()
    feedback = models.CharField(max_length=200)
