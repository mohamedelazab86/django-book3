from django.shortcuts import render,redirect
from .models import Book,Review
from .forms import BookForm,ReviewForm

def list_book(request):
    books=Book.objects.all()
    context={'book_list':books}
    return render(request,'my_book/book_list.html',context)

def detail_book(request,pk):
    book=Book.objects.get(id=pk)
    review=Review.objects.filter(book=book)

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.book=book
            my_form.save()
            return redirect('/bookss/')
    else:


         form=ReviewForm()

    context={'book':book,'form':form,'review':review}
    return render(request,'my_book/book_detail.html',context)

def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookss/')
    else:

         form=BookForm()
    context={'form':form}
    return render(request,'my_book/create.html',context)
def update_book(request,pk):
    
        
    book=Book.objects.get(id=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/bookss/')
    else:
        form=BookForm(instance=book)
           
    context={'form':form}
    return render(request,'my_book/update.html',context)
def delete_book(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return redirect('/bookss/')


