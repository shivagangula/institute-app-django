import datetime
from django.shortcuts import render, HttpResponse, redirect
from .models import RegData, StudentData, FeedbackData, CountClickData
from .forms import RegForm, LoginForm, StudentForm, FeedBackForm


def count():
   count1 = CountClickData.objects.filter(pk = 1).values()
   add = count1[0]['count'] + 1
   CountClickData.objects.filter(pk=1).update(count=add)
   return add
visits = count()

def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            frist_name = request.POST.get('frist_name', '')
            last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            mobile = request.POST.get('mobile', '')
            dob = request.POST.get('dob', '')
            data = RegData(
                frist_name=frist_name,
                last_name=last_name,
                username=username,
                password1=password1,
                password2=password2,
                email=email,
                dob=dob,
                mobile=mobile
            )
            data.save()
            form = RegForm()
        return render(request, 'inst_app/reg.html', {'form': form})
    else:
        form = RegForm()
        return render(request, 'inst_app/reg.html', {'form': form})

def Login(request):
         response = None
         if request.method == 'POST':
            print(request.method)
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                user_name = RegData.objects.all().filter(username=username)
                pwd = RegData.objects.all().filter(password1=password)

                print(username, password, user_name, pwd)
                if not user_name and pwd:
                    response = HttpResponse('Invaild User')
                else:
                    response = redirect('/home')
            return response
         else:
            form = LoginForm()
            return render(request, 'inst_app/login.html', {'form':form})


def home(request):
    add = visits
    send = {'visits':add}

    return render(request, 'inst_app/inst_home.html',send)


def services(request):
    add = visits
    send = {'visits':add}
    return render(request, 'inst_app/services.html', send)


def contact(request):
    if request.method == 'post':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name','')
            mobile = form.cleaned_data.get('mobile','')
            email = form.cleaned_data.get('email','')
            courses = form.cleaned_data.get('courses','')
            trainer = form.cleaned_data.get('trainer','')
            timings = form.cleaned_data.get('timings','')
            start_date = form.cleaned_data.get('start_date','')
            data = StudentData(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                trainer=trainer,
                timings=timings,
                start_date=start_date,
            )
            data.save()
            print(data)
            form = StudentForm()
            add = visits
            send={'form':form,'visits':add}
            return render(request,'inst_app/contact.html',send)
    else:
        form = StudentForm()
        add = visits
        send={'form':form,'visits':add}
        return render(request, 'inst_app/contact.html', send)


def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            time = datetime.datetime.now()
            feedback = request.POST.get('feedback','')
            data = FeedbackData(
                name=name,
                rating=rating,
                time=time,
                feedback=feedback
             )
            data.save()
            fdata = FeedbackData.objects.all()
            add = visits
            send ={'form':FeedBackForm(),'data':fdata,'visits':add}
            return redirect('/feedback')
    else:
        fdata = FeedbackData.objects.all()
        add = visits
        send = {'form': FeedBackForm(), 'data': fdata, 'visits':add}
        return render(request, 'inst_app/feedback.html',send)


def gal(request):
    add = visits
    send = {'visits':add}
    return render(request,'inst_app/gal.html',send)
