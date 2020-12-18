yaku_dict_default = {
    "Aka Dora": "Aka Dora",
    "Chankan": "Chankan",
    "Chantai": "Chantai",
    "Chiitoitsu": "Chiitoitsu",
    "Chinitsu": "Chinitsu",
    "Yakuhai (chun)": "Yakuhai (chun)",
    "Double Riichi": "Double Riichi",
    "Dora": "Dora",
    "Yakuhai (east)": "Yakuhai (east)",
    "Haitei Raoyue": "Haitei Raoyue",
    "Yakuhai (haku)": "Yakuhai (haku)",
    "Yakuhai (hatsu)": "Yakuhai (hatsu)",
    "Honitsu": "Honitsu",
    "Honroutou": "Honroutou",
    "Houtei Raoyui": "Houtei Raoyui",
    "Iipeiko": "Iipeiko",
    "Ippatsu": "Ippatsu",
    "Ittsu": "Ittsu",
    "Junchan": "Junchan",
    "Nagashi Mangan": "Nagashi Mangan",
    "Yakuhai (north)": "Yakuhai (north)",
    "Pinfu": "Pinfu",
    "Renhou": "Renhou",
    "Riichi": "Riichi",
    "Rinshan Kaihou": "Rinshan Kaihou",
    "Ryanpeikou": "Ryanpeikou",
    "San Ankou": "San Ankou",
    "San Kantsu": "San Kantsu",
    "Sanshoku Doujun": "Sanshoku Doujun",
    "Sanshoku Doukou": "Sanshoku Doukou",
    "Shou Sangen": "Shou Sangen",
    "Yakuhai (south)": "Yakuhai (south)",
    "Tanyao": "Tanyao",
    "Toitoi": "Toitoi",
    "Menzen Tsumo": "Menzen Tsumo",
    "Yakuhai (west)": "Yakuhai (west)",
    "Yakuhai (wind of place)": "Yakuhai (wind of place)",
    "Yakuhai (wind of round)": "Yakuhai (wind of round)",
    "Chiihou": "Chiihou",
    "Chinroutou": "Chinroutou",
    "Chuuren Poutou": "Chuuren Poutou",
    "Daburu Chuuren Poutou": "Daburu Chuuren Poutou",
    "Kokushi Musou Juusanmen Matchi": "Kokushi Musou Juusanmen Matchi",
    "Daisangen": "Daisangen",
    "Daisharin": "Daisharin",
    "Daisuurin": "Daisuurin",
    "Daichikurin": "Daichikurin",
    "Dai Suushii": "Dai Suushii",
    "Kokushi Musou": "Kokushi Musou",
    "Renhou (yakuman)": "Renhou (yakuman)",
    "Ryuuiisou": "Ryuuiisou",
    "Shousuushii": "Shousuushii",
    "Suu Ankou": "Suu Ankou",
    "Suu Ankou Tanki": "Suu Ankou Tanki",
    "Suu Kantsu": "Suu Kantsu",
    "Tenhou": "Tenhou",
    "Tsuu Iisou": "Tsuu Iisou",
}

fu_dict_default = {
    "base": "Base Fu",
    "penchan": "Side Tile Wait",
    "kanchan": "Middle Tile Wait",
    "valued_pair": "Valued Pair",
    "double_valued_pair": "Double Valued Pair",
    "pair_wait": "Single Wait",
    "tsumo": "Self Draw",
    "hand_without_fu": "Hand Without Extra Fu",
    "closed_pon": "Simple Closed Triplet",
    "open_pon": "Simple Open Triplet",
    "closed_terminal_pon": "Terminal Closed Triplet",
    "open_terminal_pon": "Terminal Open Triplet",
    "closed_kan": "Simple Closed Kan",
    "open_kan": "Simple Open Kan",
    "closed_terminal_kan": "Terminal Closed Kan",
    "open_terminal_kan": "Terminal Open Kan",
}

cost_dict_default = {
    "fu": " Fu",
    "han": " Han",
    "point": " Point",
    "dealer_pays": "Dealer Pays",
    "player_pays": "Player Pays",
    "trigger_pays": "Trigger Pays",
    "kyoutaku_bonus": "Riichi Bon On Desk",
    "total": "Total",
    "fu_details": "Fu Details",
    "cost_details": "Point Details",
    "yaku_details": "Yaku Details",
    "unavailable": "Unavailable",
    "kazoe yakuman": "Kazoe Yakuman",
    "kazoe sanbaiman": "Kazoe Sanbaiman",
    "6x yakuman": "Rokubai Yakuman",
    "5x yakuman": "Gobai Yakuman",
    "4x yakuman": "Yonbai Yakuman",
    "3x yakuman": "Toripuru Yakuman",
    "2x yakuman": "Daburu Yakuman",
    "yakuman": "Yakuman",
    "sanbaiman": "Sanbaiman",
    "baiman": "Baiman",
    "haneman": "Haneman",
    "mangan": "Mangan",
    "kiriage mangan": "Kiriage Mangan",
    "nagashi mangan": "Nagashi Mangan",
}

err_dict_default = {
    "Error": "Error",
    "NWT": "Win tile not in hand",
    "OHR": "Riichi can't be declared with open hand",
    "OHD": "Daburu Riichi can't be declared with open hand",
    "IWR": "Ippatsu can't be declared without Riichi",
    "HNW": "Hand is not winning",
    "NHY": "No yaku in hand",
    "CWT": "Chankan can't be declared with tsumo",
    "RWT": "Rinshan Kaihou can't be declared without tsumo",
    "HAT": "Haitei Raoyue can't be declared without tsumo",
    "HOT": "Houtei Raoyui can't be declared with tsumo",
    "HAR": "Haitei Raoyue can't be declared with Rinshan Kaihou",  # A dead wall tile is not considered as "the last tile"
    "HOC": "Houtei Raoyui can't be declared with Chankan",  # You can't make a meld in the last turn
    "TND": "Tenhou can't be declared by non-dealer",
    "TWT": "Tenhou can't be declared without tsumo",
    "TWM": "Tenhou can't be declared with meld",
    "CAD": "Chiihou can't be declared by dealer",
    "CWT": "Chiihou can't be declared without tsumo",
    "CWM": "Chiihou can't be declared with meld",
    "RAD": "Renhou can't be declared by dealer",
    "RWT": "Renhou can't be declared with tsumo",
    "RWM": "Renhou can't be declared with meld"
}
