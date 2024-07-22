# Generated by Django 5.0.7 on 2024-07-19 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_submenuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenuitem',
            name='parent_menu_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
            preserve_default=False,
        ),
    ]