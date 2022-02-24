from dataclasses import field
from statistics import mode
from django.contrib import admin
from catalog.models import Author, Book, Genre, BookInstance, Language

# Register your models here.
# admin.site.register([Author, Book, Genre, BookInstance, Language])
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "display_genre",
        "language",
    )
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "status",
        "due_back",
        "id",
    )
    list_filter = (
        "status",
        "due_back",
    )

    fieldsets = (
        (
            "book infomation",
            {
                "fields": (
                    "book",
                    "imprint",
                    "id",
                )
            },
        ),
        (
            "Availability",
            {
                "fields": (
                    "status",
                    "due_back",
                )
            },
        ),
    )
