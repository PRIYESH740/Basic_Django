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

def food(request):
     return render(request,'food.html')

def orders(request):
     return render(request,'order.html')
    
def delivery(request):
     return render(request,'delivery.html')
    

def contact(request):
     detail={}
     try:
          n1=request.GET['name']
          n2=request.GET['email']
          n3=request.GET['subject']
          n4=request.GET['message']

          detail={
          'name':n1,
          'email':n2,
          "subject":n3,
          'message':n4
     }
     except:
          print('I got some error in your form filling')

     
     return render(request,'contact.html',{"output":detail})
    # return HttpResponse("This is a contact us page")
