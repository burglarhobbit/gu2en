import re

def replaceArray(a, b, text):
    if len(a) != len(b):
        return ""
    for i in range(len(a)):
        pat = re.compile(a[i])
        text = pat.sub(b[i], text)
    return text

def Transliterate(text):
    for i in range(len(guj_consonants)):
        for j in range(len(guj_diacritics)):
            pat = re.compile(guj_consonants[i] + guj_diacritics[j] + "ઃ ")
            replacer = eng_halant[i] + eng_diacritics[j] + "h" + eng_diacritics[j] + " "
            text = pat.sub(replacer, text)
    
    anusvara_regex = re.compile("ં")
    has_anusvara = anusvara_regex.search(text)
    if has_anusvara:
        for i in range(len(guj_consonants)):
            for j in range(len(guj_diacritics)):
                pat_m = re.compile(guj_consonants[i] + guj_diacritics[j] + "ં[મપબભ]")
                res = pat_m.search(text)
                if res:
                    pat_m = re.compile(guj_consonants[i] + guj_diacritics[j] + "ં")
                    replacer_m = eng_halant[i] + eng_diacritics[j] + "m"
                    text = pat_m.sub(replacer_m, text)
                else:
                    pat_n = re.compile(guj_consonants[i] + guj_diacritics[j] + "ં")
                    replacer_n = eng_halant[i] + eng_diacritics[j] + "n"
                    text = pat_n.sub(replacer_n, text)
        
        for i in range(len(guj_vowels)):
            pat_m = re.compile(guj_vowels[i] + "ં[મપબભ]")
            res = pat_m.search(text)
            if res:
                pat_m = re.compile(guj_vowels[i] + "ં")
                replacer_m = eng_vowels[i] + "m"
                text = pat_m.sub(replacer_m, text)
            else:
                pat_n = re.compile(guj_vowels[i] + "ં")
                replacer_n = eng_vowels[i] + "n"
                text = pat_n.sub(replacer_n, text)
        
        for i in range(len(guj_consonants)):
            pat_m = re.compile(guj_consonants[i] + "ં[મપબભ]")
            res = pat_m.search(text)
            if res:
                pat_m = re.compile(guj_consonants[i] + "ં")
                replacer_m = eng_consonants[i] + "m"
                text = pat_m.sub(replacer_m, text)
            else:
                pat_n = re.compile(guj_consonants[i] + "ં")
                replacer_n = eng_consonants[i] + "n"
                text = pat_n.sub(replacer_n, text)
    
    for i in range(len(guj_consonants)):
        for j in range(len(guj_diacritics)):
            pat = re.compile(guj_consonants[i] + guj_diacritics[j])
            replacer = eng_halant[i] + eng_diacritics[j]
            text = pat.sub(replacer, text)
    
    text = replaceArray(guj_halant, eng_halant, text)
    text = replaceArray(guj_diacritics, eng_diacritics, text)
    text = replaceArray(guj_vowels, eng_vowels, text)
    text = replaceArray(guj_consonants, eng_consonants, text)
    text = replaceArray(guj_digits, eng_digits, text)
    
    for i in range(len(eng_consonants)):
        pat = re.compile(eng_consonants[i] + " ")
        replacer = eng_halant[i] + " "
        text = pat.sub(replacer, text)
    
    for i in range(len(eng_halant)):
        for j in range(len(eng_consonants)):
            pat = re.compile(eng_halant[i] + eng_halant[j] + " ")
            replacer = eng_halant[i] + eng_consonants[j] + " "
            text = pat.sub(replacer, text)
    
    for i in range(len(eng_vowels)):
        for j in range(len(eng_comb)):
            pat = re.compile(eng_vowels[i] + eng_comb[j] + "a ")
            replacer = eng_vowels[i] + eng_comb[j] + " "
            text = pat.sub(replacer, text)
    
    for i in range(len(lowercase_alphabets)):
        p1 = re.compile(r'(\.|\?|!)\s' + lowercase_alphabets[i])
        p2 = re.compile(r',\s("|“)' + lowercase_alphabets[i])
        p3 = re.compile(r'(\."|\.”)\s' + lowercase_alphabets[i])
        p4 = re.compile(r'(\.|\?|!)\s("|“)' + lowercase_alphabets[i])
        p5 = re.compile(r'(\?”+\?”|!”|!")\s' + lowercase_alphabets[i])
        p6 = re.compile(r'("|”)\s("|“)' + lowercase_alphabets[i])
        p7 = re.compile(r'^' + lowercase_alphabets[i])
        p8 = re.compile(r'\n' + lowercase_alphabets[i])
        text = p1.sub(r'\1 '+uppercase_alphabets[i], text)
        text = p2.sub(r', \1'+uppercase_alphabets[i], text)
        text = p3.sub(r'\1 '+uppercase_alphabets[i], text)
        text = p4.sub(r'\1 \2'+uppercase_alphabets[i], text)
        text = p5.sub(r'\1 '+uppercase_alphabets[i], text)
        text = p6.sub(r'\1 \2'+uppercase_alphabets[i], text)
        text = p7.sub(uppercase_alphabets[i], text)
        text = p8.sub(r'\n'+uppercase_alphabets[i], text)
    
    text = text.replace("yvar ", "ya")
    text = text.replace("y ", "ya ")
    text = text.replace("jnyaa", "gnaa")
    text = text.replace("jnya", "gna")
    text = text.replace("jny ", "gna")
    text = text.replace("svaa", "swaa")
    text = text.replace("svā", "swā")
    return text
