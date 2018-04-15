from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    template = loader.get_template('homepage/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if(username == "manish"):
                    return HttpResponseRedirect('genericviews/')
                else:
                    return HttpResponseRedirect('genericviews/makeentry')
            else:
                messages.error(request, 'Username and Password did not match!!!')

        except auth.ObjectDoesNotExist:
            print('Invalid User!')

    else:
        template = loader.get_template('homepage/index.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

