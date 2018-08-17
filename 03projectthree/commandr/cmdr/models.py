from django.db import models

# when I upgrade the models - makemingations & migrate + name app
class Cmdr(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
