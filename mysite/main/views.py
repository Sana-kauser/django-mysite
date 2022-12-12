from django.shortcuts import render
from django.http import HttpResponse
from main.models import Contact
import mysql.connector as sql
# to give http respons

# Create your views here.


def index(response):
    context = {
        "name": "sana",
        "course": "django"
    }
    return render(response, "index.html", context)
# is there any difference between response and request?


def v1(response):
    return HttpResponse("<h1>View 1 !</h1>")


def v2(response):
    return HttpResponse("<h1>Unneccesary view!</h1>")


def contact(request):
    if request.method == "POST":
        global n, e, p, s
        # name = request.POST['name']
        # email = request.POST['email']
        # phone = request.POST['phone']
        # subject = request.POST['subject']
        # # print(name, email, phone, subject)
        # ins = Contact(name=name, email=email, phone=phone, subject=subject)
        # ins.save()
        # print("everything is saved return to db")

        m = sql.connect(host="localhost", user="root",
                        password="sana123", database="mysite")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                n = value
            if key == "email":
                e = value
            if key == "phone":
                p = value
            if key == "subject":
                s = value
        c = "insert into users( '{}','{}','{}','{}' )".format(n, e, p, s)
        cursor.execute(c)
        m.commit()
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html")
