
from docxtpl import DocxTemplate

doc = DocxTemplate("./tz.docx")
context = {
    'type': 'ООО Ромашка',
    'subject': 'г. Москва, ул. Долгоруковская, д. 0',
    'fio_s': 'ООО Участник',
    'topic': 'г. Москва, ул. Полевая, д. 0',
    'director': 'И.И. Иванов',
    'student': 'Масяня'
}
doc.render(context)
doc.save("final.docx")




