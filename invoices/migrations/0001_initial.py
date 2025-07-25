# Generated by Django 5.2.4 on 2025-07-18 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("persons", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("B", "buy"), ("S", "sell")], max_length=1
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("D", "Draft"), ("C", "Confirmed")], default="D"
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("total", models.PositiveBigIntegerField(default=0)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="invoices",
                        to="persons.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="InvoiceItem",
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
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.PositiveIntegerField()),
                ("count", models.PositiveIntegerField()),
                ("discount", models.IntegerField(default=0)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoiceitems",
                        to="invoices.invoice",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
