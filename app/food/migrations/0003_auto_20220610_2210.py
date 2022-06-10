# Generated by Django 3.2.13 on 2022-06-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_food_carbohydrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='carbohydrate',
            field=models.CharField(choices=[('ND', 'Noodles'), ('RE', 'Rice'), ('NA', 'Not Applied'), ('UD', 'Not sure')], default='UD', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='color',
            field=models.CharField(choices=[('YL', 'Yellow'), ('RD', 'Red'), ('BR', 'Brown'), ('BL', 'Black'), ('NA', 'Not Applied'), ('UD', 'Not sure')], default='UD', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='country',
            field=models.CharField(choices=[('KR', 'Korean'), ('JP', 'Japanese'), ('NA', 'Not Applied'), ('UD', 'Not sure')], default='UD', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.CharField(choices=[('BF', 'Beef'), ('PR', 'Pork'), ('SF', 'Shell fish'), ('FS', 'Fish'), ('VG', 'Vegetarian'), ('CK', 'Chicken'), ('NA', 'No Meat'), ('UD', 'Not sure')], default='UD', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='taste',
            field=models.CharField(choices=[('SW', 'Sweet'), ('SC', 'Spicy'), ('SR', 'Sour'), ('SL', 'Salty'), ('BT', 'Bitter'), ('NA', 'Not Applied'), ('UD', 'Not sure')], default='UD', max_length=2),
        ),
        migrations.AlterField(
            model_name='food',
            name='type',
            field=models.CharField(choices=[('BD', 'Boiled'), ('FR', 'Fried'), ('ST', 'Steamed'), ('BE', 'Baked'), ('BQ', 'Barbeque'), ('RW', 'Raw'), ('NA', 'Not Applied'), ('UD', 'Not sure')], default='UD', max_length=2),
        ),
    ]