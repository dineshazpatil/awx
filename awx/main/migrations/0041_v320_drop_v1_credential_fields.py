# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_v320_migrate_v1_credentials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credential',
            name='authorize',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='authorize_password',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='become_method',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='become_password',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='become_username',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='client',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='cloud',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='host',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='password',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='project',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='secret',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='security_token',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='ssh_key_data',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='ssh_key_unlock',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='subscription',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='username',
        ),
        migrations.RemoveField(
            model_name='credential',
            name='vault_password',
        ),
        migrations.AlterUniqueTogether(
            name='credentialtype',
            unique_together=set([('name', 'kind')]),
        ),
        migrations.AlterField(
            model_name='credential',
            name='credential_type',
            field=models.ForeignKey(related_name='credentials', to='main.CredentialType', null=False)
        )
    ]