from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from workshops.forms import WorkshopRegisterForm
from workshops.models import WorkshopRegister
import zipfile
from cStringIO import StringIO


def workshop(request):
	if request.method == 'POST':
		form = WorkshopRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			workshop = form.save()
			return render(request, 'workshops/success.html', { 'workshop' : workshop })
	else:
		form = WorkshopRegisterForm()

	return render(request, 'workshops/main.html', {'form':form})

def responses(request):
	w_register = WorkshopRegister.objects.order_by('surname')

	return render(request, 'workshops/responses.html', {'responses':w_register})



def return_zipped_file(request):
    response = HttpResponse(mimetype='application/zip')
    response['Content-Disposition'] = 'filename=all_cvs.zip'
    #first assemble your files
    files = []
    for response in WorkshopRegister.objects.all():
        files.append(("%s_%s.pdf" % (response.name,response.surname,), response.cv()))
    #now add them to a zip file
    #note the zip only exist in memory as you add to it
    buffer = StringIO()
    zip = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED)
    for name, f in files:
        zip.writestr(name, f)
    zip.close()
    buffer.flush()
    #the import detail--we return the content of the buffer
    ret_zip = buffer.getvalue()
    buffer.close()
    response.write(ret_zip)
    return response