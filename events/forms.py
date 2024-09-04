from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_time', 'end_time', 'capacity', 'categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
