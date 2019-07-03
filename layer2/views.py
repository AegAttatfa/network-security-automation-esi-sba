from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def port_security(request):
	return render(request, 'layer2/index.html')
