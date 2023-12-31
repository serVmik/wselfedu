from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from english.forms import CategoryForm
from english.models import CategoryModel
from contrib_app.mixins import (
    AddMessageToFormSubmissionMixin,
    HandleNoPermissionMixin,
    RedirectForModelObjectDeleteErrorMixin,
    UserPassesTestAdminMixin,
)

PAGINATE_NUMBER = 20


class CategoryListView(
    HandleNoPermissionMixin,
    LoginRequiredMixin,
    ListView,
):
    model = CategoryModel
    context_object_name = 'categories'
    template_name = 'eng/cat_list.html'
    paginate_by = PAGINATE_NUMBER
    extra_context = {
        'title': 'Список категорий',
    }
    message_no_permission = 'Вы пока не можете делать это'


class CategoryCreateView(
    HandleNoPermissionMixin,
    UserPassesTestAdminMixin,
    AddMessageToFormSubmissionMixin,
    CreateView,
):
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('eng:categories_list')
    extra_context = {
        'title': 'Добавить категорию',
        'btn_name': 'Добавить',
    }

    success_message = 'Категория добавлена'
    error_message = 'Ошибка в добавлении категории'
    message_no_permission = 'Вы пока не можете делать это'


class CategoryUpdateView(
    HandleNoPermissionMixin,
    UserPassesTestAdminMixin,
    AddMessageToFormSubmissionMixin,
    UpdateView,
):
    model = CategoryModel
    form_class = CategoryForm
    template_name = 'form.html'
    extra_context = {
        'title': 'Изменить категорию',
        'btn_name': 'Изменить',
    }
    success_url = reverse_lazy('eng:categories_list')
    success_message = 'Категория изменена'
    error_message = 'Ошибка изменения категории'
    message_no_permission = 'Вы не можете этого делать'


class CategoryDeleteView(
    HandleNoPermissionMixin,
    UserPassesTestAdminMixin,
    RedirectForModelObjectDeleteErrorMixin,
    AddMessageToFormSubmissionMixin,
    DeleteView,
):
    model = CategoryModel
    template_name = 'delete.html'
    extra_context = {
        'title': 'Удаление категории',
        'btn_name': 'Удалить',
    }
    success_url = reverse_lazy('eng:categories_list')
    success_message = 'Категория удалена'
    message_no_permission = 'Вы не можете этого делать'
