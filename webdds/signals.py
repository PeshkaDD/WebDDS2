from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Status, OperationType


@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'dds':
        # Статусы
        default_statuses = ['Бизнес', 'Личное', 'Налог']
        existing_statuses = Status.objects.values_list('name', flat=True)

        for status in default_statuses:
            if status not in existing_statuses:
                Status.objects.create(name=status)

        # Типы операций
        default_operation_types = ['Пополнение', 'Списание']
        existing_operation_types = OperationType.objects.values_list('name', flat=True)

        for op_type in default_operation_types:
            if op_type not in existing_operation_types:
                OperationType.objects.create(name=op_type)