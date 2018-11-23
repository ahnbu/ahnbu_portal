# Generated by Django 2.1.3 on 2018-11-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('discount_price', models.PositiveIntegerField(blank=True, default=0)),
                ('category', models.CharField(max_length=20)),
                ('link', models.TextField()),
                ('update_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-update_date', '-id'],
            },
        ),
    ]
