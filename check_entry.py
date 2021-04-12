#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Katarina
'''

import re
REGULAR_VERBS = ['lop', 'loop', 'eet', 'et', 'luister', 'vind', 'houd', 'tank', 'moet', 'wil', 'blaf', 'brei','haak', 'hak', 'vis', 'schrijf', 'schrijv', 'slaap',  'slapen']
IRREGULAR_VERBS = ['']
VERBS_1S = ['loop', 'sta', 'zit', 'lig', 'eet', 'luister', 'vind', 'houd', 'tank', 'wil', 'moet', 'blaf', 'brei', 'haak', 'vis', 'schrijf', 'slaap', 'ga', 'doe', 'begin', 'heb', 'ben', 'zie', 'kook', 'maak', 'geef', 'kan', 'weet', 'rijd', 'laat', 'adem', 'vang', 'geef', 'stuur']
VERBS_3S = ['loopt', 'staat', 'zit', 'ligt', 'eet', 'luistert', 'vindt','houdt', 'tankt', 'wil', 'moet', 'blaft', 'breit', 'haakt', 'vist', 'schrijft', 'slaapt', 'gaat', 'doet', 'begint', 'heeft', 'is','ziet','kookt','maakt','geeft','kunt', 'fietst', 'rijdt', 'laat', 'ademt', 'vangt', 'geeft', 'stuurt']
VERBS_FULL = ['lopen', 'staan', 'zitten', 'liggen', 'eten', 'luisteren', 'vinden','houden', 'tanken', 'willen', 'moeten', 'blaffen', 'breien', 'haken', 'vissen', 'schrijven', 'slapen', 'gaan', 'doen', 'beginnen', 'hebben', 'zijn','zien','koken','maken','geven', 'kunnen', 'rijden', 'laten', 'ademen', 'vangen', 'geven', 'sturen']
VERBS_PAST = ['liep', 'liepen', 'stond', 'stonden', 'zat', 'zaten', 'lag', 'lagen', 'at', 'aten', 'luisterde', 'luisterden', 'vond', 'vonden', 'hield', 'hielden', 'tankte', 'tankten', 'wilde', 'wilden', 'wou', 'wouden', 'moest', 'moesten', 'blafte', 'blaften', 'breide', 'breiden', 'haakte', 'haakten', 'viste', 'visten', 'schreef', 'schreven', 'sliep', 'sliepen', 'ging', 'gingen', 'deed', 'deden', 'begon', 'begonnen', 'had', 'hadden', 'was', 'waren', 'zag', 'zagen', 'kookte', 'kookten', 'maakte', 'maakten', 'gaf', 'gaven', 'kon', 'konden', 'reden', 'reed', 'liet', 'lieten', 'ademde', 'ademden', 'ving', 'vingen', 'gaf', 'gaven']
WRONG_VD = {'geloopt':'gelopen', 'geeet':'gegeten', 'gegeet':'gegeten', 'geloop':'gelopen', 'gevind':'gevonden', 'gevond':'gevonden', 'geluister':'geluisterd', 'geluistert':'geluisterd','gegat':'gegeten', 'gegaten':'gegeten', 'geblafd':'geblaft', 'gebrei':'gebreid','gebreit':'gebreid', 'geschrijf':'geschreven', 'geschreef':'geschreven', 'geschreeft':'geschreven', 'geschreefd':'geschreven', 'geschrijft':'geschreven', 'geslaap':'geslapen', 'geslaapt':'geslapen', 'gesliep':'geslapen', 'gesliepen':'geslapen', 'gehaken':'gehaakt', 'geschriven':'geschreven', 'gegeef':'gegeven', 'gegeeft':'gegeven'}
DE_WORDS = ['straat', 'vriend', 'vriendin', 'wei', 'graat', 'muziek', 'popmuziek', 'groep', 'vriendengroep', 'vork', 'boter', 'roomboter', 'band', 'autoband', 'stoep', 'stad', 'hond', 'mevrouw', 'meneer', 'klasgenoot', 'trui', 'kraag', 'zalm', 'hengel', 'auto ', 'brief', 'tante', 'tafel', 'pen', 'kat', 'lijn','kamer', 'fiets', 'huid']
HET_WORDS = ['paard', 'gras', 'vriendje', 'vriendinnetje', 'mes', 'brood', 'volkorenbrood', 'pompstation', 'station', 'geld', 'aas', 'bed', 'kind', 'potlood', 'bureau', 'varken', 'vlees', 'kussen', 'laken', 'dier', 'bot']
PLURALS = ['kieuwen', 'schubben', 'straten', 'vrienden', 'vriendinnen', 'weides', 'graten', 'groepen', 'vriendengroepen', 'vorken', 'banden', 'autobanden', 'stoepen','steden', 'honden', 'mevrouwen','meneren', 'klasgenoten', 'truien','kragen', 'zalmen', 'hengels','auto\'s', 'brieven', 'autoos','autos', 'tantes', 'tafels','pennen', 'paarden', 'vriendjes','vriendinnetjes', 'messen', 'broden','pompstations', 'stations', 'azen','bedden', 'kinderen', 'potloden','bureaus', 'katten', 'varkens', 'kussens', 'lakens', 'kamers', 'fietsen', 'dier']
PRONOUNS = ['ik', 'jij', 'hij', 'zij', 'wij', 'mij', 'ons']
ADVERBS = ['daarna', 'daarom', 'gisteren', 'vandaag', 'toen', 'erna', 'erom', 'morgen', 'graag', 'misschien', 'waarschijnlijk', 'thuis', 'vaak', 'morgen']
WRONG_PLURALS = {'straats':'straten', 'vriends':'vrienden', 'vriendins':'vriendinnen', 'weis':'weides', 'weien':'weides', 'graats':'graten', 'groeps':'groepen', 'vorks':'vorken', 'bands':'banden', 'autobands':'autobanden', 'autoen':'auto\'s', 'autoos':'auto\'s', 'auton':'auto\'s', 'stoeps':'stoepen', 'staden':'steden', 'stads':'steden', 'honds':'honden', 'mevrouws':'mevrouwen', 'klasgenoots':'klasgenoten', 'truis':'truien', 'kraags':'kragen', 'kinds':'kinderen', 'kinden':'kinderen', 'zalms':'zalmen', 'hengelen':'hengels', 'briefen':'brieven', 'briefs':'brieven', 'tanten':'tantes', 'tante\'s':'tantes', 'paards':'paarden', 'vriendjen':'vriendjes', 'mess':'messen', 'broods':'broden', 'brooden':'broden', 'stationen':'stations', 'stationnen':'stations', 'beds':'bedden', 'beden':'bedden'}

def word_not_present_feedback(feedback, translation, word):
    feedback = feedback + f"Het lijkt erop dat je het woord \'{word}\' niet hebt gebruikt.\n"
    translation = translation + f"It seems that you did not use the word \'{word}\'.\n"
    return(feedback, translation)

def check_if_words_are_present(feedback, translation, words, entry):
    for word in words:
        if re.search(word, entry) is None: #first check if the word is in the entry; if it is not there, control for words that change when conjugated
            if word == 'lopen':
                if re.search('(loo?p|liep)', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'straat':
                if re.search('straa?t', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'graat':
                if re.search('graten', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'luisteren':
                if re.search('luister', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'eten':
                if re.search('(eet| at)', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'brood':
                if re.search('broden', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'tanken':
                if re.search('tank', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'blaffen':
                if re.search('blaf', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'breien':
                if re.search('brei', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'kraag':
                if re.search('kragen', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'haken':
                if re.search('haak', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'nodig hebben':
                if re.search('nodig', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'schrijven':
                if re.search('(schrijf|schreven|schreef)', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'brief':
                if re.search('brieven', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            elif word == 'slapen':
                if re.search('(slaap|sliep)', entry) is None:
                    feedback, translation = word_not_present_feedback(feedback, translation, word)
            else:
                feedback, translation = word_not_present_feedback(feedback, translation, word)
    return(feedback, translation)

def de_should_be_het_feedback(feedback, translation, word):
    feedback = feedback + f"\'{word}\' is een het-woord.\n"
    translation = translation + f"\'{word}\' goes with the article \'het\'.\n"
    return(feedback, translation)

def het_should_be_de_feedback(feedback, translation, word):
    feedback = feedback + f"\'{word}\' is een de-woord.\n"
    translation = translation + f"\'{word}\' goes with the article \'de\'.\n"
    return(feedback, translation)

def plural_gets_de_feedback(feedback, translation, word):
    feedback = feedback + f'{word} is meervoud, dus het krijgt het lidwoord \'de\'.\n'
    translation = translation + f'{word} is a plural, so it goes with the article \'de\'.\n'
    return(feedback, translation)

def check_articles(feedback, translation, entry):
    if re.search('(de|het|een|mijn|jouw|zijn|die|dat|deze|dit)', entry) is None:
        feedback = feedback + "Waarschuwing: het lijkt erop dat je helemaal geen lidwoorden hebt gebruikt. Kijk goed of je ergens een lidwoord bent vergeten.\n"
        translation = translation + "Warning: it seems you have not used any articles at all. Look if you have not forgotten any articles!\n"
    for word in DE_WORDS:
        if re.search(f'(het|dit|dat)( \w)? {word}', entry) is not None:
            feedback, translation = het_should_be_de_feedback(feedback, translation, word)

    for word in HET_WORDS:
        if re.search(f'(die|deze|de)( \w)? {word}($|\W)', entry) is not None:
            feedback, translation = de_should_be_het_feedback(feedback, translation, word)

    for word in PLURALS:
        if re.search(f'(het|dit|dat)( \w)? {word}', entry) is not None:
            feedback, translation = plural_gets_de_feedback(feedback, translation, word)

    #if re.search('(het|dit|dat)( \w)? \w*en', entry) is not None:
    #    feedback = feedback + "Woorden in het meervoud krijgen altijd het lidwoord \'de\'.\n"
    #    translation = translation + "Plurals always get the article \'de\'.\n"

    return(feedback, translation)

def check_prepositions(feedback, translation, entry):
    if re.search('op de straat', entry) is not None:
        feedback = feedback + "\'op de straat\' is niet echt fout, maar dan gaat het over een specifieke straat. Als je gewoon op straat loopt zeg je \'op straat\'.\n"
        translation = translation + "\'op de straat\' is not exactly wrong, but we only say it when talking about a specific street. When you are just walking on the street we say \'op straat\'.\n"
    if re.search('op .* wei', entry) is not None:
        feedback = feedback + "We zeggen \'in de wei\'.\n"
        translation = translation + "It should be \'in de wei\'.\n"
    if re.search('luister.*muziek', entry) is not None:
        if re.search('naar', entry) is None:
            feedback = feedback + "Je luistert altijd NAAR iets, dus: \'luisteren naar muziek\'.\n"
            translation = translation + "We always say \'luisteren NAAR iets\': so: \'luisteren naar muziek\'.\n"
    if re.search('(in|op|aan)( het| de)?( \w)? tank ?station', entry) is not None:
        feedback = feedback + "In het Nederlands tank je BIJ het tankstation.\n"
        translation = translation + "We say \'tanken BIJ het tankstation\'.\n"
    return(feedback, translation)

def check_verbs(feedback, translation, entry):
    if re.search('ik \w*', entry) is not None:
        verb = re.search('ik (\w*)', entry)
        verb = verb.group(1)
        if verb in VERBS_3S:
            if not verb in VERBS_1S:
                feedback = feedback + "Werkwoorden in de eerste persoon zijn gelijk aan de stam van het werkwoord (infinitief minus \'-en\'). Dus: \'ik loop\', niet \'ik lopen\'.\n"
                translation = translation + "Verbs in the first person are equal to the stem of the verb (infinitive minus \'-en\'). So: \'ik loop\', not \'ik lopen\'.\n"

    for verb in VERBS_1S:
        if re.search('ik', entry) is None and not re.search(f'{verb}($|\W)', entry) is None:
            if re.search(f'{verb} (je|jij)', entry) is None:
                feedback = feedback + f"De vorm \'{verb}\' word alleen gebruikt voor de ik-vorm en je=jij na het werkwoord.\n"
                translation = translation + f'The form \'{verb}\' is only used for the first person singular and the second person singular when the pronoun comes after the verb.\n'
    for verb in VERBS_3S:
        if re.search(f'(\w*en|wij|jullie) {verb}', entry) is not None:
            feedback = feedback + "Werkwoorden eindigen in het meervoud altijd op een -n.\n"
            translation = translation + "Plural verbs always end with -n.\n"

    for verb in VERBS_FULL:
        all_singulars = DE_WORDS + HET_WORDS
        for word in all_singulars:
            if re.search(f'(^|\.\?!).?.?.?.?.?{word} {verb}', entry) is not None:
                feedback = feedback + "Werkwoorden in de derde persoon enkelvoud zijn stam+t.\n"
                translation = translation + "Verbs in the third person singular are formed by adding a -t to the verb stem.\n"

    if re.search('vriend loop ', entry) is not None:
        feedback = feedback + "Werkwoorden in de derde persoon eindigen op een -t. Dus: \'mijn vriend loopt\', niet \'mijn vriend loop\'.\n"
        translation = translation + "Verbs end with -t in the third person. So: \'mijn vriend loopt\', not \'mijn vriend loop\'.\n"
    if re.search('ik lop ', entry) is not None:
        feedback = feedback + "Werkwoorden in de eerste persoon worden gemaakt door de infinitief te nemen minus \'-en\', maar soms moet je een letter toevoegen voor de uitspraak. Daarom is het \'ik loop\', en niet '\ik lop\'.\n"
        translation = translation + "First person verbs are created by taking the infinitive minus \'-en\', but sometimes you have to add a letter for the pronunciation. That is why we write \'ik loop\', and not \ 'ik lop\'.\n"
    if re.search('ik lopen', entry) is not None:
        feedback = feedback + "Werkwoorden in de eerste persoon zijn gelijk aan de stam van het werkwoord (infinitief minus \'-en\'). Dus: \'ik loop\', niet \'ik lopen\'.\n"
        translation = translation + "Verbs in the first person are equal to the stem of the verb (infinitive minus \'-en\'). So: \'ik loop\', not \'ik lopen\'.\n"
    if re.search('loo?pte', entry) is not None:
        feedback = feedback + "\'lopen\' is een sterk werkwoord, dat wil zeggen dat het een onregelmatige verleden tijd heeft. Het is dus \'ik liep, wij liepen\'. Het woord \'loopte\' bestaat niet.\n"
        translation = translation + "\'lopen\' is a so called strong verb, meaning that it has irregular past tense forms. So we say \'ik liep, wij liepen\' (\'I walked, we walked\'). The word \'loopte\' does not exist.\n"
    if re.search('(\ws|\wen) loop( |t)', entry) is not None:
        feedback = feedback + "Het lijkt erop dat je het werkwoord \'lopen\' in het enkelvoud hebt gebruikt waar het meervoud had moeten zijn.\n"
        translation = translation + "It seems that you have used the verb \'lopen\' (to walk) in the singular where it should have been the plural.\n"
    if re.search('paarden staat', entry) is not None:
        feedback = feedback + "Het meervoud van \'staat\' is \'staan\'. Dus: \'De paarden staan\'.\n"
        translation = translation + "The plural of \'staat\' is \'staan\'. So: \'De paarden staan\'.\n"
    if re.search('paarden is', entry) is not None:
        feedback = feedback + "Het meervoud van \'is\' is \'zijn\'. Dus: \'De paarden zijn\'.\n"
        translation = translation + "The plural of \'is\' is \'zijn\'. So: \'De paarden zijn\'.\n"
    if re.search('paard staan', entry) is not None:
        feedback = feedback + "Het enkelvoud van \'staan\' is \'staat\'. Dus: \'Het paard staat\'.\n"
        translation = translation + "The singular of \'staan\' is \'staat\'. So: \'Het paard staat\'.\n"
    if re.search('paard is', entry) is not None:
        feedback = feedback + "Het enkelvoud van \'zijn\' is \'is\'. Dus: \'Het paard is\'.\n"
        translation = translation + "The singular of \'zijn\' is \'is\'. So: \'Het paard is\'.\n"
    if re.search('vis hebben',  entry) is not None:
        feedback = feedback + "\'Vis\' is enkelvoud. Het moet dus zijn \'de vis heeft\'."
        translation = translation + "\'Vis\' is singular, so it should be \'de vis heeft\'"
    if re.search('groep luisteren', entry) is not None:
        feedback = feedback + "\'groep\' is enkelvoud. Het moet dus zijn \'de (vrienden-)groep luistert\'\n."
        translation = translation + "\'groep\' is singular. So it should be \'de (vrienden-)groep luistert\'.\n"
    if re.search('(\ws|\wen) luister(t| )', entry) is not None:
        feedback = feedback + "Het lijkt erop dat je het werkwoord \'luisteren\' in het enkelvoud hebt gebruikt waar het meervoud had moeten zijn.\n"
        translation = translation + "It seems that you have used the verb \'luisteren\' (to listen) in the singular where it should have been the plural.\n"
    if re.search('\wen is ', entry) is not None or re.search('\ws is ', entry) is not None:
        feedback = feedback + "Het lijkt erop dat je het werkwoord \'zijn\' in het enkelvoud hebt gebruikt waar het meervoud had moeten zijn.\n"
        translation = translation + "It seems that you have used the verb \'zijn\' (to be) in the singular where it should have been the plural.\n"
    if re.search(' ik \w(t|en)', entry) is not None and re.search('( eet| weet|)', entry) is None:
        feedback = feedback + "Werkwoorden in de eerste persoon zijn gelijk aan de stam van het werkwoord (infinitief minus \'-en\'). Dus: \'ik loop\'.\n"
        translation = translation + "Verbs in the first person are equal to the stem of the verb (infinitive minus \'-en\'). So: \'ik loop\'.\n"
    if re.search('(ik|hij|jij|je) eten', entry) is not None:
        feedback = feedback + "Het lijkt erop dat je het werkwoord \'eten\' in het meervoud hebt gebruikt waar het enkelvoud had moeten zijn.\n"
        translation = translation + "It seems that you have used the verb \'eten\' (to eat) in the plural where it should have been the singular.\n"
    if re.search('(wij|jullie|\wen|\ws) eet', entry) is not None:
        feedback = feedback + "Het lijkt erop dat je het werkwoord \'eten\' in het enkelvoud hebt gebruikt waar het meervoud had moeten zijn.\n"
        translation = translation + "It seems that you have used the verb \'eten\' (to eat) in the singular where it should have been the plural.\n"
    if re.search('\wt j(e|ij) ', entry) is not None and re.search('( eet| weet)', entry) is not None:
        feedback = feedback + "Als \'je\' of \'jij\' na het werkwoord komt, is het werkwoord gelijk aan de ik-vorm. Dus: \'jij loopt\', maar \'loop jij?\'.\n"
        translation = translation + "When \'je\' or \'jij\' comes after the verb the verb equals the 1st person singular. So: \'jij loopt\', but: \'loop jij?\'.\n"
    words = re.split('\W', entry)
    for word in words:
        if word in WRONG_VD:
            correct_form = WRONG_VD[word]
            feedback_string = f'De correcte vorm van het voltooid deelwoord is \'ik heb {correct_form}\'. \'{word}\' is geen bestaand woord.\n'
            translation_string = f'The correct form of the past participle is \'ik heb {correct_form}\'. The form \'{word}\' does not exist.\n'
            feedback = feedback + feedback_string
    return(feedback, translation)

def check_word_order(feedback, translation, entry):
    if re.search('dat ', entry) is None:
        if re.search('geld.*nodig', entry) is not None:
            feedback = feedback + "We zeggen niet \'ik heb nodig geld\', maar \'ik heb geld nodig\'."
            translation = translation + "We don\'t say \'ik heb nodig geld\', maar \'ik heb geld nodig\'.\n"
        if re.search('(heb|heeft).* geld.* vaak', entry) is not None:
            feedback = feedback + "Het bijwoord \'vaak\' komt direct na de persoonsvorm. Dus: \'ik heb vaak geld nodig\'.\n"
            translation = translation + "The adverb \'vaak\' comes directly after the conjugated verb. So: \'ik heb vaak geld nodig\'.\n"
    if re.search ('brie[fv].*tante', entry) is not None and re.search(' aan ', entry) is None:
        feedback = feedback + "Het indirect object komt na het object als je \'aan\' gebruikt, anders komt het ervoor. Dus: \'ik schrijf mijn tante een brief\' OF \'ik schrijf een brief aan mijn tante\'.\n"
        translation = translation + "The indirect object comes after the object when you use \'aan\' (\'to\'), in all other cases it comes before the object. So: \'ik schrijf mijn tante een brief\' OR \'ik schrijf een brief aan mijn tante\' (\'I write a letter to my aunt\').\n"

    sentences = re.split('(\.|\n)', entry)
    for sentence in sentences:
        words = re.split('\W', sentence)
        nouns_adverbs_pronouns = DE_WORDS + HET_WORDS + ADVERBS + PLURALS + PRONOUNS
        verbs = VERBS_1S + VERBS_3S + VERBS_FULL + VERBS_PAST
        verb_count = 0
        i_first_verb = 0
        for i, word in enumerate(words):
            if word in verbs:
                if verb_count == 0:
                    i_first_verb = i
                    verb_count += 1
                    if i > 0:
                        left_constituents = 0 #count the amount of nouns/adverbs that appear left of the verb
                        for left_word in words[0:i]:
                            if left_word in nouns_adverbs_pronouns:
                                left_constituents += 1
                            elif left_word == 'en':
                                left_constituents -= 1
                        if left_constituents > 1:
                            feedback = feedback + "Er komt altijd maar één constituent voor de persoonsvorm. Dus:\n\'Gisteren liep ik naar huis\'\nniet\n\'gisteren ik liep naar huis\'.\n"
                            translation = translation + "We can only put one constituent before the conjugated verb. So:\n\'Gisteren liep ik naar huis\'\nnot\n\'Gisteren ik liep naar huis\'.\n"
                    else:
                        if re.search('\?', entry) is None:
                            feedback = feedback + "In hoofdzinnen komt de persoonsvorm altijd op de tweede plek van de zin, behalve in een vraagzin. Het lijkt erop dat je ergens de persoonsvorm aan het begin hebt geplaatst.\n"
                            translation = translation + "Main clauses always have the conjugated verb in second place, except for questions. It seems like you somewhere put the conjugated verb first.\n"
                elif verb_count == 1: #het tweede werkwoord in de zin komt niet direct na het eerste werkwoord, tenzij er verder niks in de zin staat
                    if i - i_first_verb == 1: #dus als dit werkwoord en het eerste elkaar opvolgen
                        if len(words) - i > 1:
                            feedback = feedback + "De persoonsvorm komt op de tweede plek van de zin, maar de rest van de werkwoorden komt achteraan, na het lijdend voorwerp. Dus:\n\'Ik wil een appel eten\'\nNiet:\n\'Ik wil eten een appel\'.\n"
                            translation = translation + "The conjugated verb comes at the second place of the sentence, but the other verbs come at the end, afer the object. So:\n\'Ik wil een appel eten\' (\'I want to eat an apple\')\nNiet:\n\'Ik wil eten een appel\'.\n"

    return(feedback, translation)

def check_miscellaneous(feedback, translation, entry):
    if re.search('jou (straat|vriend|paard|wei|vriendengroep|brood|hond|autoband|klasgenoot|geld|hengel|tante|bed)', entry) is not None:
        feedback = feedback + "Om bezit aan te geven, gebruiken we \'jouw\', en niet \'jou\'. Bijvoorbeeld \'jouw fiets\', \'jouw vriend\', \'jouw klasgenoot\'.\n"
        translation = translation + "We express possession using the word \'jouw\', and not \'jou\'. For example \'jouw fiets\' (\'your bike\'), \'jouw vriend\' (\'your friend\'), \'jouw klasgenoot\' (\'your classmate\').\n"
    if re.search('mij (straat|vriend|paard|wei|vriendengroep|brood|hond|autoband|klasgenoot|geld|hengel|tante|bed)', entry) is not None:
        feedback = feedback + "Om bezit aan te geven, gebruiken we \'mijn\', en niet \'mij\'. Bijvoorbeeld \'mijn fiets\', \'mijn vriend\', \'mijn klasgenoot\'.\n"
        translation = translation + "We express possession using the word \'mijn\', and not \'mij\'. For example \'mijn fiets\' (\'my bike\'), \'mijn vriend\' (\'my friend\'), \'mijn klasgenoot\' (\'my classmate\').\n"
    if re.search('om (luister|lopen|eten|tanken|blaffen|breien|haken|hebben|zijn|staan|vissen|schrijven|slapen)', entry) is not None:
        feedback = feedback + "Tussen \'om\' en een werkwoord komt altijd \'te\'.\n"
        translation = translation + "Between \'om\' and a verb we always put \'te\'.\n"
    if re.search('(is|zijn) lekkere', entry) is not None:
        feedback = feedback + "Als je een bijvoeglijk naamwoord (zoals \'lekker\') gebruikt met een koppelwerkwoord (zoals in \'het is lekker\'), gebruik je de vorm zonder -e.\n"
        translation = translation + "When you use an adjective (like \'lekker\') with a copula (as in \'het is lekker\'), you us the form without -e.\n"
    if re.search('[^(mijn|zijn|haar|jouw|je|ons|onze|hun)] eigen( \w)? bed', entry) is not None:
        feedback = feedback + "Voor \'eigen\' komt altijd het bezittelijk voornaamwoord. Dus: \'mijn eigen bed\', \'jouw eigen fiets\', \'ons eigen mooie huis\'.\n"
        translation = translation + "We always put a possessive pronoun before \'eigen\'. So: \'mijn eigen bed\' (\'my own bed\'), \'jouw eigen fiets\' (\'your own bike\'), \'ons eigen mooie huis\' (\'our own beautiful house\').\n"
    if re.search(' is [a-z]+e ', entry) is not None:
        feedback = feedback + "Als je een bijvoeglijk naamwoord gebruikt na een koppelwerkwoord krijgt het nooit een -e op het einde. Dus:\n\'Het lekkere brood\'\nMAAR:\n\'Het brood is lekker\'.\n"
        translation = translation + "When you use an adjective after a copula it never ends in -e. So:\n\'Het lekkere brood\' - \'the tasty bread\'\nBUT:\n\'Het brood is lekker\' - \'the bread is tasty\'."
    for wrong_plural in WRONG_PLURALS:
        if re.search(f'{wrong_plural}($|\W)', entry) is not None:
            correct_form = WRONG_PLURALS[wrong_plural]
            feedback = feedback + f"De juiste meervoudsvorm is \'{correct_form}\', niet \'{wrong_plural}\'.\n"
            translation = translation + f"The correct plural form is \'{correct_form}\', not \'{wrong_plural}\'.\n"
    return(feedback, translation)

def check_other_errors(feedback, translation, entry):
    feedback, translation = check_articles(feedback, translation, entry)
    feedback, translation = check_prepositions(feedback, translation, entry)
    feedback, translation = check_verbs(feedback, translation, entry)
    feedback, translation = check_word_order(feedback, translation, entry)
    feedback, translation = check_miscellaneous(feedback, translation, entry)
    return(feedback, translation)

def get_feedback(entry, words):
    entry = entry.strip().lower()
    standard_feedback = f'Jouw entry was:\n{entry}\n\n'
    feedback = standard_feedback
    translation = f'Your entry was:\n{entry}\n\n'
    feedback, translation = check_if_words_are_present(feedback, translation, words, entry)
    feedback, translation = check_other_errors(feedback, translation, entry)
    if feedback == standard_feedback:
        feedback = feedback + "Het systeem heeft geen fouten in je tekst gevonden. Goed gedaan! Maar let op: dit betekent niet dat er geen fouten zijn. Het systeem ziet namelijk lang niet alles. Blijf dus ook zelf goed opletten."
        translation = translation + "The system has not found any mistakes in your text. Well done! But remember that this does not mean that there are no mistakes. Unfortunately, the system does not pick up on everything. So watch out!"
    else:
        feedback = feedback + "\nLet op! Er kunnen nog meer fouten in je tekst zitten. Het systeem ziet namelijk lang niet alles! Het kan ook dat het systeem een fout heeft gezien, terwijl die er eigenlijk niet was."
        translation = translation + "\nWatch out! There might be more errors in your text. The system sees far from everything! It is also possible that the system has spotted an error where there actually was none."
    return(feedback, translation)