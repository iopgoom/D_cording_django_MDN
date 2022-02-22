from django.contrib import admin
from catalog.models import Author, Book, Genre, BookInstance, Language

# Register your models here.
# admin.site.register([Author, Book, Genre, BookInstance, Language])
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_of_birth",
        "date_of_death",
    )


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "display_genre",
        "language",
    )


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
