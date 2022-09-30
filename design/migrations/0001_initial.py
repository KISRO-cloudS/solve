# Generated by Django 3.1.7 on 2022-09-23 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', models.TextField(default='about our app', max_length=1000)),
                ('service_title', models.CharField(default='service_name', max_length=100)),
                ('service_description', models.TextField(default='about our service', max_length=300)),
                ('service_title2', models.CharField(default='service_name', max_length=100)),
                ('service_description2', models.TextField(default='about our service', max_length=300)),
                ('service_title3', models.CharField(default='service_name', max_length=100)),
                ('service_description3', models.TextField(default='about our service', max_length=300)),
                ('team_member_name1', models.CharField(default='name', max_length=70)),
                ('team_member_role1', models.CharField(default='role', max_length=100)),
                ('team_member_image1', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
                ('team_member_name2', models.CharField(default='name', max_length=70)),
                ('team_member_role2', models.CharField(default='role', max_length=100)),
                ('team_member_image2', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
                ('team_member_name3', models.CharField(default='name', max_length=70)),
                ('team_member_role3', models.CharField(default='role', max_length=100)),
                ('team_member_image3', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
                ('team_member_name4', models.CharField(default='name', max_length=70)),
                ('team_member_role4', models.CharField(default='role', max_length=100)),
                ('team_member_image4', models.ImageField(default='about_pics/sw.png', upload_to='about_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Academic_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Digital_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('model', models.CharField(default='model', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Fashion_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Interior_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('model', models.CharField(default='model', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
                ('ingredient', models.CharField(default='None', max_length=100)),
                ('expired', models.DateField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Self_Care_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
                ('ingredient', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Talent_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('model', models.CharField(default='model', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Travel_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('new_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('old_price', models.CharField(default='00', max_length=1000000000000000000000)),
                ('Percentage_Discount', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(choices=[('Hot', 'Hot'), ('Free', 'Free'), ('New', 'New'), ('Buy', 'Buy'), ('Shop', 'Shop'), ('Order', 'Order'), ('4U', '4U'), ('Sure', 'Sure')], default='', max_length=1000)),
                ('image', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image1', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image2', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('image3', models.ImageField(default='cart_pics/sw.png', upload_to='cart_pics')),
                ('video', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('out_of', models.CharField(default='material', max_length=100)),
                ('model', models.CharField(default='model', max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='color', max_length=100)),
                ('size', models.CharField(default='size', max_length=100)),
                ('aim', models.CharField(default='Your_aim', max_length=100)),
                ('visit', models.URLField(default='http://', max_length=1000)),
                ('description', models.TextField(default='about_the_product', max_length=10000)),
                ('user', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='', max_length=1000)),
                ('category', models.CharField(choices=[('Selfcare Product', 'Selfcare Product'), ('Medical Product', 'Medical Product'), ('Talent Product', 'Talent Product'), ('Interior Product', 'Interior Product'), ('Academic Product', 'Academic Product'), ('Digital Product', 'Digital Product'), ('Travel Product', 'Travel Product'), ('Fashion and Design Product', 'Fashion and Design Product')], default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='+', max_length=15)),
                ('message', models.TextField(default='tell us something..', max_length=10000)),
                ('company', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solve_of', models.CharField(choices=[('Academic problems', 'Academic problems'), ('Agricultural problems', 'Agricultural problems'), ('Adventure problems', 'Adventure problems'), ('Anxiety problems', 'Anxiety problems'), ('Business problems', 'Business problems'), ('Biological problems', 'Biological problems'), ('Chemical problems', 'Chemical problems'), ('Ceremonic problems', 'Ceremonic problems'), ('Confidential problems', 'Confidential problems'), ('Climentic problems', 'Climentic problems'), ('Depression problems', 'Depression problems'), ('Developmental problems', 'Developmental problems'), ('boredom problems', 'boredom problems'), ('Emotional problems', 'Emotional problems'), ('Environmental problems', 'Environmental problems'), ('Fashion and Design problems', 'Fashion and Design problems'), ('Financial problems', 'Financial problems'), ('Friendship problems', 'Friendship problems'), ('Freedom problems', 'Freedom problems'), ('Health problems', 'Health problems'), ('Love and Relationship problems', 'Love and Relationship problems'), ('Medical problems', 'Medical problems'), ('Mental problems', 'Mental problems'), ('Parental problems', 'Parental problems'), ('Political problems', 'Political problems'), ('Religious problems', 'Religious problems'), ('Research and Discovery problems', 'Research and Discovery problems'), ('Stress problems', 'Stress problems'), ('Shopping problems', 'Shopping problems'), ('Security problems', 'Security problems'), ('Self Defence problems', 'Self Defence problems'), ('Self Esteem problems', 'Self Esteem problems'), ('Self Care problems', 'Self Care problems'), ('Self Control problems', 'Self Control problems'), ('Sports problems', 'Sports problems'), ('Talental problems', 'Talental problems'), ('Technological problems', 'Technological problems'), ('Traditional problems', 'Traditional problems'), ('Travel problems', 'Travel problems'), ('Other problems', 'Other problems')], default='', max_length=1000)),
                ('profile_image', models.ImageField(default='profile_pics/sw.png', upload_to='profile_pics')),
                ('my_slug', models.CharField(default='my slug', max_length=20)),
                ('follow_me_on', models.TextField(default='www.other_sites.com', max_length=300)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=1000)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated')], default='', max_length=1000)),
                ('talent', models.CharField(default='None', max_length=100)),
                ('street', models.CharField(default='None', max_length=100)),
                ('place_of_birth', models.CharField(default='None', max_length=100)),
                ('country', models.CharField(default='None', max_length=100)),
                ('hobbies', models.CharField(default='None', max_length=100)),
                ('highest_level_of_education', models.CharField(default='None', max_length=100)),
                ('profession', models.CharField(default='None', max_length=100)),
                ('mobile_number', models.CharField(default='None', max_length=100)),
                ('religion', models.CharField(default='None', max_length=100)),
                ('occupation', models.CharField(default='None', max_length=100)),
                ('age', models.PositiveIntegerField(default=0)),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(choices=[('Academic problems', 'Academic problems'), ('Agricultural problems', 'Agricultural problems'), ('Adventure problems', 'Adventure problems'), ('Anxiety problems', 'Anxiety problems'), ('Business problems', 'Business problems'), ('Biological problems', 'Biological problems'), ('Chemical problems', 'Chemical problems'), ('Ceremonic problems', 'Ceremonic problems'), ('Confidential problems', 'Confidential problems'), ('Climentic problems', 'Climentic problems'), ('Depression problems', 'Depression problems'), ('Developmental problems', 'Developmental problems'), ('boredom problems', 'boredom problems'), ('Emotional problems', 'Emotional problems'), ('Environmental problems', 'Environmental problems'), ('Fashion and Design problems', 'Fashion and Design problems'), ('Financial problems', 'Financial problems'), ('Friendship problems', 'Friendship problems'), ('Freedom problems', 'Freedom problems'), ('Health problems', 'Health problems'), ('Love and Relationship problems', 'Love and Relationship problems'), ('Medical problems', 'Medical problems'), ('Mental problems', 'Mental problems'), ('Parental problems', 'Parental problems'), ('Political problems', 'Political problems'), ('Religious problems', 'Religious problems'), ('Research and Discovery problems', 'Research and Discovery problems'), ('Stress problems', 'Stress problems'), ('Shopping problems', 'Shopping problems'), ('Security problems', 'Security problems'), ('Self Defence problems', 'Self Defence problems'), ('Self Esteem problems', 'Self Esteem problems'), ('Self Care problems', 'Self Care problems'), ('Self Control problems', 'Self Control problems'), ('Sports problems', 'Sports problems'), ('Talental problems', 'Talental problems'), ('Technological problems', 'Technological problems'), ('Traditional problems', 'Traditional problems'), ('Travel problems', 'Travel problems'), ('Other problems', 'Other problems')], default='', max_length=1000)),
                ('A_brief_Discription', models.TextField(default='Tell Your Condition ...', max_length=1000)),
                ('clip', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('user_likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help', models.TextField(default='', max_length=2000)),
                ('clip', models.FileField(default='', upload_to='videos/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cauthor', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.post')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
