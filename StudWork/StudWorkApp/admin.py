from django.contrib import admin
from .models import Student, Director, Documentation, DocMark, Realisation, RealisationMark, Work, Topic, TopicAccept
# Register your models here.

admin.site.register(Student)
admin.site.register(Director)
admin.site.register(Work)
admin.site.register(Topic)
admin.site.register(TopicAccept)
admin.site.register(Documentation)
admin.site.register(DocMark)
admin.site.register(Realisation)
admin.site.register(RealisationMark)
