
from django.shortcuts import render, redirect
from .forms import sign_up_form, login_form
from django.contrib.auth import authenticate, login, logout
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from django.contrib.auth.decorators import login_required


# Create your views here.

class linearRegressionModel():
    def __init__(self):
        HouseDF = pd.read_csv('core/USA_Housing.csv')
        X = HouseDF[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                    'Avg. Area Number of Bedrooms', 'Area Population']]
        y = HouseDF['Price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
        lm = LinearRegression()
        lm.fit(X_train,y_train)
        self.lm = lm

    def predictOutput(self, a, b, c, d, e):
        x = self.lm.predict([[a,b,c,d,e]])
        return x[0]
    
def home(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/home.html', {'name': request.user})
    return render(request, 'enroll/home.html')
    

def signUp(request):
    # stud = User.objects.all()
    if request.method == 'POST':
        frm = sign_up_form(request.POST)
        if frm.is_valid():
            frm.save()
        else:
            print(frm.errors)
            return render(request, 'enroll/register.html', {"form": frm})
    frm = sign_up_form()    
    return render(request, 'enroll/register.html', {"form": frm})


def login_page(request):
    if request.method == "POST":
        fm = login_form(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']

            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)
                return redirect('homepage')

    fm = login_form()
    return render(request, "enroll/login.html", {'form': fm})


def logout_page(request):
    logout(request)
    return redirect('homepage')

def about_page(request):
    return render(request, 'enroll/about.html')

def contact_page(request):
    return render(request, 'enroll/contact.html')

@login_required
def selling_page(request):
    return render(request, 'enroll/sell.html')


def prediction_page(request):
    model = linearRegressionModel()
    if request.method == "POST":
        income = int(request.POST.get('Income'))
        age = int(request.POST.get('age'))
        Rooms = int(request.POST.get('Rooms'))
        Bedrooms = int(request.POST.get('Bedrooms'))
        Population = int(request.POST.get('Population'))

        x = model.predictOutput(income, age, Rooms, Bedrooms, Population)
        
        return render(request, "enroll/prediction.html", {"output": round(x, 2)})

    return render(request, "enroll/prediction.html")


