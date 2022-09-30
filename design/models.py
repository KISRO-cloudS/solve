
from django.db import models

import datetime
from	django.utils	import	timezone

from django.contrib.auth.models import User, Group, Permission
  
from PIL import Image

from mimetypes import guess_type
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver







#  m o d e l  s y s t e m

category= (
	('Selfcare Product','Selfcare Product'),
	('Medical Product','Medical Product'),
	('Talent Product','Talent Product'),
	('Interior Product','Interior Product'),
	('Academic Product','Academic Product'),
	('Digital Product','Digital Product'),
	('Travel Product','Travel Product'),
	('Fashion and Design Product','Fashion and Design Product'),
	)

#Cart
user = (
	('Male','Male'),
	('Female','Female'),
	('Both','Both'),
	
	)


#Cart
value = (
	('Hot','Hot'),
	('Free','Free'),
	('New','New'),
	('Buy','Buy'),
	('Shop','Shop'),
	('Order','Order'),
	('4U','4U'),
	('Sure','Sure'),
	)


sex = (
	('Male','Male'),
	('Female','Female'),
	
	
	)


marital_status = (
	('Married','Married'),
	('Single','Single'),
	('Divorced','Divorced'),
	('Widowed','Widowed'),
	('Separated','Separated'),
	
	)


#Post

solve = (
		('Academic problems','Academic problems'),
		('Agricultural problems','Agricultural problems'),
		('Adventure problems','Adventure problems'),
		('Anxiety problems','Anxiety problems'),
		('Business problems','Business problems'),
		('Biological problems','Biological problems'),
		('Chemical problems','Chemical problems'),
		('Ceremonic problems','Ceremonic problems'),
		('Confidential problems','Confidential problems'),
		('Climentic problems','Climentic problems'),
		('Depression problems','Depression problems'),
		('Developmental problems','Developmental problems'),
		('boredom problems','boredom problems'),
		('Emotional problems','Emotional problems'),
		('Environmental problems','Environmental problems'),
		('Fashion and Design problems','Fashion and Design problems'),
		('Financial problems','Financial problems'),
		('Friendship problems','Friendship problems'),
		('Freedom problems','Freedom problems'),
		('Health problems','Health problems'),
		('Love and Relationship problems','Love and Relationship problems'),
		('Medical problems','Medical problems'),
		('Mental problems','Mental problems'),
		('Parental problems','Parental problems'),
		('Political problems','Political problems'),
		('Religious problems','Religious problems'),
		('Research and Discovery problems','Research and Discovery problems'),
		('Stress problems','Stress problems'),
		('Shopping problems','Shopping problems'),
		('Security problems','Security problems'),
		('Self Defence problems','Self Defence problems'),
		('Self Esteem problems','Self Esteem problems'),
		('Self Care problems','Self Care problems'),
		('Self Control problems','Self Control problems'),
		('Sports problems','Sports problems'),
		('Talental problems','Talental problems'),
		('Technological problems','Technological problems'),
		('Traditional problems','Traditional problems'),
		('Travel problems','Travel problems'),
		('Other problems','Other problems'),
		


		)

class Report(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(default='+', max_length=15)
	message = models.TextField(max_length=10000, default='tell us something..') 
	company = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=timezone.now)





class About_Us_Page(models.Model):
	main_description = models.TextField(max_length=1000, default='about our app')
	service_title = models.CharField(max_length=100, default='service_name')
	service_description = models.TextField(max_length=300, default='about our service')
	service_title2 = models.CharField(max_length=100, default='service_name')
	service_description2 = models.TextField(max_length=300, default='about our service')
	service_title3 = models.CharField(max_length=100, default='service_name')
	service_description3 = models.TextField(max_length=300, default='about our service')
	team_member_name1 = models.CharField(max_length=70, default='name')
	team_member_role1 = models.CharField(max_length=100, default='role')
	team_member_image1 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')
	team_member_name2 = models.CharField(max_length=70, default='name')
	team_member_role2 = models.CharField(max_length=100, default='role')
	team_member_image2 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')
	team_member_name3 = models.CharField(max_length=70, default='name')
	team_member_role3 = models.CharField(max_length=100, default='role')
	team_member_image3 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')
	team_member_name4 = models.CharField(max_length=70, default='name')
	team_member_role4 = models.CharField(max_length=100, default='role')
	team_member_image4 = models.ImageField(upload_to='about_pics', default='about_pics/sw.png')





#CART
class Fashion_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)



class Travel_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')	
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	model = models.CharField(max_length=100, default='model')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)



