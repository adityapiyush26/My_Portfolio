from django.shortcuts import render
from Portfolio.models import User
from Portfolio.forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'Portfolio/home.html')

def projects(request):
    return render(request, 'Portfolio/projects.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            p = User(name=name, email=email, message=message)
            p.save()
            return render(request, 'Portfolio/home.html')
    return render(request, 'Portfolio/contact.html', {'form':form})


def resume(request):
    return render(request, 'Portfolio/resume.html')

def users(request):
    user_list = User.objects.order_by('name')
    user_dict = {"users":user_list}
    return render(request,'Portfolio/users.html',context=user_dict)
