from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Record, Status, OperationType, Category, Subcategory
from .forms import (
    RecordForm, StatusForm, OperationTypeForm,
    CategoryForm, SubcategoryForm
)


class RecordListView(ListView):
    model = Record
    template_name = 'webdds/record_list.html'
    context_object_name = 'records'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()

        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from and date_to:
            queryset = queryset.filter(date__range=[date_from, date_to])

        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status_id=status)

        operation_type = self.request.GET.get('operation_type')
        if operation_type:
            queryset = queryset.filter(operation_type_id=operation_type)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=category)

        subcategory = self.request.GET.get('subcategory')
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['operation_types'] = OperationType.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'webdds/record_form.html'  # Все пути теперь с префиксом dds/
    success_url = reverse_lazy('record-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'webdds/record_form.html'  # Исправлено для единообразия
    success_url = reverse_lazy('record-list')


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'webdds/record_confirm_delete.html'
    success_url = reverse_lazy('record-list')


def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)


class StatusListView(ListView):
    model = Status
    template_name = 'webdds/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'webdds/status_form.html'
    success_url = reverse_lazy('status-list')


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'webdds/status_form.html'
    success_url = reverse_lazy('status-list')


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'webdds/status_confirm_delete.html'
    success_url = reverse_lazy('status-list')


class OperationTypeListView(ListView):
    model = OperationType
    template_name = 'webdds/operationtype_confirm_delete.html'
    context_object_name = 'operation_types'


class OperationTypeCreateView(CreateView):
    model = OperationType
    form_class = OperationTypeForm
    template_name = 'webdds/operationtype_form.html'
    success_url = reverse_lazy('operation-type-list')


class OperationTypeUpdateView(UpdateView):
    model = OperationType
    form_class = OperationTypeForm
    template_name = 'webdds/operationtype_form.html'
    success_url = reverse_lazy('operation-type-list')


class OperationTypeDeleteView(DeleteView):
    model = OperationType
    template_name = 'webdds/operationtype_confirm_delete.html'
    success_url = reverse_lazy('operation-type-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'webdds/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'webdds/category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'webdds/category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'webdds/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'webdds/subcategory_list.html'
    context_object_name = 'subcategories'


class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'webdds/subcategory_form.html'
    success_url = reverse_lazy('subcategory-list')


class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'webdds/subcategory_form.html'
    success_url = reverse_lazy('subcategory-list')


class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = 'webdds/subcategory_confirm_delete.html'
    success_url = reverse_lazy('subcategory-list')