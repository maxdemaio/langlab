# Import Language model
import csv, os
from conjugate.models import Conjugation, Language, Subject, Tense, Verb

# Setup language table
def en_language_import():
    l = Language(lang="English")
    l.save()

# Import verbs into verb table
def en_verb_import():
    print("Inserting verbs")
    with open("conjugate/en_data/en_verbs.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            v = Verb(lang_id=int(row["lang_id"]), verb=row["verb"])
            v.save()
            print(row['lang_id'], row['verb'], "Saved")

# Import tenses into tense table
def en_tense_import():
    print("Inserting tenses")
    with open("conjugate/en_data/en_tenses.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            t = Tense(lang_id=int(row["lang_id"]), tense=row["tense"])
            t.save()
            print(row['lang_id'], row['tense'], "Saved")

# Import subjects into subject table
def en_subject_import():
    print("Inserting subjects")
    with open("conjugate/en_data/en_subj.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            s = Subject(lang_id=int(row["lang_id"]), subject=row["subject"])
            s.save()
            print(int(row["lang_id"]), row["subject"], "Saved")

# Import conjugations into conj table
def en_conj_import():
    print("Inserting conjugations")
    with open("conjugate/en_data/en_conj.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c = Conjugation(lang_id=int(row["lang_id"]), verb_id=int(row["verb_id"]), tense_id=int(row["tense_id"]),
                      subject_id=int(row["subject_id"]), conj=row["conj"])
            c.save()
            print(int(row["lang_id"]), row["verb_id"], row["tense_id"],
                  row["subject_id"], row["conj"], "Saved")

# Insert all English data to tables in one go
def lang_import_all():
    en_language_import()
    en_verb_import()
    en_tense_import()
    en_subject_import()
    en_conj_import()
