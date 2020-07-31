from django.shortcuts import render


def sum(request):
	render(request, 'sum.html')
