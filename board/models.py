from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from note.models import Note

# Create your models here.

# Programmer Name: Elijah Rei Sabay
# I created this category for searching purposes, feel nako lisod if di sha iseparate entity
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_description = models.TextField(max_length=100)
    # ej changes

    # for displaying category name in url
    category_slug = models.SlugField(unique=True,editable=False)
    def save(self,*args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.category_name)
        super().save(*args,**kwargs)
    # 

    def __str__(self):
        return str(self.category_name)
    



class Board(models.Model):
    board_name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    BOARD_TYPES = (
        ('simple', 'Simple Board'),
        ('project', 'Project Board')
    )
    board_type = models.CharField(max_length=10, choices=BOARD_TYPES, default='simple')
    
    THEME = (
        ('white', 'Default (White)'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('pink', 'Pink')
    )
    board_theme = models.CharField(max_length=10, choices=THEME, default='white')

    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private')
    )
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')

    date_created = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_boards')  
    users = models.ManyToManyField(User, related_name='boards')
    user_count = models.IntegerField(default=1)

    def __str__(self):
        return self.board_name


class ProjectBoard(Board):
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        db_table = 'project_board'

    def update_progress(self):
        total_notes = self.notes.count()
        completed_notes = self.notes.filter(is_completed=True).count()
        self.progress = (completed_notes / total_notes) * 100 if total_notes > 0 else 0
        self.save()

    def save(self, *args, **kwargs):
        self.board_type = 'project'
        super().save(*args, **kwargs)
        # super(ProjectBoard, self).save(*args, **kwargs)


class SimpleBoard(Board):
    class Meta:
        db_table = 'simple_board'

    def save(self, *args, **kwargs):
        self.board_type = 'simple'
        super().save(*args, **kwargs)