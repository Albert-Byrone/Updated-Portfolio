# Generated by Django 2.2.7 on 2019-12-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=400)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(verbose_name='contact message')),
            ],
        ),
    ]
