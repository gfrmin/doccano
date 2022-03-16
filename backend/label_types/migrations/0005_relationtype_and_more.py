# Generated by Django 4.0.2 on 2022-02-22 05:11

from django.db import migrations, models
import django.db.models.deletion
import label_types.models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_project_polymorphic_ctype"),
        ("label_types", "0004_rename_relationtype_relationtypeold"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelationType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(db_index=True, max_length=100)),
                (
                    "prefix_key",
                    models.CharField(
                        blank=True,
                        choices=[("ctrl", "ctrl"), ("shift", "shift"), ("ctrl shift", "ctrl shift")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "suffix_key",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("0", "0"),
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("a", "a"),
                            ("b", "b"),
                            ("c", "c"),
                            ("d", "d"),
                            ("e", "e"),
                            ("f", "f"),
                            ("g", "g"),
                            ("h", "h"),
                            ("i", "i"),
                            ("j", "j"),
                            ("k", "k"),
                            ("l", "l"),
                            ("m", "m"),
                            ("n", "n"),
                            ("o", "o"),
                            ("p", "p"),
                            ("q", "q"),
                            ("r", "r"),
                            ("s", "s"),
                            ("t", "t"),
                            ("u", "u"),
                            ("v", "v"),
                            ("w", "w"),
                            ("x", "x"),
                            ("y", "y"),
                            ("z", "z"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "background_color",
                    models.CharField(default=label_types.models.generate_random_hex_color, max_length=7),
                ),
                ("text_color", models.CharField(default="#ffffff", max_length=7)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="projects.project")),
            ],
            options={
                "ordering": ["created_at"],
                "abstract": False,
            },
        ),
        migrations.AddConstraint(
            model_name="relationtype",
            constraint=models.UniqueConstraint(fields=("project", "text"), name="label_types_relationtype_is_unique"),
        ),
    ]