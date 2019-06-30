from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_reserved = BookInstance.objects.filter(status__exact = 'r').count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_books_pig = Book.objects.filter(title__icontains = 'pig'.lower()).count() 
    



    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    


    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits}, # num_visits appended
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    def get_queryset(self):
        return Book.objects.all()
        #filter(title__icontains='war')[:5] # Получить 5 книг, содержащих 'war' в заголовке



class BookDetailView(generic.DetailView):
    model = Book




class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10
	def get_author_set(self):
		return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author
