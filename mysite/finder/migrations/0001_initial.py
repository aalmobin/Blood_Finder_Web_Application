# Generated by Django 3.1.1 on 2021-02-18 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=256, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B-', 'B-'), ('O+', 'O-')], max_length=10, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('Location', models.CharField(blank=True, max_length=256, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=256, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('img', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]