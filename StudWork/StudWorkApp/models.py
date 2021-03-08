from django.db import models

# Create your models here.


class Student (models.Model):
    id_stud = models.AutoField("ID", primary_key=True)
    fio_stud = models.CharField('ФИО', max_length=40)
    login_stud = models.CharField('Логин', max_length=20)
    password_stud = models.CharField('Пароль', max_length=30)

    def __str__(self):
        return self.fio_stud

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Director (models.Model):
    id_dir = models.AutoField("ID", primary_key=True)
    fio_dir = models.CharField('ФИО', max_length=40)
    login_dir = models.CharField('Логин', max_length=20)
    password_dir = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.fio_dir

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class Work (models.Model):
    id_work = models.AutoField('Номер работы', primary_key=True)
    id_dir = models.ManyToManyField(Director)
    id_stud = models.ManyToManyField(Student)
    subject = models.CharField('Дисциплина', max_length=20)
    type = models.CharField('Тип работы', max_length=20)

    def __str__(self):
        return f"Работа номер {str(self.id_work)} по дисциплине {self.subject} ({self.type})"

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Topic (models.Model):
    id_work = models.OneToOneField(Work, on_delete=models.CASCADE, primary_key=True)
    topic_work = models.CharField('Тема работы', default="Тема не выбрана", max_length=60)

    def __str__(self):
        return f"{self.topic_work}"

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class TopicAccept (models.Model):
    id_work = models.OneToOneField(Topic, on_delete=models.CASCADE, primary_key=True)
    topic_accept = models.CharField('Тема утверждена', default="Не утверждено", max_length=20)

    def __str__(self):
        return f"Работа номер {str(self.id_work)} ({self.topic_accept})"

    class Meta:
        verbose_name = 'Состояние темы'
        verbose_name_plural = 'Состояние тем'


class Realisation (models.Model):
    id_work = models.OneToOneField(Work, on_delete=models.CASCADE, primary_key=True)
    github = models.URLField('Сылка на github', max_length=200, blank = True)

    def __str__(self):
        return f"Работа номер {str(self.id_work)} github: {self.github}"

    class Meta:
        verbose_name = 'Сылка на github'
        verbose_name_plural = 'Сылки на github'


class RealisationMark (models.Model):
    id_work = models.OneToOneField(Realisation, on_delete=models.CASCADE, primary_key=True)
    percent_done = models.IntegerField('Процент готовности', default=0)

    def __str__(self):
        return f"Работа номер {str(self.id_work)} работа закончена на: {self.percent_done}%"

    class Meta:
        verbose_name = 'Процент выполнения'
        verbose_name_plural = 'Процент выполнения'


class Documentation (models.Model):
    id_work = models.OneToOneField(Work, on_delete=models.CASCADE, primary_key=True)
    tz_link = models.URLField('Сылка на ТЗ', max_length=200, blank = True)
    ptz_link = models.URLField('Сылка на РПЗ', max_length=200, blank = True)

    def __str__(self):
        return f"Работа номер {str(self.id_work)} ТЗ: {self.tz_link};          РПЗ: {self.ptz_link}"

    class Meta:
        verbose_name = 'Документация'
        verbose_name_plural = 'Документация'


class DocMark (models.Model):
    id_work = models.OneToOneField(Documentation, on_delete=models.CASCADE, primary_key=True)
    rpz_accept = models.CharField('Выполнено', default="Нет", max_length=20)

    def __str__(self):
        return f"Работа номер {str(self.id_work)} работа выполнена: {self.rpz_accept}"

    class Meta:
        verbose_name = 'Состояние работы'
        verbose_name_plural = 'Состояние работ'
