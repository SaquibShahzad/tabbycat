# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venues', '0001_initial'),
        ('tournaments', '0001_initial'),
        ('draw', '0002_teamvenuepreference_team'),
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamvenuepreference',
            name='venue_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.VenueGroup'),
        ),
        migrations.AddField(
            model_name='teampositionallocation',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round'),
        ),
        migrations.AddField(
            model_name='teampositionallocation',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team'),
        ),
        migrations.AddField(
            model_name='debateteam',
            name='debate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.Debate'),
        ),
        migrations.AddField(
            model_name='debateteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team'),
        ),
        migrations.AddField(
            model_name='debate',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Division'),
        ),
        migrations.AddField(
            model_name='debate',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round'),
        ),
        migrations.AddField(
            model_name='debate',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='venues.Venue'),
        ),
        migrations.AlterUniqueTogether(
            name='teampositionallocation',
            unique_together=set([('round', 'team')]),
        ),
    ]
