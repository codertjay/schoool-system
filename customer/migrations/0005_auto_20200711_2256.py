# Generated by Django 3.0.7 on 2020-07-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='codertjay@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
