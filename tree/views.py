from django.shortcuts import render, redirect, get_object_or_404, redirect
from itertools import ifilter
from .models import Company
from .forms import CompanyForm

from django.db.models import Sum


def home(request):
	form = CompanyForm(request.POST or None)

	if request.method == "POST":
		if form.is_valid():
			temp = form.save(commit=False)
			parent = form['parent'].value()

			if parent == '':
				temp.path = []
				temp.save()
				temp.path = [temp.id]
			else:
				node = Company.objects.get(id=parent)
				temp.depth = node.depth + 1
				temp.path = node.path
				temp.save()
				temp.path.append(temp.id)

			temp.save()
			return redirect('tree.views.home')

	company_tree = Company.objects.all().order_by('path')
	total_earnings = Company.objects.all().aggregate(Sum('earnings'))

	return render(request, 'tree/index.html', locals(),)


def company_edit(request, pk):
	company = get_object_or_404(Company, pk=pk)
	if request.method == "POST":
		form = CompanyForm(request.POST, instance=company)
		if form.is_valid():
			temp = form.save(commit=False)
			parent = form['parent'].value()

			if parent == '':
				temp.path = []
				temp.save()
				temp.path = [temp.id]
			else:
				node = Company.objects.get(id=parent)
				temp.depth = node.depth + 1
				temp.path = node.path
				temp.save()
				temp.path.append(temp.id)

			temp.save()
			return redirect('tree.views.home')
	else:
		form = CompanyForm(instance=company)
	return render(request, 'tree/index.html', {'form':form})


def company_remove(request, pk):
	company = get_object_or_404(Company, pk=pk)
	company.delete()
	return redirect('tree.views.home')
