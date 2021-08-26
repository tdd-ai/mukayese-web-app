# Generated by Django 2.2.13 on 2021-02-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0079_add_code_upload_setup_vpc_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="desired_worker_instance",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="max_worker_instance",
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="min_worker_instance",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="worker_ami_type",
            field=models.CharField(
                blank=True, default="AL2_x86_64", max_length=256, null=True
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="worker_disk_size",
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="worker_instance_type",
            field=models.CharField(
                blank=True, default="t3.medium", max_length=256, null=True
            ),
        ),
    ]
