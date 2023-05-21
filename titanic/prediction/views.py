from django.shortcuts import render
import pickle
import numpy
import os
from prediction.models import Passenger

def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def predict(req):
    return render(req, 'predict.html')

def passengers(req):
    if req.method=='POST':
        nm=req.POST.get('qname')
        vals=Passenger.objects.filter(name__startswith=nm)[:12]
        return render(req, 'passenger.html',context={'vals':vals})
    vals=Passenger.objects.all().values()
    vals=vals[0:12]
    return render(req, 'passenger.html',context={'vals':vals})

def developer(req):
    return render(req, 'developer.html')

def result(req):
    feilds=['pclass','gender','age','sibsp','parch','fare','embarked']
    vals=[]
    for f in feilds:
        if f=='fare':
            vals.append(float(req.POST.get(f)))
            continue
        vals.append(int(req.POST.get(f)))
    v = numpy.array(vals).reshape(1,-1)
    model_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'model', 'model.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    predictions = model.predict(v)
    if predictions==1:
        return render(req, 'result.html', context={'survived':'Survived'})
    elif predictions==0:
        return render(req, 'result.html', context={'survived':'Did not Survive'})
    return render(req, 'result.html')

def add(req):
    if req.method=='POST':
        nm=req.POST.get('name')
        age=req.POST.get('age')
        pc=req.POST.get('pclass')
        gender=req.POST.get('gender')
        p = Passenger(name=nm, age=age, pc=pc, gender=gender)
        p.save()
        return render(req, 'add.html', context={'show':True})
    return render(req, 'add.html', context={'show':False})

def delete(req):
    if req.method=='POST':
        pid=req.POST.get('id')
        p = Passenger.objects.get(id=pid)
        p.delete()
        return render(req, 'delete.html', context={'show':True})
    return render(req, 'delete.html', context={'show':False})