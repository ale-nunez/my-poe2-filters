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

filter_version = '0.0.2'

conf = [{
  'name' : 'test-filter',
  'version' : filter_version,
  'author' : 'Ale Nunez',
  'description' : 'Test Template for Poe2: Custom filter',
  'strictness' : 'regular', # 'soft', 'regular', 'strict', 'uber'
  '1h_weapons' : [], # list of types of 1h weapons to show
  # list of types of 2h weapons to show 
  '2h_weapons' : ['bows'],  # [ 'bows', 'staves', '2h_swords', '2h_axes', '2h_maces', 'quarterstaves', 'crossbows' ]
  # list of types of off-hands to show 
  'off_hands' : ['quivers'],
  # list of types of body_armours to show 
  'body_armours' : ['ev', 'ev_es'], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of helmets to show
  'helmets' : ['es', 'ev_es'], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of gloves to show
  'gloves' : ['ev', 'es', 'ev_es'], # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
  # list of types of boots to show
  'boots' : ['ev', 'es', 'ev_es'] # ['ar', 'ev', 'es', 'ar_ev', ar_es', 'ev_es']
}]