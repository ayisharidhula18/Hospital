from django import forms

from.models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput(),
        }
        labels = {
            'patient_name' : "Patient_Name ",
            'patient_phone' : "Patient_Phone ",
            'patient_email' : "Patient_Email ",
            'doc_name' : "Doctor Name ",
            'booking_date' : "Booking Date ",
           

        }