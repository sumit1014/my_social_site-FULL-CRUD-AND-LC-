# Generated by Django 3.1.7 on 2021-09-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_no', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=400)),
                ('blog_content', models.TextField()),
                ('author_name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=150)),
                ('blog_post_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]