from django.forms import ModelForm, TextInput, NumberInput, URLInput
from django import forms

from .models import Work, Director, Student, Topic, Documentation, Realisation, TopicAccept, DocMark, RealisationMark


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['subject', 'type', 'id_stud', 'id_dir', 'id_work']

    widjets = {
        "subject": TextInput(attrs={'placeholder': 'TYPE'}),
        "type": TextInput(attrs={'placeholder': 'TYPE'}),
        "id_stud": TextInput(attrs={'placeholder': 'TYPE'}),
        "id_dir": TextInput(attrs={'placeholder': 'TYPE'}),
        "id_work": TextInput(attrs={'placeholder': 'TYPE'}),
    }


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['fio_dir', 'login_dir', 'password_dir']

    widjets = {
        "fio_dir": TextInput(attrs={'placeholder': 'TYPE'}),
        "login_dir": TextInput(attrs={'placeholder': 'TYPE'}),
        "password_dir": TextInput(attrs={'placeholder': 'TYPE'})
    }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fio_stud', 'login_stud', 'password_stud']

    widjets = {
        "fio_stud": TextInput(attrs={'placeholder': 'TYPE'}),
        "login_stud": TextInput(attrs={'placeholder': 'TYPE'}),
        "password_stud": TextInput(attrs={'placeholder': 'TYPE'})
    }

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['id_work', 'topic_work']

    widjets = {
        "topic_work": TextInput(attrs={'placeholder': 'TYPE'})
    }


class TopicAcceptForm(ModelForm):
    class Meta:
        model = TopicAccept
        fields = ['topic_accept']

    widjets = {
        "topic_accept": TextInput(attrs={'placeholder': 'TYPE'})
    }


class DocumentationForm(ModelForm):
    class Meta:
        model = Documentation
        fields = ['tz_link', 'ptz_link']

    widjets = {
        "tz_link": URLInput(attrs={'placeholder': 'TYPE'}),
        "ptz_link": URLInput(attrs={'placeholder': 'TYPE'})
    }


class DocMarkForm(ModelForm):
    class Meta:
        model = DocMark
        fields = ['rpz_accept']

    widjets = {
        "rpz_accept": URLInput(attrs={'placeholder': 'TYPE'}),

    }


class RealisationForm(ModelForm):
    class Meta:
        model = Realisation
        fields = ['github']

    widjets = {
        "github": TextInput(attrs={'placeholder': 'TYPE'})
    }


class RealisationMarkForm(ModelForm):
    class Meta:
        model = RealisationMark
        fields = ['percent_done']

    widjets = {
        "percent_done": TextInput(attrs={'placeholder': 'TYPE'})
    }