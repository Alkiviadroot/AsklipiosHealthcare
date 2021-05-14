from django.db import models

# Create your models here.

class Asthenia(models.Model):
    onoma=models.CharField(max_length=100)
    orismos=models.TextField()
    
    def __str__(self):
        return f"{self.onoma}"
    
class Xaraktiristika(models.Model):
    asthenia=models.ForeignKey(Asthenia,on_delete=models.CASCADE)
    xaraktiristiko=models.TextField()
    
    def __str__(self):
        return f"{self.asthenia}-Xaraktiristiko_{self.id}"

class Sxoleio(models.Model):
    asthenia=models.ForeignKey(Asthenia,on_delete=models.CASCADE)
    odigia=models.TextField()
    
    def __str__(self):
        return f"{self.asthenia}-odigia_{self.id}"
    
class Ekpedeftikoi(models.Model):
    asthenia=models.ForeignKey(Asthenia,on_delete=models.CASCADE)
    odigia=models.TextField()
    
    def __str__(self):
        return f"{self.asthenia}-odigia_{self.id}"
    
class Goneis(models.Model):
    asthenia=models.ForeignKey(Asthenia,on_delete=models.CASCADE)
    odigia=models.TextField()
    
    def __str__(self):
        return f"{self.asthenia}-odigia_{self.id}"
    
class Perisotera(models.Model):
    asthenia=models.ForeignKey(Asthenia,on_delete=models.CASCADE)
    link=models.URLField()
    
    def __str__(self):
        return f"{self.asthenia}-link_{self.id}"