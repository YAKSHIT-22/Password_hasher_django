from django.shortcuts import render, HttpResponse
from .models import Login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword = make_password(request.POST['password'])
        checkpassword=check_password(request.POST['password'],encryptedpassword)
        data=Login(email=email, password=encryptedpassword)
        data.save()
        #here it saving the data from field directly to the database table
        return render(request, 'index.html', {'encryptedpassword':encryptedpassword,'checkpassword':checkpassword})
    else:
        return render(request, 'index.html')