# Generated by Django 4.2 on 2023-04-22 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0012_remove_projectrolereview_headline_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectrolereview",
            name="member",
        ),
        migrations.AddField(
            model_name="projectrolereview",
            name="role",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="projects.projectrole",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="projectrolereview",
            name="reviewer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews_written",
                to="projects.projectrole",
            ),
        ),
    ]
