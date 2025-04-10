from django.db import models
from django.contrib.auth.models import User

class Question(models.Model): # Model to store questions
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model): # Model to store question answers
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers')

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Answer to {self.question.title}"