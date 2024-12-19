from django.shortcuts import render
from myapp.forms import Feedbackform

# Create your views here.
def feedBack(request):
	f=Feedbackform()
	if request.method=="POST":   
		f=Feedbackform(request.POST)
		if f.is_valid():
			name=f.cleaned_data['name']
			rollno=f.cleaned_data['rollno']
			email=f.cleaned_data['email']
			feedback=f.cleaned_data['feedback']
			d={'name':name,'rollno':rollno,'email':email,'feedback':feedback}
			return render(request,'htmlpage/output.html',d)
	d={'form':f}
	return render(request,'htmlpage/input.html',d)


