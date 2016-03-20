from django.shortcuts import render, redirect
from itertools import ifilter
from .models import Company
from .forms import CompanyForm


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

	return render(request, 'tree/index.html', locals(),)