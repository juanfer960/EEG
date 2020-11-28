from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Prediction, Plot
from . import forms
from first_app.forms import NewUserForm,FormName,FormSearch,Loadfrom
import pickle
from sklearn import svm
from sklearn.metrics import classification_report
from django.core.files.storage import FileSystemStorage
import datetime
from .models import LoadDataProces
import numpy as np
import mne
import pandas as pd
from pandas import DataFrame
import matplotlib
from random import sample
from matplotlib import pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg
import urllib, base64
import json
from pymongo import MongoClient
import pickle

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    form = NewUserForm()
    from_2 = FormSearch()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['name']
            password = form.cleaned_data['password']

            predictions_0 = Prediction.objects.filter(prediction = '0')[:3]
            predictions_1 = Prediction.objects.filter(prediction = '1')[:3]
            predictions_2 = Prediction.objects.filter(prediction = '2')[:3]

            temp = []
            dataRes_1 = []
            dataRes_2 = []
            dataRes_3 = []

            for prediction in predictions_0:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)
                    temp.append("EEG: " + prediction.eeg)

                    dataRes_1.append(temp.copy())
                    temp.clear()
                except:
                    print('error')
             
            for prediction in predictions_1:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)
                    temp.append("EGG: " + prediction.eeg)

                    dataRes_2.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            for prediction in predictions_2:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)
                    temp.append("EGG: " + prediction.eeg)

                    dataRes_3.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            dataRes = {'form':from_2, 'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3}

            if userValid(user,password):
                return  render(request,'basicapp/workPage.html',context=dataRes)

            else:
                data = {'user': 'null', 'password': 'null'}
                form = NewUserForm(data)
              

                return render(request,'basicapp/pageError.html')

    return render(request,'basicapp/login.html',{'form':form})


def logup(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'basicapp/successPage.html')
        else:
            print('ERROR FORM INVALID')

    return render(request,'basicapp/logup.html',{'form':form})


def userValid (user, password):
    try:
        User.objects.get(user = user, password =  password)
        print(User)
    except:
        return False

    return True


def singout(request):
    return render(request,'index.html')


def search(request,**kwargs):
    form = forms.Loadfrom()

    user = kwargs['user']
    password = kwargs['password']
    dataRes = {'user': user, 'password': password,'form':form}

    return  render(request,'basicapp/search.html',context=dataRes)


def home(request,**kwargs):

    user = kwargs['user']
    password = kwargs['password']

    form = FormSearch()

    prediction_result = 3

    predictions_0 = Prediction.objects.filter(prediction = '0')[:prediction_result]
    predictions_1 = Prediction.objects.filter(prediction = '1')[:prediction_result]
    predictions_2 = Prediction.objects.filter(prediction = '2')[:prediction_result]

    print(predictions_0)
    print(predictions_0)
    print(predictions_0)

    temp = []
    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []

    for prediction in predictions_0:
        try:
            temp.append("Nombre Doctor: " + prediction.user_id)
            temp.append("ID Paciente: " + prediction.patinte_id)
            temp.append("Edad Paciente: " + prediction.patiente_age)
            temp.append("Fecha Análisis: " + prediction.analysis_date)
            temp.append("EGG: " + prediction.eeg)

            dataRes_1.append(temp.copy())
            temp.clear()
        except:
            print('error')

    for prediction in predictions_1:
        try:
            temp.append("Nombre Doctor: " + prediction.user_id)
            temp.append("ID Paciente: " + prediction.patinte_id)
            temp.append("Edad Paciente: " + prediction.patiente_age)
            temp.append("Fecha Análisis: " + prediction.analysis_date)
            temp.append("EGG: " + prediction.eeg)

            dataRes_2.append(temp.copy())
            temp.clear()
        except:
            print('error')

    for prediction in predictions_2:
        try:
            temp.append("Nombre Doctor: " + prediction.user_id)
            temp.append("ID Paciente: " + prediction.patinte_id)
            temp.append("Edad Paciente: " + prediction.patiente_age)
            temp.append("Fecha Análisis: " + prediction.analysis_date)
            temp.append("EGG: " + prediction.eeg)

            dataRes_3.append(temp.copy())
            temp.clear()
        except:
            print('error')
       

    dataRes = {'form':form,'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3}

    return  render(request,'basicapp/workPage.html',context=dataRes)


def fileSerch(request,**kwargs):

    form = forms.Loadfrom()

    user=kwargs['user']
    password=kwargs['password']

    if request.method == 'POST':
        form = forms.Loadfrom(request.POST)

        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        if form.is_valid():
            archivo = form.cleaned_data['archivo']
            paciente = form.cleaned_data['paciente']
            edad = form.cleaned_data['edad']

            loadDataProces = LoadDataProces(eeg = archivo, patinte_id = paciente, patiente_age = edad, analysis_date = datetime.datetime.now(), user_id = user, prediction = '0', process = "0")
            loadDataProces.save()

        else:
            print('error')

        form = forms.Loadfrom()

        dataRes = {'user': user, 'password': user, 'URL': 'El archivo se cargo correctamente en: ' + url,'form':form}

    return  render(request,'basicapp/search.html',context=dataRes)
    

def eegSerch(request,**kwargs):

    form = forms.FormSearch()

    dataRes_  = []

    temp = []

    dataRes_1 = []
    dataRes_2 = []
    dataRes_3 = []

    user=kwargs['user']
    password=kwargs['password']

    if request.method == 'POST':
        form = forms.FormSearch(request.POST)

        if form.is_valid():

            doctor = form.cleaned_data['doctor']
            paciente = form.cleaned_data['paciente']

            prediction_result =  3

           
            predictions_0 = Prediction.objects.filter(prediction = '0', patinte_id = paciente, user_id = doctor)[:prediction_result]
            predictions_1 = Prediction.objects.filter(prediction = '1', patinte_id = paciente, user_id = doctor)[:prediction_result]
            predictions_2 = Prediction.objects.filter(prediction = '2', patinte_id = paciente, user_id = doctor)[:prediction_result]

            for prediction in predictions_0:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)
                    temp.append("EGG: " + prediction.eeg)

                    dataRes_1.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            for prediction in predictions_1:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)
                    temp.append("EGG: " + prediction.eeg)

                    dataRes_2.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            for prediction in predictions_2:
                try:
                    temp.append("Nombre Doctor: " + prediction.user_id)
                    temp.append("ID Paciente: " + prediction.patinte_id)
                    temp.append("Edad Paciente: " + prediction.patiente_age)
                    temp.append("Fecha Análisis: " + prediction.analysis_date)
                    temp.append("EGG: " + prediction.eeg)

                    dataRes_3.append(temp.copy())
                    temp.clear()
                except:
                    print('error')

            dataRes = {'form':form, 'user': user, 'password': password,'dataRes_uno':dataRes_1,'dataRes_dos':dataRes_2,'dataRes_tres':dataRes_3}

        return  render(request,'basicapp/workPage.html',context=dataRes)


