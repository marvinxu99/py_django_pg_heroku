# Generated by Django 3.0.7 on 2020-08-23 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import itrac.models.project


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('code', models.CharField(default='WINN', max_length=20)),
                ('slug', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=40, null=True)),
                ('URL', models.CharField(max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, upload_to=itrac.models.project.get_avatar_full_path)),
                ('avatar_version', models.IntegerField(blank=True, default=0, editable=False)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ['title'],
            },
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='issue_prefix',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.AddField(
            model_name='issue',
            name='coded_id',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('1', '1 - highest'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 - lowest')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['coded_id'], name='itrac_issue_coded_i_2094ef_idx'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Issues', to='itrac.Project'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['title'], name='itrac_proje_title_8071b7_idx'),
        ),
    ]
