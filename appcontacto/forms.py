from django import forms

class formulario(forms.Form):

    nombre = forms.CharField(label='nombre', max_length=25, required=True)

    correo = forms.EmailField(label='Correo', required=True)

    Consultas_Y_Preguntas = forms.CharField(widget=forms.Textarea, required=True)