class Digital_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')	
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	model = models.CharField(max_length=100, default='model')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)





class Academic_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)



class Interior_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	model = models.CharField(max_length=100, default='model')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)




class Talent_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	model = models.CharField(max_length=100, default='model')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)




class Medical_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of = models.CharField(max_length=100,default='material')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)
	ingredient = models.CharField(max_length=100, default='None')
	expired = models.DateField(default='None')




class Self_Care_Cart(models.Model):
	title = models.CharField(max_length=100)
	new_price = models.CharField(default='00', max_length=1000000000000000000000)
	old_price = models.CharField(default='00', max_length=1000000000000000000000)
	Percentage_Discount = models.PositiveIntegerField(default=0)
	value = models.CharField(default='', max_length=1000,choices=value)
	image = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image1 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image2 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	image3 = models.ImageField(upload_to='cart_pics', default='cart_pics/sw.png')
	video = models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	out_of  = models.CharField(max_length=100,default='material')
	weight = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length=100,default='color')
	size = models.CharField(max_length=100,default='size')
	aim = models.CharField(max_length=100,default='Your_aim')
	visit = models.URLField(max_length=1000, default='http://')
	description = models.TextField(max_length=10000, default='about_the_product')
	user = models.CharField(default='', max_length=1000,choices=user)
	category = models.CharField(default='', max_length=1000,choices=category)
	ingredient = models.CharField(max_length=100, default='None')
	
		






# FOLLOWING AND FOLLOWERS





# POST

class Post(models.Model):
	author	=	models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
	problem = models.CharField(default='', max_length=1000,choices=solve)
	A_brief_Discription=models.TextField(max_length=1000,default="Tell Your Condition ...")
	clip=models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	user_likes = models.ManyToManyField(User)
	created_on = models.DateTimeField(default=timezone.now)
	likes = models.PositiveIntegerField(default=0)
	
	def total_likes(self):
		return self.user_likes.count()

	class Meta:
		ordering =['-created_on']	
    




	def clip_type_html(self):
		type_tuple = guess_type(self.clip.url, strict=True)
		if (type_tuple[0]).__contains__("image"):
			return "image"
		elif (type_tuple[0]).__contains__("video"):
			return "video"






class FollowersCount(models.Model):
	follower = models.CharField(max_length=1000)
	user =models.CharField(max_length=1000)

	def __str__(self):
         return self.user



# COMMENT

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	Help = models.TextField(default='', max_length=2000)
	clip=models.FileField(upload_to='videos/%Y/%m/%d/', default='')
	created_on = models.DateTimeField(default=timezone.now)
	author	=	models.ForeignKey(User, on_delete=models.CASCADE, related_name='cauthor', default='')

	def clip_type_html(self):
		type_tuple = guess_type(self.clip.url, strict=True)
		if (type_tuple[0]).__contains__("image"):
			return "image"
		elif (type_tuple[0]).__contains__("video"):
			return "video"	

	class Meta:
		ordering =['-created_on']







#  FOR PROFILE

class Profile(models.Model):
    solve_of = models.CharField(default='',max_length=1000,choices=solve)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_image=models.ImageField(upload_to='profile_pics', default='profile_pics/sw.png')
    my_slug = models.CharField(  max_length=20, default='my slug')
    following = models.ManyToManyField(User, blank=True, related_name= "following", symmetrical=False)
    follow_me_on = models.TextField(max_length=300, default='www.other_sites.com')
    sex = models.CharField(default='',max_length=1000,choices=sex)
    marital_status = models.CharField(default='',max_length=1000,choices=marital_status)
    talent = models.CharField(max_length=100, default='None')
    street = models.CharField(max_length=100, default='None')
    place_of_birth = models.CharField(max_length=100, default='None')
    country = models.CharField(max_length=100, default='None')
    hobbies = models.CharField(max_length=100, default='None')
    highest_level_of_education = models.CharField(max_length=100, default='None')
    profession = models.CharField(max_length=100, default='None')
    mobile_number = models.CharField(max_length=100, default='None')
    religion = models.CharField(max_length=100, default='None')
    occupation = models.CharField(max_length=100, default='None')
    age = models.PositiveIntegerField(default=0)
    



   


    
    def __str__(self):
         return f'{self.user.username} Profile'



    def save(self, *args, **kwargs):
    	super(Profile, self).save(*args, **kwargs)
    	img = Image.open(self.profile_image.path)
    	if img.height > 300 or img.width > 300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.profile_image.path)
    	 # Open image


    

    	


        
        
        # resize image
        
            
             # Resize image
            

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



