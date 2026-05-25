from django.db import models


class Clinica(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE
    )

    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE
    )

    data_hora = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        default='Pendente'
    )

    def __str__(self):
        return f"{self.paciente.nome} - {self.medico.nome} - {self.data_hora}"

# Create your models here.
