# conf = {
#   'name' : 'filter-name',
#   'strictness' : 'regular', #'soft, regular, semi-strict, strict, very-strict, uber-strict, all',
#   '1h_weapons' : [], # list of types of 1h weapons to show
#   '2h_weapons' : [],  # list of types of 2h weapons to show
#   'off_hands' : [], # list of types of off-hands to show 
#   'body_armours' : ['ar', 'ev'], # list of types of armour to show ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
#   'helmets' : [], # list of types of armour to show ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
#   'gloves' : [], # list of types of armour to show ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
#   'boots' : [] # list of types of armour to show ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
# }

filter_version = '0.0.1'
author = 'Ale Nunez'

# --------------------------------- filter bow 1 

filter_bow1_soft = {
  'name' : 'bow1_soft',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: Soft filter: bow, quiver, armour ev, ev_es, es',
  'strictness' : 'soft', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'bows' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'quivers' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'ev', 'es', 'ev_es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}

filter_bow1_regular = {
  'name' : 'bow1_regular',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: Regular filter: bow, quiver, armour ev, ev_es, es',
  'strictness' : 'regular', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'bows' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'quivers' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'ev', 'es', 'ev_es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}

filter_bow1_strict = {
  'name' : 'bow1_strict',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: strict filter: bow, quiver, armour ev, ev_es, es',
  'strictness' : 'strict', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'bows' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'quivers' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'ev', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'ev', 'es', 'ev_es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}

filter_bow1_uber = {
  'name' : 'bow1_uber',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: uber filter: bow, quiver, armour ev, ev_es, es',
  'strictness' : 'uber', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'bows' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'quivers' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'ev', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'ev', 'es', 'ev_es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'ev', 'es', 'ev_es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}


# --------------------------------- filter sorc 1 

filter_sorc_soft = {
  'name' : 'sorc_soft',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: Soft filter: sorc, es',
  'strictness' : 'soft', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [ 'wands' ],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'staves' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'shields', 'focus' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}

filter_sorc_regular = {
  'name' : 'sorc_regular',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: Regular filter: sorc, es',
  'strictness' : 'regular', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [ 'wands' ],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'staves' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'shields', 'focus' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}

filter_sorc_strict = {
  'name' : 'sorc_strict',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: Strict filter: sorc, es',
  'strictness' : 'strict', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [ 'wands' ],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'staves' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'shields', 'focus' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}

filter_sorc_uber = {
  'name' : 'sorc_uber',
  'version' : filter_version,
  'author' : author,
  'description' : 'Test Template for Poe2: Uber filter: sorc, es',
  'strictness' : 'uber', # 'soft', 'regular', 'strict', 'uber'
  # list of types of 1h weapons to show 
  '1h_weapons' : [ 'wands' ],  # [ 'claws', 'daggers', 'wands', '1h_swords', '1h_axes', '1h_maces', 'sceptres', 'spears', 'flails' ]
  # list of types of 2h weapons to show 
  '2h_weapons' : [ 'staves' ],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : [ 'shields', 'focus' ], # [ 'quivers', 'shields', 'focus' ]
  # list of types of body_armours to show 
  'body_armours' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : [ 'es' ], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : [ 'es' ] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}