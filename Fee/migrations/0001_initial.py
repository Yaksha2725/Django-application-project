# Generated by Django 5.0.6 on 2024-05-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_id', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('fee_paid', models.CharField(max_length=14)),
                ('date_of_payment', models.DateField()),
                ('due', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=50)),
            ],
        ),
    ]
