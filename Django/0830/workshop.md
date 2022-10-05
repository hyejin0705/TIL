1. intro/urls.py
```
urlpattens=[
    path('dinner/', views.dinner)

]
```


2. pages/views.py
```
def dinner(request):
    return render(request, 'dinner/html',)
```

3. templates/dinner.html



