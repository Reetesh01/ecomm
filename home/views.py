from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *

# Create your views here.
class BaseView(View):
	views = {}
	views['categories'] = Category.objects.all()
	views['subcategories'] = SubCategory.objects.all()
	views['sliders'] = Slider.objects.all()
	views['ads'] = Ad.objects.all()


class HomeView(BaseView):
	def get(self,request):
		self.views
		self.views['products'] = Products.objects.all()
		self.views['offers'] = Products.objects.filter(labels = 'offer')
		self.views['hots'] = Products.objects.filter(labels = 'hot')
		self.views['news'] = Products.objects.filter(labels = 'new')
		

		
		return render(request,'index.html', self.views)


class SubcategoryView(BaseView):
	def get(self,request,slug):
		subcatid = SubCategory.objects.get(slug = slug).id
		self.views['subcat_product'] = Products.objects.filter(subcategory_id = subcatid)

		return render(request,'kitchen.html',self.views)

class DetailView(BaseView):
	def get(self,request,slug):
		self.views['detail_product'] = Products.objects.filter(slug = slug)

		return render(request,'single.html',self.views)

class SearchView(BaseView):
	def get(self,request):
		if request.method == 'GET':
			query = request.GET['search']

			if query != '':
				self.views['search_product'] = Products.objects.filter(name__icontains = query)
			else:
				return redirect('/')

		return render(request,'search.html',self.views)


from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,'The Username Is Already Used!!')
				return redirect('/register')

			elif User.objects.filter(email = email).exists():
				messages.error(request,'The Email Is Already Used!!')
				return redirect('/register')

			else:
				user = User.objects._create_user(
					username = username,
					email = email,
					password = password
					)
				user.save()
				return redirect('/')
		else:
			messages.error(request,'The Password Dosenot Match!!')
			return redirect('/register')

	return render(request,'register.html')