# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:32:07 2021

@author: kater
"""

#os.chdir("C:/Users/kater/Dropbox/PhD/Frictionless Data Fellowship")

from frictionless import describe

resource = describe("correlational_fordatapackage.csv", infer_missing_values=["", "NA"])

from frictionless import describe_schema

schema = describe_schema("correlational_fordatapackage.csv")


schema.get_field("participant").title = "participant code"
schema.get_field("age(1st session)").title = "age"
schema.get_field("PPVT_raw").title = "PPVT raw scores"
schema.get_field("PPVT_raw").description ="Peabody Pictured Vocabulary Test raw scores"
schema.get_field("age(1st session)").description = "participants' age (in months) in the first session"
schema.get_field("PPVT_z").title = "PPVT z-scores"
schema.get_field("PPVT_z").description = "Peabody Pictured Vocabulary Test z-scores"
schema.get_field("RCPM_raw").title = "RCPM raw scores"
schema.get_field("RCPM_raw").description = "Raven's Colored Progressive Matrices raw scores. RCPM measures non-verbal intelligence. "
schema.get_field("RCPM_z").title = "RCPM z scores"
schema.get_field("RCPM_z").description = "Raven's Colored Progressive Matrices z-scores."
schema.get_field("Srep_structure_correct/32").title = "sentence repetition"
schema.get_field("Srep_structure_correct/32").description = "The Sentence Repetition task, scored according to structure correct, is comprised of 32 sentences of varying syntactic complexity."
schema.get_field("morph_prod/24").title = "morphosyntax production"
schema.get_field("morph_prod/24").description = "The morphosyntax production task is a subtest of the Developmental Verbal IQ test (Tsimpli & Stavrakaki 2001). It contains  24 items."
schema.get_field("morph_comp/31").title = "morphosyntax comprehension"
schema.get_field("morph_comp/31").description = "The morphosyntax comprehension task is a subtest of the Developmental Verbal IQ test (Tsimpli & Stavrakaki 2001). It contains 31 items."
schema.get_field("syll_manip/12").title = "syllable manipulation"
schema.get_field("syll_manip/12").description = "Syllable manipulation is a composite score, taken from the three syllable manipulation subtests of the Metaphon test, measuring phonological awareness. It is scored out of 12."
schema.get_field("phon_manip/8").title = "phoneme manipulation"
schema.get_field("phon_manip/8").description = "Phoneme manipulation is a composite score, taken from two phoneme manipulation subtests of the Metaphon test, measuring phonological awareness. It is scored out of 8. "
schema.get_field("pseudoword_rep/48").title = "pseudoword repetition"
schema.get_field("pseudoword_rep/48").description = "Repetition of pseudowords: score out of 48\n(phonological working memory)"
schema.get_field("fwd_recall/54").title = "forward digit recall"
schema.get_field("fwd_recall/54").description = "Forward digit recall: score out of 54\n(verbal working memory)"
schema.get_field("fwd_recall_range/9").title = "forward digit recall range"
schema.get_field("fwd_recall_range/9").description = "the range of the recall, out of possible 9"
schema.get_field("bwd_recall/45").title = "backward digit recall"
schema.get_field("bwd_recall/45").description = "Backward digit recall: score out of 45"
schema.get_field("bwd_recall_range/9").title = "backward digit recall range"
schema.get_field("bwd_recall_range/9").description = "backward digit recall range, out of possible 9"
schema.get_field("fwd_corsi/54").title = "Corsi task forward"
schema.get_field("fwd_corsi/54").description = "Visuospatial WM (Corsi task) forward recall: score out of 54"
schema.get_field("fwd_corsi_range/9").title = "Corsi task forward range"
schema.get_field("fwd_corsi_range/9").description = "The range of the recall, out of possible 9"
schema.get_field("bwd_corsi/45").title = "Corsi task backward"
schema.get_field("bwd_corsi/45").description = "the range of the recall, out of possible 9"
schema.get_field("bwd_corsi_range/9").title = "Corsi task backward range"
schema.get_field("bwd_corsi_range/9").description = "the range of the recall, out of possible 9"
schema.get_field("melody_score").title = "melody score"
schema.get_field("melody_score").description = "Score of the melody subtest of the MBEMA (Peretz et al. 2013) - out of 20."
schema.get_field("rhythm_score").title = "rhythm score"
schema.get_field("rhythm_score").description = "Score of the rhythm subtest of the MBEMA (Peretz et al. 2013) - out of 20."
schema.get_field("cBAT_score").title = "cBAT score"
schema.get_field("cBAT_score").description = "Overall percentage of the complex Beat Alignment Test (Einarson 2016)"
schema.get_field("complex_cBAT").title = "complex cBAT"
schema.get_field("complex_cBAT").title = "Percentage for the complex rhythm items of the cBAT"
schema.get_field("simple_cBAT").title = "simple cBAT"
schema.get_field("simple_cBAT").title = "Percentage for the simple rhythm items of the cBAT"
schema.get_field("chat_d'").title = "auditory attention d'"
schema.get_field("chat_d'").description = "d' for the auditory attention task chat-y-es-tu"
schema.get_field("trackgridprop").title = "visual attention raw"
schema.get_field("trackgridprop").description = "visual attention proportion of correct responses"
schema.get_field("trackgridprop_z").title = "visual attention z-scores"
schema.get_field("trackgridprop_z").description = "visual attention z-scores of correct responses"
schema.get_field("trackrecallprop").title = "visual recall shape proportion"
schema.get_field("trackrecallprop").description = "proportion of correct responses for the recall of shapes"
schema.get_field("trackrecallprop_z").title = "visual recall shape z-scores"
schema.get_field("trackrecallprop_z").description = "z-scores of correct responses for the recall of shapes"

from frictionless import Field 

schema.add_field(Field(name="keywords", type="string")) # = ("preschoolers","language comprehension","phonological awareness", "working memory","music skills","rhythm perception")
schema.get_field("keywords")














schema.to_yaml("tmp/correlational.schema-simple.yaml")


#resource.schema.get_field("fwd_corsi/54").type = "integer"
#resource.to_yaml("tmp/correlational_fordatapackage.resource.yaml")


#from frictionless import describe_schema
#
#schema = describe_schema("correlational_fordatapackage.csv")
#
#print(schema)



#! frictionless extract 16-11-20_correlational_fordatapackage.csv

#! frictionless validate 16-11-20_correlational_fordatapackage.csv

