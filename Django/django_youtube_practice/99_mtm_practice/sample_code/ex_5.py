from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'


# 코드 예시
doctor1 = Doctor.objects.create(name='justin')
patient1 = Patient.objects.create(name='tony')
patient2 = Patient.objects.create(name='harry')

reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()
doctor1.patient_set.all()
patient1.doctors.all()

patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
doctor1.patient_set.all()
patient2.doctors.all()

doctor1.patient_set.remove(patient1)
patient2.doctors.remove(doctor1)
