from django.db import models

# Create your models here.
# Note: any foreign key will add the suffix "_id" to the column name
# The id member belongs to the Model class that is inherited

class Language(models.Model):
    lang = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.lang}"


class Verb(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    verb = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: Language: {self.lang}, Verb: {self.verb}"


class Tense(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    tense = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tense}"


class Subject(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: Language: {self.lang}, Subject: {self.subject}"


class Conjugation(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    tense = models.ForeignKey(Tense, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    conj = models.CharField(max_length=200)

    def __str__(self):
        return f"""{self.conj}"""