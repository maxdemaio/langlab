from random import choice, randint

from django.contrib import messages
from django import forms
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Conjugation, Language, Subject, Tense, Verb


# Django form classes for tenses and conjugations
class TenseForm(forms.Form):
    tenses = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            attrs={"class": "form-control form-control-lg"}),
        required=True, 
        label="")

class ConjugationForm(forms.Form):
    your_conjugation = forms.CharField(label='Your conjugation', max_length=100, 
        widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    # Hidden input fields that will contain the tense ids, subjects, verbs instance
    tenseIDs = forms.CharField(widget=forms.HiddenInput())
    randTense = forms.CharField(widget=forms.HiddenInput())
    randSubj = forms.CharField(widget=forms.HiddenInput())
    randVerb = forms.CharField(widget=forms.HiddenInput())
    correctConj = forms.CharField(widget=forms.HiddenInput())


def conjugate(request):
    """ Conjugate Home """
    # Return a list of all languages
    languages = Language.objects.all()
    return render(request, "conjugate/index.html", {
        "languages": languages
    })


def tenses(request, lang_id):
    """ Conjugate Tenses """
    # Filter for tenses based on the language foreign key
    tenses = Tense.objects.filter(lang_id=lang_id)

    # Check if language has tenses
    if tenses:
        # Obtain language
        language = Language.objects.get(pk=lang_id)
        # Change instance of form and populate tenses for the chosen language
        form = TenseForm()
        form.fields['tenses'].choices = [(x.id, x) for x in tenses]

        return render(request, "conjugate/tenses.html", {
            "form": form,
            "language": language,
            "lang_id": lang_id
        })
    else:
        # Return 404 language not found
        return render(request, "conjugate/error.html", {
            "error": "404",
            "message": "Language not found,"
        })


def conjugations(request, lang_id):
    """ Conjugate Conjugations """
    # POST request
    if request.method == "POST":
        form = ConjugationForm(request.POST)

        # Form is valid
        if form.is_valid():
            tenseIDs = form.cleaned_data["tenseIDs"].strip('][').split(', ')
            randTense = form.cleaned_data["randTense"]
            randSubj = form.cleaned_data["randSubj"]
            randVerb = form.cleaned_data["randVerb"]
            your_conjugation = form.cleaned_data["your_conjugation"]
            correctConj = form.cleaned_data["correctConj"]
            
            # Verb conjugated correctly
            if your_conjugation == correctConj:
                # Recreate query string
                tenseIDs = "?tenses=" + "&tenses=".join(tenseIDs)

                # Repass in the language ID, and tenseIDs list as queries to the URL
                # Display a correct message
                messages.success(request, 'Correct!')
                return redirect(reverse("conjugations", args=[lang_id]) + tenseIDs)
            # Verb conjugated incorrectly
            else:
                # Set error message
                messages.error(request, f"Incorrect! The correct conjugation was '{correctConj}'.")
                
                # Recreate conjugation form and maintain chosen tense IDs
                tenseList = list(map(int, tenseIDs))
                form = ConjugationForm(initial={'tenseIDs': tenseList, 'randTense': randTense,
                    'randSubj': randSubj, 'randVerb': randVerb, 'correctConj': correctConj}, auto_id=False)
                
                return render(request, "conjugate/conjugations.html", {
                    "form": form,
                    "correctConj": correctConj,
                    "lang_id": lang_id,
                    "randTense": randTense,
                    "randSubj": randSubj,
                    "randVerb": randVerb
                })
                
        # Form is not valid
        else:
            # Return an error template on form submission
            return render(request, "conjugate/error.html", {
                "error": "Form",
                "message": "The form submission was not valid,"
            })
    # GET request
    else:
        # Check if tense IDs are valid integers
        try:
            tenseList = list(map(int, request.GET.getlist("tenses")))
        except:
            # Return tense ID error
            return render(request, "conjugate/error.html", {
                "error": "Tense ID",
                "message": "The tense IDs were not valid integers,"
            })

        # Check if tense IDs exist
        if not tenseList:
            # Return tense ID error
            return render(request, "conjugate/error.html", {
                "error": "Tense ID",
                "message": "No tense IDs were provided,"
            })

        # Check if tense IDs match for the language
        # Obtain tenses for the language
        validTenses = Tense.objects.filter(lang_id=lang_id).values()
        validTensesLen = len(validTenses)

        minTenseID = validTenses[0]["id"]
        maxTenseID = validTenses[validTensesLen - 1]["id"]

        for x in tenseList:
            if x < minTenseID or x > maxTenseID:
                # Return tense ID error
                return render(request, "conjugate/error.html", {
                    "error": "Tense ID",
                    "message": "Tense IDs do not match up with the chosen language,"
                })
            
        # Obtain subjects for the language
        subjectList = Subject.objects.filter(lang_id=lang_id).values()

        # Select a random subject
        randSubjPos = randint(0, len(subjectList) - 1)
        randSubj = subjectList[randSubjPos]["subject"]
        randSubjID = subjectList[randSubjPos]["id"]
        
        # Select a random tense from tenses chosen
        randTenseID = choice(tenseList)
        randTense = Tense.objects.get(id=randTenseID)

        # Select a random verb
        verbList = Verb.objects.filter(lang_id=lang_id).values()
        randVerbPos = randint(0, len(verbList) - 1)
        randVerb = verbList[randVerbPos]["verb"]
        randVerbID = verbList[randVerbPos]["id"]

        # Correct conjugation for subject and tense
        correctConj = Conjugation.objects.get(
            lang_id=lang_id, tense_id=randTenseID, subject_id=randSubjID, verb_id=randVerbID)

        # Create conjugation form and maintain chose tense IDs
        form = ConjugationForm(initial={'tenseIDs': tenseList, 'randTense': randTense,
            'randSubj': randSubj, 'randVerb': randVerb, 'correctConj': correctConj}, auto_id=False)

        # Obtain language
        language = Language.objects.get(pk=lang_id)

        return render(request, "conjugate/conjugations.html", {
            "form": form,
            "language": language,
            "correctConj": correctConj,
            "lang_id": lang_id,
            "randTense": randTense,
            "randSubj": randSubj,
            "randVerb": randVerb
        })
