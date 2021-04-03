from django.db import models

default_max_length = 50


class Skill(models.Model):
    name = models.CharField(max_length=default_max_length)
    level = models.IntegerField(default=2, choices=((1, 'low'), (2, 'medium'), (3, 'high')))

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=default_max_length)
    title = models.CharField(max_length=default_max_length)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=default_max_length)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
