# Generated by Django 4.2.4 on 2023-08-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0006_alter_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='type',
            field=models.CharField(choices=[('family', 'Family'), ('bachelor', 'Bachelor'), ('sublet', 'Sublet')], default='family', max_length=10),
        ),
    ]
