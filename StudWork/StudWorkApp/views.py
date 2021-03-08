from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.forms.models import model_to_dict
from django.views.generic import DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import WorkForm, DirectorForm, StudentForm, TopicForm, DocumentationForm, RealisationForm, TopicAcceptForm, DocMarkForm, RealisationMarkForm
from .models import Work, Director, Student, Topic, Documentation, Realisation, TopicAccept, DocMark, RealisationMark

import docxtpl

@login_required
def v_student(request):
    ID_S = Student.objects.get(login_stud=request.user.get_username())
    works = Work.objects.filter(id_stud=ID_S)
    w_form = works

    date = {
        'works': works
    }
    return render(request, 'StudWorkApp/Student/Student.html', date)


@login_required
def v_student_edit(request, pk):
    if request.method == 'POST':
        try:
            t_form = Topic()
            t_form.id_work = Work.objects.get(id_work=pk)
            t_form.topic_work = request.POST.get('topic_work')
            t_form.save()

            r_form = Realisation()
            r_form.id_work = Work.objects.get(id_work=pk)
            r_form.github = request.POST.get('github')
            r_form.save()

            d_form = Documentation()
            d_form.id_work = Work.objects.get(id_work=pk)
            d_form.tz_link = request.POST.get('tz_link')
            d_form.ptz_link = request.POST.get('ptz_link')
            d_form.save()
        except:
            pass


    work = Work.objects.filter(id_work=pk)
    topic = Topic.objects.filter(id_work__in=work)
    real = Realisation.objects.filter(id_work__in=work)
    doc = Documentation.objects.filter(id_work__in=work)

    try:
        t_form = TopicForm(initial={'topic_work': topic.values('topic_work')[0]['topic_work']})
        r_form = RealisationForm(initial={'github': real.values('github')[0]['github']})
        d_form = DocumentationForm(initial={'tz_link': doc.values()[0]['tz_link'], 'ptz_link': doc.values('ptz_link')[0]['ptz_link']})
    except:
        r_form = RealisationForm()
        d_form = DocumentationForm()
        t_form = TopicForm()

    data = {
        'subject': work.values()[0]['subject'],
        'type_work': work.values()[0]['type'],
        'id_work': work.values()[0]['id_work'],
        't_form': t_form,
        'r_form': r_form,
        'd_form': d_form,
    }
    return render(request, 'StudWorkApp/Student/Student_edit.html', data)



@login_required
def v_director(request):
    id_D = Director.objects.get(login_dir=request.user.get_username())
    works_D = Work.objects.filter(id_dir=id_D)
    id_S = Student.objects.all()
    works_S = Work.objects.filter(id_stud__in=id_S)
    works = works_S & works_D
    works_v = works.values('id_stud')

    students =[]
    for c, el in enumerate(works_v):
        id = el['id_stud']
        students.append(Student.objects.get(id_stud__exact=id))
    students_set = set(students)

    date = {
        'students': students_set,
    }
    return render(request, 'StudWorkApp/Director/Director.html', date)

@login_required
def v_director_list_work(request, pk):
    ID_D = Director.objects.get(login_dir=request.user.get_username())
    work_D = Work.objects.filter(id_dir=ID_D)
    ID_S = Student.objects.filter(id_stud=pk)
    work_S = Work.objects.filter(id_stud__in=ID_S)

    work = work_D & work_S
    date = {
        'works': work,
    }
    return render(request, 'StudWorkApp/Director/Director_edit.html', date)

