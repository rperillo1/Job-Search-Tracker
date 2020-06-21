# Generated by Django 3.0.2 on 2020-06-21 18:20

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='company',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='date_applied',
            field=models.DateField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.TextField(default='descrip'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='interest_level',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='notes',
            field=models.TextField(default='notes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='salary',
            field=models.CharField(default='20,000', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('A', 'Applied'), ('C', 'Contacted Back'), ('R', 'Recruiter Touch'), ('F', '1st Interview'), ('S', '2nd Interview'), ('T', '3rd Interview')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='application',
            name='title',
            field=models.CharField(default='jr web dev', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='company_info',
            field=models.TextField(default='google'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='preparation_text',
            field=models.TextField(default='get rdy for interview'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='questions',
            field=models.TextField(default='what do you value in an employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='rating',
            field=models.IntegerField(default='5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(default='Django', max_length=100),
            preserve_default=False,
        ),
    ]
