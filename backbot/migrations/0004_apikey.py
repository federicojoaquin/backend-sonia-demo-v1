# Generated by Django 4.2 on 2023-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backbot", "0003_alter_botsettings_company_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApiKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=100)),
            ],
        ),
    ]
