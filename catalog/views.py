from pyexpat import model
from django.shortcuts import render, HttpResponse
from catalog.models import Book, BookInstance, Author, Genre, Language
from django.views import generic

# Create your views here.
def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }
    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""

    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""

    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based detail view for a book."""

    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""

    model = Author
