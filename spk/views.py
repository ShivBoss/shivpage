from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import MailMe, ImgBlog
from .forms import MailMeForm

# Create your views here.



def home(request):


	return render(request, "home.html", {})

	
def mailme(request):

	form = MailMeForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		ins = form.save(commit=False)
		ins.save()
		messages.info(request, 'Thank You for mailing me!!!')
		return HttpResponseRedirect(reverse("mail"))

	context = {
		'form':form,
	}
	return render(request,'mailMe_page.html', context)


def myblog(request):

	queryset_list = ImgBlog.objects.all().order_by("-timestamp")

	query = request.GET.get("q")

	if query:
		queryset_list = queryset_list.filter(Q(title__icontains=query)|Q(context__icontains=query)).distinct()

	paginator = Paginator(queryset_list, 5)

	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {

		"obj_list" : queryset,		

	}
	return render(request, 'blog_page.html', context)



def blog_detail(request, id=None):
	
	ins = get_object_or_404(ImgBlog, id=id)
	context = {		
		"ins" : ins,
	}
	return render(request, 'blog_detail_page.html', context)

