import operator


def get_language_starred(user, lang):
    count = 0
    stars = user.get_starred()
    for star in stars:
        if star.language == lang:
            count += 1

    print("You have " + str(count) + " starred repos with " + lang)


def get_starred_list(user, order=None):
    star_list = {}
    stars = user.get_starred()
    for star in stars:
        if star.language not in star_list:
            star_list[star.language] = 1
        else:
            star_count = star_list[star.language]
            star_count += 1
            star_list[star.language] = star_count

    sorted_languages = None

    if order:
        if order == 'asc':
            sorted_languages = sorted(
                star_list.items(), key=operator.itemgetter(1))
        elif order == 'desc':
            sorted_languages = sorted(star_list.items(),
                                      key=operator.itemgetter(1), reverse=True)

    if not sorted_languages:
        sorted_languages = star_list

    for lang in sorted_languages:
        val = f'{lang[0]} {lang[1]}'
        print(val)


def get_list_of_type(user, lang):
    all_starred = user.get_starred()
    repo_list = []
    for star in all_starred:
        if star.language == lang:
            repo_list.append(star.full_name)

    for repo in repo_list:
        print(repo)
