# Generated by Django 4.2.1 on 2023-07-07 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vantablack', '0002_activity_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_history',
            name='activity_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.commentviews'),
        ),
        migrations.AlterField(
            model_name='activity_history',
            name='activity_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.postviews'),
        ),
        migrations.AlterField(
            model_name='activity_history',
            name='shared_to_profile',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]