@login_required
def v_director_edit_work(request, pk):
    msg = ''
    if request.method == 'POST':
        try:
            r_form = RealisationMark()
            r_form.id_work = Realisation.objects.get(id_work=pk)
            r_form.percent_done = request.POST.get('percent_done')
            r_form.save()

            t_form = TopicAccept()
            t_form.id_work = Topic.objects.get(id_work=pk)
            t_form.topic_accept = request.POST.get('topic_accept')
            t_form.save()

            d_form = DocMark()
            d_form.id_work = Documentation.objects.get(id_work=pk)
            d_form.rpz_accept = request.POST.get('rpz_accept')
            d_form.save()
        except:
            msg = "Кажется студент ещё не выполнил задание (Его тема, ссылка на работу или документы пусты)"

    work = Work.objects.filter(id_work=pk)
    real = Realisation.objects.filter(id_work__in=work)
    topic = Topic.objects.filter(id_work__in=work)
    doc = Documentation.objects.filter(id_work__in=work)


    try:
        real_f = real.values()[0]['github']
    except:
        real_f = ''


    try:
        real_p = RealisationMark.objects.filter(id_work__in=real)
        r_form = RealisationMarkForm(initial={'percent_done': real_p.values('percent_done')[0]['percent_done']})

        topic_p = TopicAccept.objects.filter(id_work__in=topic)
        t_form = TopicAcceptForm(initial={'topic_accept': topic_p.values('topic_accept')[0]['topic_accept']})

        doc_p = DocMark.objects.filter(id_work__in=doc)
        d_form = DocMarkForm(initial={'rpz_accept': doc_p.values('rpz_accept')[0]['rpz_accept']})
    except:
        r_form = RealisationMarkForm()
        t_form = TopicAcceptForm()
        d_form = DocMarkForm()


    date = {
        'subject': work.values()[0]['subject'],
        'type_work': work.values()[0]['type'],
        'id_work': work.values()[0]['id_work'],
        'github': real_f,
        'r_form': r_form,
        't_form': t_form,
        'd_form': d_form,
        'msg': msg
    }

    return render(request, 'StudWorkApp/Director/Dir/Director_edit_work.html', date)


@login_required
def v_admin(request):
    error = ''
    if request.method == 'POST':
        s_add = StudentForm(request.POST)
        d_add = DirectorForm(request.POST)
        w_add = WorkForm(request.POST)
        if s_add.is_valid():
            user = User.objects.create_user(request.POST['login_stud'], None, request.POST['password_stud'])
            group = Group.objects.get(name='student')
            group.user_set.add(user)
            user.save()
            s_add.save()

        if d_add.is_valid():
            user = User.objects.create_user(request.POST['login_dir'], None, request.POST['password_dir'])
            group = Group.objects.get(name='director')
            group.user_set.add(user)
            user.save()
            d_add.save()

        if w_add.is_valid():
            w_add.save()
        return HttpResponseRedirect("./")
    else:
            error = "Ytdthyj"

    students = Student.objects.all()
    directors = Director.objects.all()
    works = Work.objects.all()

    w_form = WorkForm
    d_form = DirectorForm
    s_form = StudentForm

    date = {
        'directors': directors,
        'students': students,
        'works': works,
        'w_form': w_form,
        'd_form': d_form,
        's_form': s_form,
    }
    return render(request, 'StudWorkApp/Admin/Admin.html', date)


@login_required
def ad_list(request):
    dir = Director.objects.all()
    date = {
        'dir': dir,
    }
    return render(request, 'StudWorkApp/Admin/ad_list.html', date)

@login_required
def ad_list_s(request, pk):
    id_D = Director.objects.get(id_dir=pk)
    works_D = Work.objects.filter(id_dir=id_D)
    id_S = Student.objects.all()
    works_S = Work.objects.filter(id_stud__in=id_S)
    works = works_S & works_D
    works_v = works.values('id_stud')

    students =[]
    for c, el in enumerate(works_v):
        id = el['id_stud']
        students.append(Student.objects.get(id_stud__exact=id))
    students_set = set(students)

    date = {
        'students': students_set,
    }
    return render(request, 'StudWorkApp/Admin/Adm/ad_list_s.html', date)



