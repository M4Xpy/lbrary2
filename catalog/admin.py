from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import LiteraryFormat, Book, Author


@admin.register(Book)  # admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format", ]
    list_filter = ["format", ]
    search_fields = ["title", ]


@admin.register(Author)  # admin.site.register(Author, UserAdmin)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pseudonym",)
    fieldsets = UserAdmin.fieldsets + (
        ("additional information", {"fields": ("pseudonym",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("additional information", {"fields": ("first_name", "last_name", "pseudonym",)}),
    )

    # UserAdmin.list_display += ("pseudonym",)
    # UserAdmin.fieldsets += (
    #     ("additional information", {"fields": ("pseudonym",)}),
    # )
    # UserAdmin.add_fieldsets += (
    #     ("additional information", {"fields": ("first_name", "last_name", "pseudonym",)}),
    # )


admin.site.register(LiteraryFormat)
