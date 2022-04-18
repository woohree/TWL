from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 코드 예시
doctor1 = Doctor.objects.create(name='justin')
doctor2 = Doctor.objects.create(name='eric')
patient1 = Patient.objects.create(name='tony', doctor=doctor1)
patient2 = Patient.objects.create(name='harry', doctor=doctor2)
patient3 = Patient.objects.create(name='tony', doctor=doctor2)
patient4 = Patient.objects.create(name='harry', doctor=doctor1, doctor2)
