from django.db import models
from django.contrib.auth import get_user_model

from wagtail.fields import RichTextField
from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail.admin.panels import FieldPanel, FieldRowPanel

from staff.models import Profile

class Article(models.Model):

    class Section(models.TextChoices):
        UNASSIGNED = "UNA", "unassigned"
        AT_SCITECH = 'SCT', "at scitech"
        IN_PITTSBURGH = "PIT", "in pittsburgh"
        POLITICS = "POL", "politics"
        TECHNOLOGY = "TEC", "technology"
        SPORTS = "SPT", "sports"
        BLOG = "BLG", "blog"
    
    class Priority(models.IntegerChoices):
        LOW = 0, "low"
        NORMAL = 1, "normal"
        HIGH = 2, "high"
        HIGHEST = 3, "highest"

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

    # article stuff
    section = models.CharField(max_length=3, choices=Section.choices, default=Section.UNASSIGNED)
    title = models.CharField(max_length=100)
    prologue = RichTextField(blank=True)
    content = RichTextField(blank=True)

    # for author to change when done writing
    needs_approval = models.BooleanField(default=False,verbose_name="done writing")
    needs_approval_date = models.DateTimeField(blank=True,null=True,verbose_name="date done writing")

    # for editors
    approved = models.BooleanField(default=False,verbose_name="approved for publishing")
    approved_date = models.DateTimeField(blank=True,null=True,verbose_name="date approved for publishing")

    published = models.BooleanField(default=False,verbose_name="publish")
    pub_date = models.DateTimeField(blank=True, null=True,verbose_name="date published")

    # for superusers/editors in chief
    priority = models.IntegerField(choices=Priority.choices,default=Priority.NORMAL)

    def __str__(self):
        return self.title

