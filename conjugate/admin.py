from django.contrib import admin
from .models import Conjugation, Language, Subject, Tense, Verb

# Register your models here.
admin.site.register(Conjugation)
admin.site.register(Language)
admin.site.register(Subject)
admin.site.register(Tense)
admin.site.register(Verb)
