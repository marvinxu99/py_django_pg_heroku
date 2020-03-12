# Generated by Django 3.0.4 on 2020-03-12 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('choice_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CodeValue',
            fields=[
                ('code_value', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('code_set', models.IntegerField()),
                ('definition', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=60)),
                ('display', models.CharField(max_length=40)),
                ('display_key', models.CharField(max_length=40)),
                ('update_appctx', models.IntegerField(default=0, verbose_name='Update Application Context')),
                ('update_count', models.IntegerField(default=1, verbose_name='Update Application Context')),
                ('update_dt_tm', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('update_id', models.IntegerField(default=0, verbose_name='Updated by')),
                ('update_task', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'code_value',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name_first', models.CharField(max_length=128, verbose_name='Fist Name')),
                ('name_middle', models.CharField(blank=True, max_length=128, verbose_name='Middle Name')),
                ('name_last', models.CharField(max_length=128, verbose_name='Last Name')),
                ('name_full_formatted', models.CharField(max_length=128, verbose_name='Full Name')),
                ('is_active', models.BooleanField(verbose_name='Active')),
                ('active_status_cd', models.IntegerField(verbose_name='Active Status')),
                ('active_status_dt_tm', models.DateTimeField(verbose_name='Active Status Date')),
                ('person_type_cd', models.IntegerField(verbose_name='User Type')),
                ('created_dt_tm', models.DateTimeField(verbose_name='Date Created')),
                ('update_dt_tm', models.DateTimeField(verbose_name='Date Updated')),
                ('update_id', models.IntegerField(verbose_name='Updated by')),
            ],
        ),
        migrations.CreateModel(
            name='PersonImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('number', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('opened', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person_Alias',
            fields=[
                ('person_alias_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('active_ind', models.BooleanField(verbose_name='Active')),
                ('active_status_cd', models.IntegerField(verbose_name='Ative Status')),
                ('alias', models.CharField(max_length=200, verbose_name='Alias')),
                ('alias_expiry_dt_tm', models.DateTimeField(verbose_name='Alias Expiry Date')),
                ('alias_pool_cd', models.BigIntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Person')),
            ],
        ),
        migrations.AddIndex(
            model_name='codevalue',
            index=models.Index(fields=['code_set'], name='code_set_idx'),
        ),
        migrations.AddIndex(
            model_name='codevalue',
            index=models.Index(fields=['display_key'], name='display_key_idx'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]