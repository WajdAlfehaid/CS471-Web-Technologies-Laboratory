from django.shortcuts import render

def index2(request, val1=0):
    if not str(val1).isdigit():
        return render(request, "bookmodule/index2.html",
                      {"error": "error, expected val1 to be integer"})
    return render(request, "bookmodule/index2.html",
                  {"val1": val1})

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')