# line length for each block header:
len0 = 150
len1 = 110
len2 = 80
len3 = 48

# --- FUNCTIONS -----------------------------------------------------------------

# ---------------------------------------------------------- function header_line
def header_line(type, symbol, length, text) : 
  line = '# '
  if type == "1" : # [ 1: "# ----", "# ===" ]
    while len(line) < length :
      line += symbol
    line += '\n'
    return line
  
  elif type == "2" : # [ 2: "# text " ]
    line = line + text
    line += '\n'
    return line
  
  elif type == "3" : # [ "3: # --- #text" ]
    line = ' ' + text
    while len(line) < (length-2) : 
      line = symbol + line
    line = '# ' + line
    line += '\n'
    return line
  else :
    pass
# ------------------ end of header_line

# --------------------------------------------------------- function header_block
def header_block(type, index, text, tags) :
  block = ''
  title = index + '. ' + text

  if type == '1' : 
    line_len = len1
    lines = [
      header_line('1', '=', line_len, ''),
      header_line('1', '-', line_len, ''),
      header_line('2', '', line_len, title.upper()),
      header_line('3', '-', line_len, tags),
      header_line('1', '=', line_len, ''),
      '\n'
    ]
  
  elif type == '2' :
    line_len = len2
    lines = [
      header_line('1', '=', line_len, ''),
      header_line('2', '', line_len, title),
      header_line('3', '=', line_len, tags),
      '\n'
    ]
  
  elif type == '3' :
    line_len = len3
    lines =  [
      header_line('1', '-', line_len, ''),
      header_line('2', '', line_len, title),
      header_line('3', '-', line_len, tags),
      '\n'
    ]
  
  else : 
    lines = []

  for line in lines: 
      block += line
    
  return block
# ------------------ end of header_block

# ---------------------------------------------------------- function filter_header
def filter_header(filter_title, version, author, description) :
  result_block = ''
  # filter_title = 'My Custom Filter Template for Path of Exile 2'
  # version = '0.0.1'
  # author = 'Ale Nuñez'
  # description = 'Basic Template for Poe2 Custom filter'
  line_len = len0
  lines = [
    header_line('1', '=', line_len, ''),
    header_line('2', '', line_len, filter_title),
    header_line('1', '=', line_len, ''),
    header_line('2', '=', line_len, 'VERSION: ' + version),
    header_line('2', '=', line_len, 'AUTHOR: ' + author),
    header_line('2', '=', line_len, description),
    header_line('2', '=', line_len, ''),
    '\n'
  ]

  for line in lines: 
      result_block += line

  return result_block

# print(header_line('3', '=', len1, 'hello'))
# print(header_block('1', '0001', 'HOLA', '#currency'))
# print(header_block('2', '0001', 'Currency', '#currency'))
# print(header_block('3', '0001', 'Currency', '#currency'))
# print(filter_header())


# COMENT TYPES
# -- filter-header: 
# len(150)
#
# =======================================================================================================================================================
# My Filter Template - for Path of Exile 2
# =======================================================================================================================================================
#
# ---------------------------------------------------------------------------------------------------
#
# Block 0: (to deprecate)
# --------------------------------------------------------------------------------------------------
# 0. OVERRIDES
# --------------------------------------------------------------------------------------------------
#
# Block 1 
# len(100)
#
# ==================================================================================================
# --------------------------------------------------------------------------------------------------
# 0001. CURRENCY
# ---------------------------------------------------------------------------------------- #currency
# ==================================================================================================
#
# Block 2: 
# len(80)
#
# ==============================================================================
# 0001.1 Common currency
# ==================================================================== #currency
#
# Block 3: 
# len(48)
#
# ----------------------------------------------
# 0001.1.1 Currency Tier S
# ---------------------------------- #currency-s