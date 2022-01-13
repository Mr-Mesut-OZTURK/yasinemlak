# Generated by Django 4.0.1 on 2022-01-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emlak', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='email',
            new_name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='cc_myself',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
