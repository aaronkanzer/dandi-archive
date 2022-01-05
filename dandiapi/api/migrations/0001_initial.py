# Generated by Django 3.1.7 on 2021-03-16 16:39

import uuid

import django.contrib.postgres.indexes
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields

import dandiapi.api.models.asset
import dandiapi.api.models.version
import dandiapi.api.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('path', models.CharField(max_length=512)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetBlob',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                ('uuid', models.UUIDField(unique=True)),
                (
                    'blob',
                    models.FileField(
                        blank=True,
                        storage=dandiapi.api.storage.get_storage,
                        upload_to=dandiapi.api.storage.get_storage_prefix,
                    ),
                ),
                (
                    'sha256',
                    models.CharField(
                        blank=True,
                        max_length=64,
                        null=True,
                        validators=[django.core.validators.RegexValidator('^[0-9a-f]{64}$')],
                    ),
                ),
                (
                    'etag',
                    models.CharField(
                        max_length=40,
                        validators=[
                            django.core.validators.RegexValidator('^[0-9a-f]{32}(-[1-9][0-9]*)?$')
                        ],
                    ),
                ),
                ('size', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AssetMetadata',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                ('metadata', models.JSONField(blank=True, default=dict, unique=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dandiset',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
            ],
            options={
                'ordering': ['id'],
                'permissions': [('owner', 'Owns the dandiset')],
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                (
                    'blob',
                    models.FileField(
                        blank=True,
                        storage=dandiapi.api.storage.get_storage,
                        upload_to=dandiapi.api.storage.get_storage_prefix,
                    ),
                ),
                (
                    'etag',
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=40,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator('^[0-9a-f]{32}(-[1-9][0-9]*)?$')
                        ],
                    ),
                ),
                ('upload_id', models.UUIDField(db_index=True, unique=True)),
                ('size', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                (
                    'version',
                    models.CharField(
                        default='draft',
                        max_length=13,
                        validators=[
                            django.core.validators.RegexValidator('^(0\\.\\d{6}\\.\\d{4})|draft$')
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='VersionMetadata',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name='created'
                    ),
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name='modified'
                    ),
                ),
                ('metadata', models.JSONField(default=dict)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddIndex(
            model_name='versionmetadata',
            index=django.contrib.postgres.indexes.HashIndex(
                fields=['metadata'], name='api_version_metadat_1146a6_hash'
            ),
        ),
        migrations.AddIndex(
            model_name='versionmetadata',
            index=django.contrib.postgres.indexes.HashIndex(
                fields=['name'], name='api_version_name_ed2a83_hash'
            ),
        ),
        migrations.AddField(
            model_name='version',
            name='dandiset',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='versions',
                to='api.dandiset',
            ),
        ),
        migrations.AddField(
            model_name='version',
            name='metadata',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='versions',
                to='api.versionmetadata',
            ),
        ),
        migrations.AddIndex(
            model_name='upload',
            index=models.Index(fields=['etag'], name='api_upload_etag_a467fd_idx'),
        ),
        migrations.AddIndex(
            model_name='assetblob',
            index=django.contrib.postgres.indexes.HashIndex(
                fields=['etag'], name='api_assetbl_etag_cf8377_hash'
            ),
        ),
        migrations.AddField(
            model_name='asset',
            name='blob',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='assets',
                to='api.assetblob',
            ),
        ),
        migrations.AddField(
            model_name='asset',
            name='metadata',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='assets',
                to='api.assetmetadata',
            ),
        ),
        migrations.AddField(
            model_name='asset',
            name='previous',
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='api.asset',
            ),
        ),
        migrations.AddField(
            model_name='asset',
            name='versions',
            field=models.ManyToManyField(related_name='assets', to='api.Version'),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together={('dandiset', 'version')},
        ),
    ]
