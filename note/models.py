from django.db import models
# from board import models
# from board.models import Board, ProjectBoard, SimpleBoard
from django.apps import apps

# Create your models here.
# SAUCE: https://docs.djangoproject.com/en/5.1/topics/db/models/
class Note(models.Model):
    content = models.TextField()
    board = models.ForeignKey('board.Board', null=True, related_name='notes', on_delete=models.SET_NULL) 

    is_completed = models.BooleanField(default=False)

    def toggle_complete(self):
        self.is_completed = not self.is_completed
        self.save()
        
        # Lazy load the Board and update progress if the board is a ProjectBoard
        Board = apps.get_model('board', 'Board')
        if isinstance(self.board, Board) and self.board.board_type == 'project':
            self.board.update_progress()

    def __str__(self):
        return self.content
