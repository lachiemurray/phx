# Generated by Django 2.1.5 on 2019-03-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190309_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='text_size',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='large', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='text_size',
            field=models.CharField(choices=[('small', 'Small'), ('large', 'Large')], default='large', max_length=200),
            preserve_default=False,
        ),
    ]
