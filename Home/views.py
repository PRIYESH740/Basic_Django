from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # context={
    #     'variable':"Hello developer , How are you?"
    # }
    # return render(request,'index.html',context)
    #return HttpResponse("This is home page")

     return render(request,'index.html')

def about(request):
     return render(request,'about.html')
    # return HttpResponse("This iS ABOUT page")

def services(request):
     return render(request,'services.html')
    # return HttpResponse("this is Services pages")

def contact(request):
     return render(request,'contact.html')
    # return HttpResponse("This is a contact us page")
