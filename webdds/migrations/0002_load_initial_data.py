from django.db import migrations


def load_initial_data(apps, schema_editor):
    Status = apps.get_model('webdds', 'Status')
    OperationType = apps.get_model('webdds', 'OperationType')

    # Создаем статусы
    statuses = ['Бизнес', 'Личное', 'Налог']
    for status in statuses:
        Status.objects.get_or_create(name=status)

    # Создаем типы операций
    operation_types = ['Пополнение', 'Списание']
    for op_type in operation_types:
        OperationType.objects.get_or_create(name=op_type)


class Migration(migrations.Migration):
    dependencies = [
        # Укажите последнюю миграцию вашего приложения
        ('webdds', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]