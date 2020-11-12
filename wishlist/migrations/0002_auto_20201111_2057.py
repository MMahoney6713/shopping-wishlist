# Generated by Django 2.2.5 on 2020-11-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='email',
            field=models.EmailField(default='name@email.com', max_length=254),
            preserve_default=False,
        ),
    ]
