# Generated by Django 4.1.2 on 2022-11-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=5, verbose_name='Enquete'),
        ),
    ]
