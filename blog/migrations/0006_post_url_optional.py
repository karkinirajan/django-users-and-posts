from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_post_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="url",
            field=models.URLField(blank=True, max_length=200),
        ),
    ]
