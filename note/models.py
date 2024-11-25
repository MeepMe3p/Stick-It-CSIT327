from django.db import models
# from board import models
# from board.models import Board, ProjectBoard, SimpleBoard
from django.apps import apps

# Create your models here.
# SAUCE: https://docs.djangoproject.com/en/5.1/topics/db/models/
class Note(models.Model):
    content = models.TextField()
    border_color = models.CharField(max_length=10)  # Assuming you store the color as a hex code
    coordinates = models.JSONField()  # Storing x and y as a JSON object
    is_finished = models.BooleanField(default=False)
    checkbox_id = models.CharField(max_length=100)

    def toggle_complete(self):
        self.is_finished = not self.is_finished
        self.save()
        
        # Lazy load the Board and update progress if the board is a ProjectBoard
        Board = apps.get_model('board', 'Board')
        if isinstance(self.board, Board) and self.board.board_type == 'project':
            self.board.update_progress()

    def __str__(self):
        return self.content
