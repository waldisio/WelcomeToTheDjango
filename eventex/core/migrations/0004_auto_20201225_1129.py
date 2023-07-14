# Generated by Django 3.1.4 on 2020-12-25 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contato', 'verbose_name_plural': 'contatos'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='kind',
            field=models.CharField(choices=[('E', 'Email'), ('P', 'Telefone')], max_length=1, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.speaker', verbose_name='palestrante'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.CharField(max_length=255, verbose_name='valor'),
        ),
    ]
