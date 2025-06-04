from django.urls import path
from . import views

urlpatterns = [
    # Главная страница приложения
    path('', views.RecordListView.as_view(), name='record-list'),

    # CRUD для записей
    path('records/create/', views.RecordCreateView.as_view(), name='record-create'),
    path('records/<int:pk>/update/', views.RecordUpdateView.as_view(), name='record-update'),
    path('records/<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record-delete'),

    # AJAX endpoint
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax-load-subcategories'),

    # Управление справочниками
    path('statuses/', views.StatusListView.as_view(), name='status-list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status-delete'),

    path('operation-types/', views.OperationTypeListView.as_view(), name='operation-type-list'),
    path('operation-types/create/', views.OperationTypeCreateView.as_view(), name='operation-type-create'),
    path('operation-types/<int:pk>/update/', views.OperationTypeUpdateView.as_view(), name='operation-type-update'),
    path('operation-types/<int:pk>/delete/', views.OperationTypeDeleteView.as_view(), name='operation-type-delete'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('subcategories/', views.SubcategoryListView.as_view(), name='subcategory-list'),
    path('subcategories/create/', views.SubcategoryCreateView.as_view(), name='subcategory-create'),
    path('subcategories/<int:pk>/update/', views.SubcategoryUpdateView.as_view(), name='subcategory-update'),
    path('subcategories/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory-delete'),
]