# Generated by Django 4.2.4 on 2024-02-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('PY', 'Pondicherry'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
