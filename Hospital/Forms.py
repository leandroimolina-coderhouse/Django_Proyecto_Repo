from django import forms
from Hospital.models import DepartamentoMedico


class DepartamentoMedicoForm(Forms.ModelForm):
    class Meta:
        model = DepartamentoMedico
        fields = [
            "nombre",
            "nro_departamento"
            "email_dpto"
            "nro_empleados"
            "fecha_de_creacion"            
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_departamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_empleados': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_dpto': forms.EmailInput(attrs={'class': 'form-control'}),
        }