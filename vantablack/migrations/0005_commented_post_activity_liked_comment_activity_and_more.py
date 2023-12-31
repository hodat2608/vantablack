# Generated by Django 4.2.1 on 2023-07-09 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vantablack', '0004_alter_commentviews_comment_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='commented_post_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='liked_comment_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='liked_post_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_emotion', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_liked_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.postviews')),
                ('user_liked_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='repply_comment_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Repply_commentviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_message', models.TextField(blank=True, max_length=1000000, null=True)),
                ('rep_mess_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rep_comment_likes', models.ManyToManyField(blank=True, null=True, related_name='rep_comment_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='commentviews',
            name='message',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='activity_history',
        ),
        migrations.AddField(
            model_name='repply_commentviews',
            name='rep_commentviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.commentviews'),
        ),
        migrations.AddField(
            model_name='repply_commentviews',
            name='user_rep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='repply_comment_activity',
            name='comment_rep_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.commentviews'),
        ),
        migrations.AddField(
            model_name='repply_comment_activity',
            name='user_rep_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='liked_comment_activity',
            name='comment_liked_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.commentviews'),
        ),
        migrations.AddField(
            model_name='liked_comment_activity',
            name='user_liked_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commented_post_activity',
            name='comment_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.commentviews'),
        ),
        migrations.AddField(
            model_name='commented_post_activity',
            name='post_comment_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.postviews'),
        ),
        migrations.AddField(
            model_name='commented_post_activity',
            name='user_comment_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
