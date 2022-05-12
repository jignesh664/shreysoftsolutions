from django.shortcuts import render


from .models import Contact

# Create your views here.
def index(request):
	return render(request,'index.html')

# def portfolio_details(request):
# 	return render(request,'portfolio_details.html')

def contact(request):
	Contact.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		subject=request.POST['subject'],
		message=request.POST['message']

		)
	msg="Your message has been sent. Thank you! Will Reach You Soon"
	return render(request,'index.html',{'msg':msg})
