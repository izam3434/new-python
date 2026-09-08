survey_results = [
    ["Python", "Java", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "Javascript", "C++", "Java"]
]

#1. Identify the languages that were chosen by all participants
language_sets = [set(languages) for languages in survey_results]
common_languages = set.intersection(*language_sets)
print("Languages chosen by all participants:", common_languages)

#2. Find the languages that were only chosen by a single participant
single_choice_languages = set()
for lang in set.union(*language_sets):
    count = sum(1 for lang_set in language_sets if lang in lang_set)
    if count == 1:
        single_choice_languages.add(lang)
print("Languages chosen by a single participant:", single_choice_languages)

#3. Determine the number of unique languages mentioned in the survey
all_languages = set.union(*language_sets)
print("Number of unique languages mentioned in the survey:", len(all_languages))

#4. List the languages that were chosen by exactly two participants
two_choice_languages = set()
for lang in all_languages:
    count = sum(1 for lang_set in language_sets if lang in lang_set)
    if count == 2:
        two_choice_languages.add(lang)
print("Languages chosen by exactly two participants:", two_choice_languages)

#5. Find participants who have the exact same set of favorite languages
same_favorite_languages = []
for i, lang_set1 in enumerate(language_sets):
    for j, lang_set2 in enumerate(language_sets[i + 1:], i + 1):
        if lang_set1 == lang_set2:
            same_favorite_languages.append((i, j))
print("Participants with the exact same set of favorite languages:", same_favorite_languages)