from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies =[

    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=8,decimal_places=2, default= 0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),              
            ],
        ),
    ]