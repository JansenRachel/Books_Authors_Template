# Generated by Django 2.2 on 2021-08-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='no value submitted'),
            preserve_default=False,
        ),
    ]