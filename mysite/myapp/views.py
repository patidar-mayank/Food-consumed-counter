from django.shortcuts import render,redirect
from .models import Food,Consume

# Create your views here.
def index(request):
    if request.method=="POST":
        food_consumed=request.POST['food_consumed']
        consume=Food.objects.get(name=food_consumed)# to get not name acutal object
        user=request.user # it will user who currently loged-in
        consume=Consume(user=user,food_consumed=consume)
        consume.save()
        foods=Food.objects.all() # actually we want to show food item in both cases that why we put in else block as well as if block we write foods
           
    else:   
         
        foods=Food.objects.all()
    consumed_food=Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})


def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')
     
