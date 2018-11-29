from django.db import models

class Cert(models.Model):
    description = models.CharField(max_length=254)
    date_aquired = models.DateField()
    date_expired = models.DateField(null=True,
    blank=True)
    link = models.URLField(null=True,
    blank=True)

    def __str__(self):
        return self.description

class OnlineResource(models.Model):
    description = models.CharField(max_length=254)
    link = models.URLField()

    def __str__(self):
        return self.description + " - " + self.link

class Skill(models.Model):
    category = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    years_exp = models.IntegerField(blank=True,
    null=True)
    priority = models.IntegerField()

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.description

class Exp(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True,
    null=True)
    company = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    info = models.TextField()
    duties = models.TextField()

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.company + " - " + self.title

class Edu(models.Model):
    degree = models.CharField(max_length=254)
    school = models.CharField(max_length=254)
    gpa = models.DecimalField(decimal_places=2,
                                max_digits=10)
    grad_date = models.DateField()

    def __str__(self):
        return self.degree