from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return render(request,'generator/home.html')

def password(request):


	char = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('numbers'):
		char.extend(list('0123456789'))

	if request.GET.get('special'):
		char.extend(list('@!#$%&*(_)+-/><|[]{}~'))

	length = int(request.GET.get('length',12))

	genpass = ''

	for i in range(length):

		genpass += random.choice(char)

	return render(request,'generator/password.html',{'genpass':genpass})

def about(request):
	return render(request,'generator/about.html')
