from django.forms import CharField, Form, IntegerField

class CursoFormulario(Form):
    curso = CharField()
    camada = IntegerField()
    