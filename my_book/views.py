from django.shortcuts import render
from .models import Book,Review

# Create your views here.

#===================== create  crud opertions  by class baseview  =======================
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

class List_book(ListView):                     # CONTEXT IN EMPLATE      NAME OF MODEL _LIST    book_list   -   object_list
    model=Book                                 # template    name of templtes_ action           book_list  

class Detail_book(DetailView):
    model=Book
  

class Create_book(CreateView):
    model=Book
    fields='__all__'
    success_url='/books/'
    template_name='my_book/create.html'

class Update_book(UpdateView):
    model=Book
    fields='__all__'
    success_url='/books/'
    template_name='my_book/update.html'

class Delete_book(DeleteView):
    model=Book
    template_name='my_book/delete.html'
    success_url='/books/'