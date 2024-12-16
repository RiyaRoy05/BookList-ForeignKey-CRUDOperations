from django.shortcuts import render,redirect
from web.forms import BookForm
from web.models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request,"index.html",context=context)

def second(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = BookForm()
        
    context = {
        'form': form
    }
    return render(request,"second.html",context=context)

def updateB(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    context = {
        'form': form,
        'id': id,
    }
    return render(request,"updateB.html",context=context)

def hbUp(request,id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        formdata = BookForm(instance=book, data=request.POST, files=request.FILES)
        if formdata:
            formdata.save()
        else:
            print("error2")
        return redirect("/")
    else:
        print("error")

def hdel(request,id):
    book = Book.objects.get(id=id)
    if book:
        book.delete()
    else:
        print("error")
    return redirect("/")


def detail(request,id):
    book = Book.objects.get(id=id)
    context ={
        'book' : book
    }

    return render(request,"Details.html",context=context)