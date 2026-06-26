from django.shortcuts import render
from .models import Student


def homepage(request):

    # Existing Data
    name = "Venky"
    place = "Vijayawada"
    hobby = "Cricket"
    fruits = ["Apple", "Banana", "Mango", "Orange"]
    favnum = 7
    favfruit = "Apple"

    # Form Submission
    if request.method == "POST":

        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        state = request.POST.get("state")
        country = request.POST.get("country")
        qualification = request.POST.get("qualification")
        branch = request.POST.get("branch")
        gender = request.POST.get("gender")

        Student.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            password=password,
            dob=dob,
            state=state,
            country=country,
            qualification=qualification,
            branch=branch,
            gender=gender,
        )

        return render(request, "home.html", {
            "name": name,
            "place": place,
            "hobby": hobby,
            "fruits": fruits,
            "favnum": favnum,
            "favfruit": favfruit,

            "success": True,

            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "gender": gender,
        })

    return render(request, "home.html", {
        "name": name,
        "place": place,
        "hobby": hobby,
        "fruits": fruits,
        "favnum": favnum,
        "favfruit": favfruit,
    })