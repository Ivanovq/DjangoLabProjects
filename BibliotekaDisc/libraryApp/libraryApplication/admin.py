from django.contrib import admin
from .models import Genre, Rating, Translator, Book, BookTranslator

# Register your models here.


class BookRatingInline(admin.TabularInline):
    model = Rating
    extra = 1

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    inlines = [BookRatingInline]
    list_filter = ('available',)

    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False



class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser  # Дозволено само за суперкорисници

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Дозволено само за суперкорисници


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Translator)
admin.site.register(BookTranslator)
