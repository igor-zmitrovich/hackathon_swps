# Generated by Django 4.2 on 2023-04-22 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0011_rename_role_description_projectrole_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectrolereview",
            name="headline",
        ),
        migrations.RemoveField(
            model_name="projectrolereview",
            name="project",
        ),
        migrations.AlterField(
            model_name="projectrolereview",
            name="reviewer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews_written",
                related_query_name="review_written",
                to="projects.projectrole",
            ),
        ),
    ]