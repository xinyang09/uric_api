# Generated by Django 3.2 on 2022-10-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('host', '0003_host_environment'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorParams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='描述信息')),
            ],
            options={
                'verbose_name': '监控参数类型',
                'verbose_name_plural': '监控参数类型',
                'db_table': 'monitor_params',
            },
        ),
        migrations.CreateModel(
            name='MonitorHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(max_length=255, verbose_name='时间间隔')),
                ('host', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='host.host', verbose_name='主机')),
            ],
            options={
                'verbose_name': '监控主机列表',
                'verbose_name_plural': '监控主机列表',
                'db_table': 'monitor_host',
            },
        ),
    ]