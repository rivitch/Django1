from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def title(request): 
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 2.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 { color: #237;}
            
            p {color: #555; }
        </style>
    </head>
    <body>
        <h1>Django</h1>
    
        <p>Django - это высокоуровневый фреймворк для веб-приложений на языке
        Python. </p>
    <h2>Преимущества использования Django</h2>
        <p>Использование Django имеет множество преимуществ, таких как:</p>
        <p>● Быстрая разработка веб-приложений</p>
        <p>● Простота и удобство использования</p>
        <p>● Высокая производительность</p>
        <p>● Безопасность</p>
        <p>● Масштабируемость</p>
    </body>
    </html>
    """
    logger.info(f'Visiting a page TITLE in: {datetime.now()}')
    return HttpResponse(html)

def my_site(request): 
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 2.5;
                margin: 0;
                padding: 20px;
            }
            h1 { color: #20;}
            p {color: #900; }
        </style>
    </head>
    <body>
        
    <h1>About</h1>
        <p>descrition</p>
       </body>
    </html>
    """
    logger.info(f'Был в : {datetime.now()}')
    return HttpResponse(html)