def gen_tz_d(request, pk):
    doc = docxtpl.DocxTemplate(r"C:\Users\mrnik\Downloads\StudWork\StudWork\StudWorkApp\tz.docx")
    work = Work.objects.filter(id_work=pk)

    student = Student.objects.get(id_stud = work.values('id_stud')[0]['id_stud'])
    director = Director.objects.get(id_dir=work.values('id_dir')[0]['id_dir'])
    try:
        topic = Topic.objects.get(id_work=work.values('id_work')[0]['id_work'])
    except:
        topic = "Тема не указана"
    context = {
            'type':    work.values()[0]['type'],
            'subject': work.values()[0]['subject'],
            'fio_s':   student,
            'topic':   topic,
            'director': director,
            'student': student
    }
    doc.render(context)
    doc.save(r"C:\Users\mrnik\Downloads\StudWork\TZ_"+str(student)+str(work.values()[0]['subject'])+str(topic)+".docx")
    return HttpResponseRedirect('../../../../director/dir/' + str(pk))


def gen_kp_d(request, pk):
        doc = docxtpl.DocxTemplate(r"C:\Users\mrnik\Downloads\StudWork\StudWork\StudWorkApp\kp.docx")
        work = Work.objects.filter(id_work=pk)

        student = Student.objects.get(id_stud=work.values('id_stud')[0]['id_stud'])
        director = Director.objects.get(id_dir=work.values('id_dir')[0]['id_dir'])
        try:
            topic = Topic.objects.get(id_work=work.values('id_work')[0]['id_work'])
        except:
            topic = "Тема не указана"
        context = {
            'subject': work.values()[0]['subject'],
            'fio_s': student,
            'topic': topic,
            'director': director,
        }
        doc.render(context)
        doc.save(r"C:\Users\mrnik\Downloads\StudWork\KP_"+str(student)+str(work.values()[0]['subject'])+str(topic)+".docx")
        return HttpResponseRedirect('../../../../director/dir/'+str(pk))

def gen_tz_s(request, pk):
    doc = docxtpl.DocxTemplate(r"C:\Users\mrnik\Downloads\StudWork\StudWork\StudWorkApp\tz.docx")
    work = Work.objects.filter(id_work=pk)

    student = Student.objects.get(id_stud = work.values('id_stud')[0]['id_stud'])
    director = Director.objects.get(id_dir=work.values('id_dir')[0]['id_dir'])
    try:
        topic = Topic.objects.get(id_work=work.values('id_work')[0]['id_work'])
    except:
        topic = "Тема не указана"
    context = {
            'type':    work.values()[0]['type'],
            'subject': work.values()[0]['subject'],
            'fio_s':   student,
            'topic':   topic,
            'director': director,
            'student': student
    }
    doc.render(context)
    doc.save(r"C:\Users\mrnik\Downloads\StudWork\TZ_"+str(student)+str(work.values()[0]['subject'])+str(topic)+".docx")
    return HttpResponseRedirect('../../../../student/' + str(pk))


def gen_kp_s(request, pk):
        doc = docxtpl.DocxTemplate(r"C:\Users\mrnik\Downloads\StudWork\StudWork\StudWorkApp\kp.docx")
        work = Work.objects.filter(id_work=pk)

        student = Student.objects.get(id_stud=work.values('id_stud')[0]['id_stud'])
        director = Director.objects.get(id_dir=work.values('id_dir')[0]['id_dir'])
        try:
            topic = Topic.objects.get(id_work=work.values('id_work')[0]['id_work'])
        except:
            topic = "Тема не указана"
        context = {
            'subject': work.values()[0]['subject'],
            'fio_s': student,
            'topic': topic,
            'director': director,
        }
        doc.render(context)
        doc.save(r"C:\Users\mrnik\Downloads\StudWork\KP_"+str(student)+str(work.values()[0]['subject'])+str(topic)+".docx")
        return HttpResponseRedirect('../../../../student/'+str(pk))


def switch_control(request):
    info = request.user.groups.get()
    date = {
        'info': info,
    }
    if info.id == 7:
        return HttpResponseRedirect('/administrotor')
    elif info.id == 8:
        return HttpResponseRedirect('/student')
    elif info.id == 9:
        return HttpResponseRedirect('/director')
    return render(request, 'StudWorkApp/index.html', date)