# ********** Grafica **********************************************************************************************
 

def plot(request,**kwargs):

    cont = 0
    
    fileName_ = request.GET['field1']

    fileName = fileName_.lstrip('EGG: ')

    print('***************************************')
    print(fileName)
    print('****************************************')

    plot = Plot.objects.filter(edfName = fileName)

    if(len(plot)==0):
        Plot.objects.create(edfName = fileName, count = cont)
    else:
        for plot_  in plot:
            cont = plot_.count 
            cont = int(cont) + 10
            Plot.objects.filter(edfName = fileName).update(count = cont)

    chn_lst=['FP1-F3', 'F3-C3', 'C3-P3', 'P3-O1', 'FP2-F4', 'F4-C4', 'C4-P4', 'P4-O2', \
             'FP1-F7', 'F7-T3', 'T3-T5', 'T5-O1', 'FP2-F8', 'F8-T4', 'T4-T6', 'T6-O2']
             
    cleaned_eeg = loadFile(fileName)
    chn_idx = mne.pick_channels(cleaned_eeg.info['ch_names'], include=chn_lst, exclude=[])
    
    ax = cleaned_eeg.plot(duration=10, start=cont, order=chn_idx, highpass=0.5, lowpass=32, remove_dc=True)

    buf = io.BytesIO()
    ax.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    uri = urllib.parse.quote(string) 
    print('FIN GENERACION IMAGEN')

    return HttpResponse(uri)


def loadFile(fileName):
    cleaned_eeg = mne.io.read_raw_edf('/Users/juanzuluaga/Documents/ProyectoFinal/aplicacion/APPEEG/media/' +fileName)
    return cleaned_eeg




         

   

    












