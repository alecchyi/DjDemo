from django.db import models


class Member(models.Model):
    '''
    Member
    '''
    #Constants
    STATUS = {"normal":0, "deleted":2}
    REG_ROLES = ["teacher", "parent", "student"]
    
    #attributes
    username = models.CharField(max_length=45);
    password = models.CharField(max_length=45);
    email = models.CharField(max_length=45);
    status = models.SmallIntegerField(0);
    real_name = models.CharField(max_length=45);
    image_url = models.FilePathField(max_length=200);
    birth = models.DateTimeField(blank=True, null=True);
    reg_role = models.CharField(max_length=45);
    age = models.SmallIntegerField(null=True);
    gender = models.NullBooleanField(null=True);
    address = models.CharField(max_length=500);
    created_at = models.DateTimeField(auto_now=True);
    updated_at = models.DateTimeField(auto_now=True);
    salt = models.CharField(max_length=100);
    reg_from = models.CharField(max_length=45);
    phone = models.CharField(max_length=45);
    cellphone = models.CharField(max_length=45);
    nickname = models.CharField(max_length=100);
    domain = models.IntegerField(100, max_length=10, null=True)
    row_id = models.IntegerField(max_length=10, null=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    quota = models.IntegerField(max_length=10, null=True)
    last_login = models.DateTimeField(null=True)
    rel_teacher = models.IntegerField(max_length=10, null=True)
    
class UserGroup(models.Model):
    '''
        a set of  members
    '''
    
    GROUP_TYPE = {"country":1, "province":2, "city":3, "distict":4, "school":5, 
                  "grade":6, "classroom":7, "group":8}
    STATUS = {"normal":0, "wait_approve":1, "deleted":2}
    
    name = models.CharField(max_length=100)
    group_type = models.SmallIntegerField()
    parent_id = models.IntegerField()
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
        
    
class GroupUserRelation(models.Model):
    '''
      a relation table between user and user_group
    '''
    
    STATUS = {"noraml":0, "deleted":1}
    ROLE = {"admin":0, "member":1,}
    
#     user_id = models.IntegerField()
    user_group = models.ForeignKey(UserGroup)
    status = models.SmallIntegerField()
    role = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Member)

        
class Role(models.Model):
    '''
        roles for all members
    '''
    
    STATUS = {"normal":0}
    
    name = models.CharField(max_length=50)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    

class UserRole(models.Model):
    ''' relation between user and role '''
    
    member = models.ForeignKey(Member)
    role = models.ForeignKey(Role)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Menu(models.Model):
    ''' menu'''
    
    MENU_TYPE = {"menu":0, "function":1}
    STATUS = {"normal":0}
    
    name = models.CharField(max_length=45)
    slug = models.CharField(max_length=45)     #slug for name, such as "authhome"
    menu_type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    member = models.ForeignKey(Member)    #creator id
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class MenuRole(models.Model):
    ''' relation between menu and role '''
    
    menu = models.ForeignKey(Menu)
    role = models.ForeignKey(Role)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Tag(models.Model):
    
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Blog(models.Model):
    
    title = models.CharField(max_length=100)
    member = models.ForeignKey(Member)
    content = models.TextField()
    blog_type = models.SmallIntegerField(max_length=2)
    status = models.SmallIntegerField(max_length=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    