from django.db import models

class questions(models.Model):
    question=models.TextField(max_length=300)
    asker_email=models.EmailField(blank=True)
    description=models.TextField(max_length=1000)

class anwsers(models.Model):
    question=models.TextField(max_length=300)
    anwserer_email=models.EmailField(blank=True)
    anwser=models.TextField(max_length=10000)
