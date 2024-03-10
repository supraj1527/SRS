# Generated by Django 4.2.5 on 2023-09-18 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0006_alter_facultycoursemappings_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="FCourseMappings",
            fields=[
                ("mapid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "Course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.course",
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.faculty",
                    ),
                ),
            ],
            options={
                "db_table": "fcoursemapp_table",
            },
        ),
    ]