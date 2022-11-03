from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
<<<<<<< HEAD

    date = models.DateField()

    def __str__(self):
        return self.title
=======
    
    date = models.DateField()
>>>>>>> 3bdcdc1034400883ca1aba4725c23e0524c55afc
