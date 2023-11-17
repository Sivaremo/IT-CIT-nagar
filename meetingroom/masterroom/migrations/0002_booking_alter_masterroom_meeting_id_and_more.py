# Generated by Django 4.2.7 on 2023-11-17 17:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('masterroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookingname', models.CharField(max_length=1000)),
                ('Starting_Time', models.TimeField()),
                ('Ending_Time', models.TimeField()),
                ('date', models.DateField()),
                ('Purpose_of_meeting', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='masterroom',
            name='meeting_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=10000, unique=True),
        ),
        migrations.DeleteModel(
            name='BookingDates',
        ),
        migrations.AddField(
            model_name='booking',
            name='Booking_Room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterroom.masterroom'),
        ),
    ]
