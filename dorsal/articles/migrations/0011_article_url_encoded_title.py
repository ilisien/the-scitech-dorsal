# Generated by Django 4.0.7 on 2022-12-26 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_prologue'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url_encoded_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
