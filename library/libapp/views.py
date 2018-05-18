from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .forms import BookForm

# Create your views here.


def book_details(request):

    data = Book.objects.all().order_by('name', '-edition')

    return render(request, 'book_details.html', {'book_data': data})


class BookView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'book_details.html'
    context_object_name = 'book_data'
    ordering = ('-edition', )

    #def get_queryset(self):

    #    data = Book.objects.all().order_by('-name')
    #    return data


def book_data(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise form.ValidationErrors
        return HttpResponseRedirect('libapp/book_details/')
    else:
        form = BookForm()


    return render(request, 'create_book.html', {'form': form})
