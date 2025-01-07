from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from ContactoApp.forms import ContactoForm
from .models import Contactos

# Create your views here.

@login_required(login_url="/")
def Register_cont(request):
    form_contacto = ContactoForm(data=request.POST)
    if request.method == "POST":
        if form_contacto.is_valid():
            print(request.POST['nombre_contacto'])
            name = request.POST['nombre_contacto']
            email = request.POST['correo_contacto']
            subject = request.POST['asunt_contacto']
            message = request.POST['msj_contacto']
            template = render_to_string('ContactoApp/email_template.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })
            emailSender = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                # ACA VA EL CORREO O LA LISTA DE CORREOS A LOS QUE QUIERO ENVIAR ESTE EMAIL. PUEDE SER UNO O TANTOS COMO LOS QUE DESEE
                # SI ES UNO SOLO, COLOCO EL CORREO UNICO ENTRE COMILLAS SIMPLES Y NADA MAS. SI AGREGO MÁS TENGO QUE SEPARARLOS CON UNA COMA ','
                ['oacentenom@gmail.com','drajennycarusi@gmail.com']
            )
            emailSender.content_subtype = 'html'
            emailSender.fail_silently = False
            emailSender.send()
            User = request.user
            Contactos.objects.create(usr_contacto=User,nombre_contacto=name,correo_contacto=email,asunt_contacto=subject,msj_contacto=message)
            #messages.success(request, 'El correo electrónico se envió correctamente')
            return redirect("Home")    
    else:
        form_contacto = ContactoForm()
    return render(request, "ContactoApp/Register_cont.html/", {"form":form_contacto})
