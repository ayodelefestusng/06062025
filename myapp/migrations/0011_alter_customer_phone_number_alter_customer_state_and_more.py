# Generated by Django 5.2.1 on 2025-06-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_customer_email_alter_customer_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('AB', 'Abia'), ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), ('SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara')], max_length=150),
        ),
        migrations.AlterField(
            model_name='llm',
            name='cedi',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=50),
        ),
        migrations.AlterField(
            model_name='llm',
            name='euro',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=50),
        ),
        migrations.AlterField(
            model_name='llm',
            name='naira',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=50),
        ),
        migrations.AlterField(
            model_name='llm',
            name='pound',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=50),
        ),
        migrations.AlterField(
            model_name='llm',
            name='usd',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='retailoutlet',
            name='state',
            field=models.CharField(choices=[('AB', 'Abia'), ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), ('SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara')], max_length=150),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='state',
            field=models.CharField(choices=[('AB', 'Abia'), ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), ('SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara')], max_length=150),
        ),
    ]
