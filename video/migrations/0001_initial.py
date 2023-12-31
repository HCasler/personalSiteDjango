# Generated by Django 4.2.4 on 2023-09-01 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('manifestLoc', models.CharField(max_length=254)),
                ('thumbnailLoc', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistType', models.CharField(choices=[('video', 'Video'), ('audio', 'Audio'), ('subti', 'Subtitle'), ('ifram', 'Iframes')], default='video', max_length=5)),
                ('bandwidth', models.BigIntegerField(blank=True, null=True)),
                ('storageLoc', models.CharField(max_length=254)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video')),
            ],
        ),
        migrations.CreateModel(
            name='MediaSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmentNum', models.IntegerField()),
                ('storageLoc', models.CharField(max_length=254)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.playlist')),
            ],
        ),
    ]
