# Generated by Django 3.2 on 2023-08-11 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0017_alter_board_info_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.BooleanField(default=False)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_region', to='boards.regioncategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='star_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
