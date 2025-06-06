# Generated by Django 5.2.2 on 2025-06-05 12:46

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorGestor',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Numero_indentificacao', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=200)),
                ('Telefone', models.CharField(max_length=100)),
                ('Data_de_Nascimento', models.DateField(blank=True, null=True)),
                ('Data_de_contratacao', models.DateField(blank=True, null=True)),
                ('Usuario', models.CharField(choices=[('Professor', 'Professor'), ('Gestor', 'Gestor')], max_length=9)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('curso', models.CharField(blank=True, max_length=100, null=True)),
                ('carga_horaria', models.PositiveIntegerField(blank=True, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('Professor_responsavel', models.ForeignKey(blank=True, default=1, limit_choices_to={'Usuario': 'Professor'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_inicio', models.DateField(blank=True, null=True)),
                ('Data_termino', models.DateField(blank=True, null=True)),
                ('Periodo', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=10)),
                ('Professor_responsavel', models.ForeignKey(limit_choices_to={'Usuario': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Disciplina_professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
                ('Sala_reservada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sala')),
            ],
        ),
    ]
