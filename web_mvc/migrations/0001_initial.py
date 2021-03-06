# Generated by Django 2.0.2 on 2018-02-27 04:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('eth_address', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribute_date', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('value', models.DecimalField(decimal_places=27, max_digits=30)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_mvc.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('last_edited_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_mvc.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Reputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuate', models.CharField(choices=[(0, 'Not Evaluated Yet'), (1, 'One Star'), (2, 'Two Star'), (3, 'Three Star'), (4, 'Four Star'), (5, 'Five Star')], default=0, max_length=1)),
                ('reputee_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_mvc.Author')),
                ('reputee_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_mvc.Post')),
            ],
        ),
        migrations.AddField(
            model_name='contribution',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_mvc.Post'),
        ),
    ]
