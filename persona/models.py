from django.db import models

class Persona(models.Model):
    
    type_documents = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('RC', 'Registro Civil'),
        ('TI', 'Tarjeta de Identidad'),
    ]
    
    type_document = models.CharField(max_length=2, choices=type_documents, default='CC')
    document_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    hobbie= models.TextField(max_length=200)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos