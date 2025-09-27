# Ex.05 Design a Website for Server Side Processing
## Date: 27.09.2025

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
views.py

from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None
    if request.method == 'POST':
        try:
            height = float(request.POST.get('height')) / 100
            weight = float(request.POST.get('weight'))
            bmi = round(weight / (height ** 2), 2)
        except (ValueError, ZeroDivisionError):
            print("Invalid input received.")
            bmi = "Invalid input"
            category = None
    print(f" Height: {height * 100} cm \n Weight: {weight} kg \n BMI: {bmi}")
    return render(request, 'tomapp/tom.html', {'bmi': bmi, 'category': category})

urls.py


from django.contrib import admin
from django.urls import path
from tomapp.views import bmi_calculator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bmi_calculator, name='bmi_calculator'),
]

tom.html

<!DOCTYPE html>
<html>

<head>
    <title>BMI Calculator</title>
    <style>
        body {
            background-color: rgb(230, 240, 255);
            font-size: large;
            color: rgb(0, 51, 102);
        }

        @keyframes jerry {
            0% {
                width: 0px;
            }

            100% {
                width: 400px;
            }

        }

        * {
            padding: 0px;
            margin: 0px;
        }

        #box {
            border: 4px solid skyblue;
            width: 400px;
            height: 500px;
            border-radius: 6%;
            display: flex;
            flex-wrap: nowrap;
            flex-direction: column;
            gap: 30px;
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: turquoise;
            animation-name: jerry;
            animation-duration: 3s;
        }

        h1 {
            color: rgb(0, 76, 153);
        }

        .btn {
            padding: 10px;
            font-size: small;
            font-weight: bold;
            border-radius: 8%;
            border: solid 2px rgb(0, 0, 0);
            color:rgb(0, 76, 153);
        }

        .values {
            border-radius: 6px;
            border: solid 2px rgb(0, 0, 0);
            padding: 5px;
        }
    </style>
</head>

<body>
    <center>
        <strong>
            <h1>Jeffrin - 25009198</h1>
        </strong>
        <div id="box">
            <br><br>
            <h2>BMI Calculator</h2>
            <br>

            <form method="post">
                {% csrf_token %}
                <strong><label for="height">Height (cm):</label></strong>
                <input type="text" id="height" name="height" placeholder="height" style="padding:3px;" class="values"
                    required>
                <br>
                <br>
                <strong><label for="weight">Weight (kg):</label></strong>
                <input type="text" id="weight" name="weight" placeholder="weight" style="padding:3px;" class="values"
                    required>
                <br>
                <br>
                <input type="submit" value="Calculate BMI" class="btn">
            </form>
            {% if bmi %}
            <h2>Your BMI: {{ bmi }}</h2>
            {% if category %}
            <p>Category: {{ category }}</p>
            {% endif %}
            {% endif %}
        </div>
    </center>
</body>

</html>

```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (57).png>)

## HOMEPAGE:
![alt text](<Screenshot (55).png>)

## RESULT:
The program for performing server side processing is completed successfully.
