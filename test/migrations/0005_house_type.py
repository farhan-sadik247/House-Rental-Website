# Generated by Django 4.2.4 on 2023-08-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_house_bathroom_no_house_bedroom_no_house_flat_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='type',
            field=models.CharField(choices=[('FM', 'Family'), ('BC', 'Bachelor'), ('SB', 'Sublet')], default='FM', max_length=2),
        ),
    ]
