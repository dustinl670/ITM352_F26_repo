

celebs = ("Austin Abrams", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Elizabeth Olsen")
ages = (30, 36, 33, 62, 37)

celeb_list = []
for celeb in celebs:
    celeb_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)