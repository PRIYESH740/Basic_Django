from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import usersForm
from api.models import *
from .models import News
# Create your views here.
def home(request):
    # context={
    #     'variable':"Hello developer , How are you?"
    # }
    # return render(request,'index.html',context)
    #return HttpResponse("This is home page")
     # if request.method=='GET':
     #      output=request.GET.get('output')
     newsData=News.objects.all()
     homeData=Homepage.objects.all()
     data={
          'homeData':homeData,
          'newsData':newsData,
     }

     return render(request,'index.html',data)

def about(request):
     ServiceData=Service.objects.all()
     memberData=TeamMember.objects.all()
     data={
          'ServiceData':ServiceData,
          'memberData':memberData
          }
     return render(request,'about.html',data)
    # return HttpResponse("This iS ABOUT page")

def food(request):
     foodData=FoodItem.objects.all().order_by('food_name')                  #[:3] this is limiting concept for showing number of content is 3.
     data={
          'foodData':foodData
     }
     return render(request,'food.html',data)

def orders(request):
     data={}
     try:
          if request.method=='POST':
               name=request.POST.get('name')
               phone=request.POST.get('phone')
               address=request.POST.get('address')
               food=request.POST.get('food')
               quantity=request.POST.get('quantity')
          
          data={
               'Name':name,
          'Phone':phone,
          "Address":address,
          'Food':food,
          'Quantity':quantity
          }
          url='/delivery/?output={}'.format(data)
          return HttpResponseRedirect(url)

     except:
          print('Invalid input')

     return render(request,'order.html')
    
def delivery(request):
     if request.method=='GET':
          output=request.GET.get('output')
     return render(request,'delivery.html',{'output':output})
    

def contact(request):
     detail={}
     try:
          if request.method=='POST':
               n1=request.POST.get('name')
               n2=request.POST.get('email')
               n3=request.POST.get('subject')
               n4=request.POST.get('message')

          detail={
          'Name':n1,
          'Email':n2,
          "Subject":n3,
          'Message':n4
     }
          # url='/?output={}'.format(detail)
          # return redirect(url)

     except:
          print('I got some error in your form filling')

     
     return render(request,'contact.html',{"output":detail})
    # return HttpResponse("This is a contact us page")

def submitform(request):
     fn=usersForm()
     data={'form':fn}
     return render(request,'userform.html',data) 

def calculator(request):
     c=''
     try:
          if request.method=="POST":
               n1=eval(request.POST.get('num1'))
               n2=eval(request.POST.get('num2'))
               opr=request.POST.get('opr')

               if opr=='+':
                    c=n1+n2
               elif opr=="-":
                    c=n1-n2
               elif opr=="*":
                    c=n1*n2
               else:
                    c=n1/n2
     except:
          c='--Invalid-Operation--'
     return render(request,'calculator.html',{'c':c}) 


def marksheet(request):

     if request.method=='POST':
          s1=eval(request.POST.get('subject1'))
          s2=eval(request.POST.get('subject2'))
          s3=eval(request.POST.get('subject3'))
          s4=eval(request.POST.get('subject4'))
          s5=eval(request.POST.get('subject5'))

          t=s1+s2+s3+s4+s5
          p=(t*100)/500
          if p>=60:
               d="First Division"
          elif p>=50:
               d="Second Division"
          elif p>=40:
               d="Third Division"
          else:
               d='Fail'
          data={'total':t,'per':p,'divi':d}

          return render(request,'marksheet.html',data) 

def newsdetails(request,newsid):
     newsDetail=News.objects.get(id=newsid)
     data={
          'newsDetail':newsDetail
     }

     return render(request,'newsdetails.html',data)

     