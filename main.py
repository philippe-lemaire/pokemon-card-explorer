import utils

sets = utils.get_sets("")
# utils.write_to_csv(sets)

# dragons = utils.search_cards('supertype:pokemon types:dragon')
# utils.save_search_to_csv(dragons, 'dragons')

# trainers = utils.search_cards('supertype:trainer set.id:sm10')
# utils.save_search_to_csv(trainers, 'trainers_from_sm10')

# fire_pkm_from_last_set = utils.search_cards('supertype:pokemon types:fire set.id:swsh5')
# utils.save_search_to_csv(fire_pkm_from_last_set, 'fire_mons_from_battle_styles')

# double_colorless_attacks = utils.search_cards('attacks.cost:Colorless,Colorless')
# len(double_colorless_attacks)
# utils.download_cards_imgs('swsh45')

# swsh45 = utils.search_cards('set.id:swsh45')
# utils.download_cards_csv_and_img('set.id:sm115')

sets = utils.get_sets("")
for item in sets:
    utils.download_cards("set.id:" + item["id"])
