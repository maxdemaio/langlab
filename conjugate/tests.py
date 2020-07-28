from django.test import TestCase

from .models import Conjugation, Language, Subject, Tense, Verb

# Create your tests here.
class ConjugateTestCase(TestCase):

    def setUp(self):

        # 1) English: Create language, verb, tense, subject, conjugation
        ourLanguage = Language.objects.create(id=1, lang="English")
        ourVerb = Verb.objects.create(id=1, lang_id=1, verb="do")
        ourTense = Tense.objects.create(id=1, lang_id=1, tense="Present Simple")
        ourSubject = Subject.objects.create(id=1, lang_id=1, subject="He/She/It")
        ourConjugation = Conjugation.objects.create(id=1, lang_id=1, verb_id=1, tense_id=1,
                                     subject_id=1, conj="does")
        
        # 2) French: Create language, verb, tense, subject, conjugation
        ourLanguage = Language.objects.create(id=2, lang="French")
        ourVerb = Verb.objects.create(id=2, lang_id=2, verb="manger")
        ourTense = Tense.objects.create(id=2, lang_id=2, tense="Le Présent")
        ourSubject = Subject.objects.create(id=2, lang_id=2, subject="Je")
        ourConjugation = Conjugation.objects.create(id=2, lang_id=2, verb_id=2, tense_id=2,
                                                    subject_id=2, conj="mange")

    def test_language_count(self):
        languages = Language.objects.all()
        self.assertEqual(languages.count(), 2)
