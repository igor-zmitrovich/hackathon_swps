# Generated by Django 4.2 on 2023-04-22 09:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0013_remove_projectrolereview_member_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectrolereview",
            old_name="reviewer",
            new_name="reviewer_role",
        ),
    ]