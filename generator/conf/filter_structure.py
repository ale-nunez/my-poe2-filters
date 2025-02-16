
filter_structure = [
  # ----------------------------------- 0000 filter-header
  { 
    'name' : 'filter-header',
    'type' : 'filter-header'
  },
  # ----------------------------------- 0000 filter-index
  { 
    'name' : 'filter-index',
    'type' : 'filter-index'
  },
  # --------------------------------------- 0000 overrides
  { 
    'name' : 'overrides_header', 
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0000",
      "text" : "Overrides",
      "tags" : "#overrides"
    }
  },
  { 
    'name' : 'overrides_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "overr" },
      { "strictness" : "strict", "file" : "overr" },
      { "strictness" : "regular", "file" : "overr" },
      { "strictness" : "soft", "file" : "overr" }
    ] 
  },
  # ---------------------------------------- 0001 currency
  { 
    'name' : 'currency_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0001",
      "text" : "Currency",
      "tags" : "#currency"
    }
  },
  { 
    'name' : 'common_currency_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.1",
      "text" : "Common Currency",
      "tags" : "#currency"
    } 
  },
  { 
    'name' : 'common_currency_s_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0001.1.1",
      "text" : "Currency tier S",
      "tags" : "#currency-s"
    } 
  },
  { 
    'name' : 'common_currency_s_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_s" },
      { "strictness" : "strict", "file" : "curr_s" },
      { "strictness" : "regular", "file" : "curr_s" },
      { "strictness" : "soft", "file" : "curr_s" }
    ] 
  },
  { 
    'name' : 'common_currency_a_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0001.1.2",
      "text" : "Currency tier A",
      "tags" : "#currency-a"
    } 
  },
  { 
    'name' : 'common_currency_a1_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_a1" },
      { "strictness" : "strict", "file" : "curr_a1" },
      { "strictness" : "regular", "file" : "curr_a1" },
      { "strictness" : "soft", "file" : "curr_a1" }
    ] 
  },
  { 
    'name' : 'common_currency_a2_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_a2" },
      { "strictness" : "strict", "file" : "curr_a2" },
      { "strictness" : "regular", "file" : "curr_a2" },
      { "strictness" : "soft", "file" : "curr_a2" }
    ] 
  },
  { 
    'name' : 'common_currency_b_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0001.1.3",
      "text" : "Currency tier B",
      "tags" : "#currency-b"
    }
  },
  { 
    'name' : 'common_currency_b1_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_b1" },
      { "strictness" : "strict", "file" : "curr_b1" },
      { "strictness" : "regular", "file" : "curr_b1" },
      { "strictness" : "soft", "file" : "curr_b1" }
    ] 
  },
  {
    'name' : 'common_currency_b2_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_b2" },
      { "strictness" : "strict", "file" : "curr_b2" },
      { "strictness" : "regular", "file" : "curr_b2" },
      { "strictness" : "soft", "file" : "curr_b2" }
    ] 
  },
  {
    'name' : 'common_currency_b3_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_b3" },
      { "strictness" : "strict", "file" : "curr_b3" },
      { "strictness" : "regular", "file" : "curr_b3" },
      { "strictness" : "soft", "file" : "curr_b3" }
    ] 
  },
  {
    'name' : 'common_currency_b4_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_b4" },
      { "strictness" : "strict", "file" : "curr_b4" },
      { "strictness" : "regular", "file" : "curr_b4" },
      { "strictness" : "soft", "file" : "curr_b4" }
    ] 
  },
  {
    'name' : 'common_currency_b5_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_b5" },
      { "strictness" : "strict", "file" : "curr_b5" },
      { "strictness" : "regular", "file" : "curr_b5" },
      { "strictness" : "soft", "file" : "curr_b5" }
    ] 
  },
  {
    'name' : 'common_currency_b6_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_b6" },
      { "strictness" : "strict", "file" : "curr_b6" },
      { "strictness" : "regular", "file" : "curr_b6" },
      { "strictness" : "soft", "file" : "curr_b6" }
    ] 
  },
  { 
    'name' : 'common_currency_c_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0001.1.4",
      "text" : "Currency Tier C",
      "tags" : "#currency-c"
    } 
  },
  {
    'name' : 'common_currency_c1_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_c1" },
      { "strictness" : "strict", "file" : "curr_c1" },
      { "strictness" : "regular", "file" : "curr_c1" },
      { "strictness" : "soft", "file" : "curr_c1" }
    ] 
  },
  {
    'name' : 'common_currency_c2_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_c2" },
      { "strictness" : "strict", "file" : "curr_c2" },
      { "strictness" : "regular", "file" : "curr_c2" },
      { "strictness" : "soft", "file" : "curr_c2" }
    ] 
  },
  {
    'name' : 'common_currency_c3_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_c3" },
      { "strictness" : "strict", "file" : "curr_c3" },
      { "strictness" : "regular", "file" : "curr_c3" },
      { "strictness" : "soft", "file" : "curr_c3" }
    ]
  },
  { 
    'name' : 'common_currency_d_scrolls_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0001.1.5",
      "text" : "Scroll of Wisdom",
      "tags" : "#wisdom #scroll"
    }
  },
  {
    'name' : 'common_currency_d_scrolls_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_scroll_hide" },
      { "strictness" : "strict", "file" : "curr_scroll_hide" },
      { "strictness" : "regular", "file" : "curr_scroll_hide" },
      { "strictness" : "soft", "file" : "curr_scroll" }
    ] 
  },
  { 
    'name' : 'common_currency_e_gold_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0001.1.6",
      "text" : "Gold",
      "tags" : "#gold"
    }
  },
  {
    'name' : 'common_currency_e_gold_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_gold_strict" },
      { "strictness" : "strict", "file" : "curr_gold_mid" },
      { "strictness" : "regular", "file" : "curr_gold_mid" },
      { "strictness" : "soft", "file" : "curr_gold_soft" }
    ] 
  },
  # --------------------------------------- 0001.2 league-currency
  { 
    'name' : 'league_currency_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2",
      "text" : "Special and league currency",
      "tags" : "#currency #league"
    }
  },
  { 
    'name' : 'league_currency_00_common_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.1",
      "text" : "Common",
      "tags" : "#league #common"
    }
  },
  {
    'name' : 'common_currency_00_common_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_00_common" },
      { "strictness" : "strict", "file" : "scurr_00_common" },
      { "strictness" : "regular", "file" : "scurr_00_common" },
      { "strictness" : "soft", "file" : "scurr_00_common" }
    ] 
  },
  { 
    'name' : 'league_currency_01_sanctum_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.2",
      "text" : "Sanctum",
      "tags" : "#sanctum #sekhema #trial"
    }
  },
  {
    'name' : 'common_currency_01_sanctum_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_01_sanctum_uber" },
      { "strictness" : "strict", "file" : "scurr_01_sanctum_mid" },
      { "strictness" : "regular", "file" : "scurr_01_sanctum_mid" },
      { "strictness" : "soft", "file" : "scurr_01_sanctum_soft" }
    ] 
  },
  { 
    'name' : 'league_currency_02_ultimatum_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.3",
      "text" : "Ultimatum",
      "tags" : "#ultimatum #trial"
    }
  },
  {
    'name' : 'common_currency_02_ultimatum_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_02_ultimatum" },
      { "strictness" : "strict", "file" : "scurr_02_ultimatum" },
      { "strictness" : "regular", "file" : "scurr_02_ultimatum" },
      { "strictness" : "soft", "file" : "scurr_02_ultimatum" }
    ] 
  },
  { 
    'name' : 'league_currency_03_delyrium_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.4",
      "text" : "Delyrium / Simulacrum",
      "tags" : "#delyrium #simulacrum"
    } 
  },
  {
    'name' : 'common_currency_03_delyrium_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_03_delyrium" },
      { "strictness" : "strict", "file" : "scurr_03_delyrium" },
      { "strictness" : "regular", "file" : "scurr_03_delyrium" },
      { "strictness" : "soft", "file" : "scurr_03_delyrium" }
    ] 
  },
  { 
    'name' : 'league_currency_04_breach_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.5",
      "text" : "Breach / Catalyst",
      "tags" : "#breach #catalyst"
    }
  },
  {
    'name' : 'common_currency_04_breach_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_04_breach" },
      { "strictness" : "strict", "file" : "scurr_04_breach" },
      { "strictness" : "regular", "file" : "scurr_04_breach" },
      { "strictness" : "soft", "file" : "scurr_04_breach" }
    ] 
  },
  { 
    'name' : 'league_currency_05_expedition_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.6",
      "text" : "Expedition",
      "tags" : "#expedition"
    }
  },
  {
    'name' : 'common_currency_05_expedition_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_05_expedition" },
      { "strictness" : "strict", "file" : "scurr_05_expedition" },
      { "strictness" : "regular", "file" : "scurr_05_expedition" },
      { "strictness" : "soft", "file" : "scurr_05_expedition" }
    ] 
  },
  { 
    'name' : 'league_currency_06_ritual_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.7",
      "text" : "Ritual / Omens",
      "tags" : "#ritual #omen"
    }
  },
  {
    'name' : 'common_currency_06_ritual_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "scurr_06_ritual" },
      { "strictness" : "strict", "file" : "scurr_06_ritual" },
      { "strictness" : "regular", "file" : "scurr_06_ritual" },
      { "strictness" : "soft", "file" : "scurr_06_ritual" }
    ] 
  },
  { 
    'name' : 'currency_unknown_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0001.2.8",
      "text" : "Unknown Currency",
      "tags" : "#currency #unknown"
    }
  },
  {
    'name' : 'currency_unknown_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "curr_unknown" },
      { "strictness" : "strict", "file" : "curr_unknown" },
      { "strictness" : "regular", "file" : "curr_unknown" },
      { "strictness" : "soft", "file" : "curr_unknown" }
    ] 
  },
  # --------------------------------------- 0002 maps
  { 
    'name' : 'maps_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0002",
      "text" : "Maps",
      "tags" : "#maps"
    }
  },
  { 
    'name' : 'waystones_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0002.1",
      "text" : "Waystones",
      "tags" : "#maps #waystones"
    }
  },
  { 
    'name' : 'waystones_s_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0002.1.1",
      "text" : "Waystones tier S",
      "tags" : "#waystones_s"
    } 
  },
  { 
    'name' : 'waystones_s_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "maps_s" },
      { "strictness" : "strict", "file" : "maps_s" },
      { "strictness" : "regular", "file" : "maps_s" },
      { "strictness" : "soft", "file" : "maps_s" }
    ] 
  },
  { 
    'name' : 'waystones_a_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0002.1.2",
      "text" : "Waystones tier A",
      "tags" : "#waystones_a"
    } 
  },
  { 
    'name' : 'waystones_a_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "maps_a_uber" },
      { "strictness" : "strict", "file" : "maps_a_strict" },
      { "strictness" : "regular", "file" : "maps_a_regular" },
      { "strictness" : "soft", "file" : "maps_a_soft" }
    ] 
  },
  { 
    'name' : 'waystones_b_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0002.1.3",
      "text" : "Waystones tier B",
      "tags" : "#waystones_b"
    }
  },
  { 
    'name' : 'waystones_b_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "maps_b_uber" },
      { "strictness" : "strict", "file" : "maps_b_strict" },
      { "strictness" : "regular", "file" : "maps_b_regular" },
      { "strictness" : "soft", "file" : "maps_b_soft" }
    ] 
  },
  { 
    'name' : 'waystones_c_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0002.1.4",
      "text" : "Waystones tier C",
      "tags" : "#waystones_c"
    }
  },
  { 
    'name' : 'waystones_c_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "maps_c_uber" },
      { "strictness" : "strict", "file" : "maps_c_strict" },
      { "strictness" : "regular", "file" : "maps_c_regular" },
      { "strictness" : "soft", "file" : "maps_c_soft" }
    ] 
  },
  { 
    'name' : 'tablets_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0002.2",
      "text" : "Tablets",
      "tags" : "#maps #tablets"
    }
  },
  { 
    'name' : 'tablets_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "maps_tablets" },
      { "strictness" : "strict", "file" : "maps_tablets" },
      { "strictness" : "regular", "file" : "maps_tablets" },
      { "strictness" : "soft", "file" : "maps_tablets" }
    ] 
  },
  # --------------------------------------- 0003 GEMS
  { 
    'name' : 'gems_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0003",
      "text" : "Gems",
      "tags" : "#gems"
    }
  },
  { 
    'name' : 'gems_s_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0003.1",
      "text" : "Gems tier s",
      "tags" : "#gems_s"
    }
  },
  { 
    'name' : 'gems_s_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "gems_s" },
      { "strictness" : "strict", "file" : "gems_s" },
      { "strictness" : "regular", "file" : "gems_s" },
      { "strictness" : "soft", "file" : "gems_s" }
    ] 
  },
  { 
    'name' : 'gems_a_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0003.2",
      "text" : "Gems tier A",
      "tags" : "#gems_a"
    } 
  },
  { 
    'name' : 'gems_a_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "gems_a_uber" },
      { "strictness" : "strict", "file" : "gems_a_strict" },
      { "strictness" : "regular", "file" : "gems_a_regular" },
      { "strictness" : "soft", "file" : "gems_a_soft" }
    ] 
  },
  # --------------------------------------- 0004 flasks
  { 
    'name' : 'flasks_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0004",
      "text" : "Flasks",
      "tags" : "#flasks"
    }
  },
  {
    'name' : 'flasks_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "flasks_uber" },
      { "strictness" : "strict", "file" : "flasks_strict" },
      { "strictness" : "regular", "file" : "flasks_regular" },
      { "strictness" : "soft", "file" : "flasks_soft" }
    ] 
  },
  # --------------------------------------- 0005 Runes
  { 
    'name' : 'runes_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0005",
      "text" : "Runes",
      "tags" : "#runes"
    }
  },
  { 
    'name' : 'runes_a_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0005.1",
      "text" : "Runes tier A",
      "tags" : "#runes_a"
    }
  },
  {
    'name' : 'runes_a_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "runes_a_hide" },
      { "strictness" : "strict", "file" : "runes_a" },
      { "strictness" : "regular", "file" : "runes_a" },
      { "strictness" : "soft", "file" : "runes_a" }
    ]
  },
  { 
    'name' : 'runes_b_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0005.2",
      "text" : "Base Runes",
      "tags" : "#runes_b"
    }
  },
  {
    'name' : 'runes_b_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "runes_b_hide" },
      { "strictness" : "strict", "file" : "runes_b" },
      { "strictness" : "regular", "file" : "runes_b" },
      { "strictness" : "soft", "file" : "runes_b" }
    ] 
  },
  # --------------------------------------- 0006 Charms
  { 
    'name' : 'charms_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0006",
      "text" : "Charms",
      "tags" : "#charms"
    }
  },
  {
    'name' : 'charms_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "charms_uber" },
      { "strictness" : "strict", "file" : "charms_strict" },
      { "strictness" : "regular", "file" : "charms_regular" },
      { "strictness" : "soft", "file" : "charms_soft" }
    ] 
  },
  # --------------------------------------- 0007. Salvagable
  { 
    'name' : 'salvagable_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0007",
      "text" : "Salvagable",
      "tags" : "#salvagable"
    }
  },
  {
    'name' : 'salvagable_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "salvagable_hide" },
      { "strictness" : "strict", "file" : "salvagable" },
      { "strictness" : "regular", "file" : "salvagable" },
      { "strictness" : "soft", "file" : "salvagable" }
    ] 
  },
  # --------------------------------------- 0008 EQUIPMENT
  # ------------------------- 0008.0 Decorators
  {
    'name' : 'eq_decorators_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.0",
      "text" : "Decorators",
      "tags" : "#decorators"
    }
  },
  {
    'name' : 'eq_decorators_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_dec" },
      { "strictness" : "strict", "file" : "eq_dec" },
      { "strictness" : "regular", "file" : "eq_dec" },
      { "strictness" : "soft", "file" : "eq_dec" }
    ] 
  },
  # ------------------------- 0008.1 Uniques
  {
    'name' : 'eq_uniq_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.1",
      "text" : "Uniques",
      "tags" : "#uniques"
    }
  },
  {
    'name' : 'eq_uniq_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_uniq_uber" },
      { "strictness" : "strict", "file" : "eq_uniq_strict" },
      { "strictness" : "regular", "file" : "eq_uniq_regular" },
      { "strictness" : "soft", "file" : "eq_uniq_soft" }
    ] 
  },
  # ------------------------- 0008.2 Chance bases
  {
    'name' : 'eq_chance_bases_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.2",
      "text" : "Chance bases",
      "tags" : "#chance_bases"
    }
  },
  {
    'name' : 'eq_chance_bases_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_chance_bases" },
      { "strictness" : "strict", "file" : "eq_chance_bases" },
      { "strictness" : "regular", "file" : "eq_chance_bases" },
      { "strictness" : "soft", "file" : "eq_chance_bases" }
    ] 
  },
  # ------------------------- 0008.3 Jewelry
  {
    'name' : 'eq_jewelry_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.3",
      "text" : "Jewelry",
      "tags" : "#equip #jewelry"
    }
  },
  {
    'name' : 'eq_jewelry_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_jewelry" },
      { "strictness" : "strict", "file" : "eq_jewelry" },
      { "strictness" : "regular", "file" : "eq_jewelry" },
      { "strictness" : "soft", "file" : "eq_jewelry" }
    ] 
  },
  # ------------------------- 0008.4 Jewels
  {
    'name' : 'eq_jewels_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.4",
      "text" : "Jewels",
      "tags" : "#equip #jewels"
    }
  },
  {
    'name' : 'eq_jewels_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_jewels" },
      { "strictness" : "strict", "file" : "eq_jewels" },
      { "strictness" : "regular", "file" : "eq_jewels" },
      { "strictness" : "soft", "file" : "eq_jewels" }
    ] 
  },
  # ------------------------- 0008.5 Weapons
  {
    'name' : 'eq_weapons_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.5",
      "text" : "Weapons",
      "tags" : "#equip #weapons"
    }
  },
  # ------------------------- 0008.5.1 1h Weapons
  {
    'name' : 'eq_1h_weapons_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.5.1",
      "text" : "1h Weapons",
      "tags" : "#weapons #1h-weapons"
    }
  },
  # {
  #   'name' : 'eq_1h_weapons_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_weapon_1h_bases" },
  #     { "strictness" : "strict", "file" : "eq_weapon_1h_bases" },
  #     { "strictness" : "regular", "file" : "eq_weapon_1h_bases" },
  #     { "strictness" : "soft", "file" : "eq_weapon_1h_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_1h_weapons_block',
    'type' : 'class-block',
    'subtype' : '1h_weapons',
    'classes' : [
      {
        'condition' : 'claws',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_claws_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_claws_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_claws_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_claws_soft" }
        ]
      },
      {
        'condition' : 'daggers',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_daggers_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_daggers_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_daggers_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_daggers_soft" }
        ]
      },
      {
        'condition' : 'wands',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_wands_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_wands_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_wands_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_wands_soft" }
        ]
      },
      {
        'condition' : '1h_swords',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_swords_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_swords_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_swords_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_swords_soft" }
        ]
      },
      {
        'condition' : '1h_axes',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_axes_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_axes_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_axes_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_axes_soft" }
        ]
      },
      {
        'condition' : '1h_maces',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_maces_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_maces_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_maces_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_maces_soft" }
        ]
      },
      {
        'condition' : 'sceptres',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_sceptres_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_sceptres_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_sceptres_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_sceptres_soft" }
        ]
      },
      {
        'condition' : 'spears',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_spears_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_spears_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_spears_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_spears_soft" }
        ]
      },
      {
        'condition' : 'flails',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_1h_flails_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_1h_flails_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_1h_flails_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_1h_flails_soft" }
        ]
      }
    ]
  },
  {
    'name' : 'eq_1h_weapons_init',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_weapon_1h_init_strict" },
      { "strictness" : "strict", "file" : "eq_weapon_1h_init" },
      { "strictness" : "regular", "file" : "eq_weapon_1h_init" },
      { "strictness" : "soft", "file" : "eq_weapon_1h_init" }
    ] 
  },
  # ------------------------- 0008.5.2 2h weapons
  {
    'name' : 'eq_2h_weapons_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.5.2",
      "text" : "2h Weapons",
      "tags" : "#weapons #2h-weapons"
    }
  },
  # {
  #   'name' : 'eq_2h_weapons_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_weapon_2h_bases" },
  #     { "strictness" : "strict", "file" : "eq_weapon_2h_bases" },
  #     { "strictness" : "regular", "file" : "eq_weapon_2h_bases" },
  #     { "strictness" : "soft", "file" : "eq_weapon_2h_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_2h_weapons_block',
    'type' : 'class-block',
    'subtype' : '2h_weapons',
    'classes' : [
      {
        'condition' : 'bows',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_bows_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_bows_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_bows_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_bows_soft" } 
        ]
      },
      {
        'condition' : 'staves',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_staves_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_staves_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_staves_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_staves_soft" }
        ]
      },
      {
        'condition' : '2h_swords',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_swords_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_swords_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_swords_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_swords_soft" }
        ]
      },
      {
        'condition' : '2h_axes',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_axes_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_axes_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_axes_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_axes_soft" }
        ]
      },
      {
        'condition' : '2h_maces',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_maces_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_maces_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_maces_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_maces_soft" }
        ]
      },
      {
        'condition' : 'quarterstaves',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_quarterstaves_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_quarterstaves_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_quarterstaves_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_quarterstaves_soft" }
        ]
      },
      {
        'condition' : 'crossbows',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_2h_crossbows_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_2h_crossbows_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_2h_crossbows_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_2h_crossbows_soft" }
        ]
      }
    ]
  },
  {
    'name' : 'eq_2h_weapons_init',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_weapon_2h_init_strict" },
      { "strictness" : "strict", "file" : "eq_weapon_2h_init" },
      { "strictness" : "regular", "file" : "eq_weapon_2h_init" },
      { "strictness" : "soft", "file" : "eq_weapon_2h_init" }
    ] 
  },
  # ------------------------- 0008.5.3 Off-hands
  {
    'name' : 'eq_off_hands_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.5.3",
      "text" : "Off-hands",
      "tags" : "#weapons #off-hand"
    }
  },
  # {
  #   'name' : 'eq_off_hands_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_weapon_offhand_bases" },
  #     { "strictness" : "strict", "file" : "eq_weapon_offhand_bases" },
  #     { "strictness" : "regular", "file" : "eq_weapon_offhand_bases" },
  #     { "strictness" : "soft", "file" : "eq_weapon_offhand_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_off_hands_block',
    'type' : 'class-block',
    'subtype' : 'off_hands',
    'classes' : [
      {
        'condition' : 'quivers',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_offhand_quivers_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_offhand_quivers_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_offhand_quivers_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_offhand_quivers_soft" } 
        ]
      },
      {
        'condition' : 'shields',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_offhand_shields_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_offhand_shields_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_offhand_shields_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_offhand_shields_soft" }
        ]
      },
      {
        'condition' : 'focus',
        'files' : [
          { "strictness" : "uber", "file" : "eq_weapon_offhand_focus_uber" },
          { "strictness" : "strict", "file" : "eq_weapon_offhand_focus_strict" },
          { "strictness" : "regular", "file" : "eq_weapon_offhand_focus_regular" },
          { "strictness" : "soft", "file" : "eq_weapon_offhand_focus_soft" }
        ]
      }
    ]
  },
  {
    'name' : 'eq_off_hands_init',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_weapon_offhand_init_strict" },
      { "strictness" : "strict", "file" : "eq_weapon_offhand_init" },
      { "strictness" : "regular", "file" : "eq_weapon_offhand_init" },
      { "strictness" : "soft", "file" : "eq_weapon_offhand_init" }
    ] 
  },
  # ------------------------- 0008.6 Armours
  {
    'name' : 'eq_armours_header',
    'type' : 'header',
    "header-data" : {
      "type" : "2",
      "index" : "0008.6",
      "text" : "Armours",
      "tags" : "#equip #armour"
    }
  },
  # ------------------------- 0008.6.1 Body Armour
  {
    'name' : 'eq_body_armours_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.6.1",
      "text" : "Body Armour",
      "tags" : "#armour #body-armour"
    }
  },
  # {
  #   'name' : 'eq_body_armours_bases_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_armour_body_armour_bases" },
  #     { "strictness" : "strict", "file" : "eq_armour_body_armour_bases" },
  #     { "strictness" : "regular", "file" : "eq_armour_body_armour_bases" },
  #     { "strictness" : "soft", "file" : "eq_armour_body_armour_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_body_armours_block',
    'type' : 'class-block',
    'subtype' : 'body_armours',
    'classes' : [
      {
        'condition' : 'ar',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_body_armour_ar_uber" },
          { "strictness" : "strict", "file" : "eq_armour_body_armour_ar_strict" },
          { "strictness" : "regular", "file" : "eq_armour_body_armour_ar_regular" },
          { "strictness" : "soft", "file" : "eq_armour_body_armour_ar_soft" } 
        ]
      },
      {
        'condition' : 'ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_body_armour_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_body_armour_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_body_armour_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_body_armour_ev_soft" }
        ]
      },
      {
        'condition' : 'es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_body_armour_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_body_armour_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_body_armour_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_body_armour_es_soft" }
        ]
      },
      {
        'condition' : 'ar_ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_body_armour_ar_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_body_armour_ar_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_body_armour_ar_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_body_armour_ar_ev_soft" } 
        ]
      },
      {
        'condition' : 'ar_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_body_armour_ar_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_body_armour_ar_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_body_armour_ar_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_body_armour_ar_es_soft" }
        ]
      },
      {
        'condition' : 'ev_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_body_armour_ev_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_body_armour_ev_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_body_armour_ev_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_body_armour_ev_es_soft" }
        ]
      }
    ]
  },
  # ------------------------- 0008.6.2 Helmet
  {
    'name' : 'eq_helmets_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.6.2",
      "text" : "Helmet",
      "tags" : "#armour #helmet"
    }
  },
  # {
  #   'name' : 'eq_helmets_bases_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_armour_helmet_bases" },
  #     { "strictness" : "strict", "file" : "eq_armour_helmet_bases" },
  #     { "strictness" : "regular", "file" : "eq_armour_helmet_bases" },
  #     { "strictness" : "soft", "file" : "eq_armour_helmet_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_helmets_block',
    'type' : 'class-block',
    'subtype' : 'helmets',
    'classes' : [
      {
        'condition' : 'ar',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_helmet_ar_uber" },
          { "strictness" : "strict", "file" : "eq_armour_helmet_ar_strict" },
          { "strictness" : "regular", "file" : "eq_armour_helmet_ar_regular" },
          { "strictness" : "soft", "file" : "eq_armour_helmet_ar_soft" } 
        ]
      },
      {
        'condition' : 'ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_helmet_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_helmet_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_helmet_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_helmet_ev_soft" }
        ]
      },
      {
        'condition' : 'es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_helmet_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_helmet_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_helmet_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_helmet_es_soft" }
        ]
      },
      {
        'condition' : 'ar_ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_helmet_ar_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_helmet_ar_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_helmet_ar_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_helmet_ar_ev_soft" } 
        ]
      },
      {
        'condition' : 'ar_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_helmet_ar_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_helmet_ar_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_helmet_ar_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_helmet_ar_es_soft" }
        ]
      },
      {
        'condition' : 'ev_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_helmet_ev_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_helmet_ev_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_helmet_ev_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_helmet_ev_es_soft" }
        ]
      }
    ]
  },
  # ------------------------- 0008.6.3 Gloves
  {
    'name' : 'eq_gloves_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.6.3",
      "text" : "Gloves",
      "tags" : "#armour #gloves"
    }
  },
  # {
  #   'name' : 'eq_gloves_bases_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_armour_gloves_bases" },
  #     { "strictness" : "strict", "file" : "eq_armour_gloves_bases" },
  #     { "strictness" : "regular", "file" : "eq_armour_gloves_bases" },
  #     { "strictness" : "soft", "file" : "eq_armour_gloves_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_gloves_block',
    'type' : 'class-block',
    'subtype' : 'gloves',
    'classes' : [
      {
        'condition' : 'ar',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_gloves_ar_uber" },
          { "strictness" : "strict", "file" : "eq_armour_gloves_ar_strict" },
          { "strictness" : "regular", "file" : "eq_armour_gloves_ar_regular" },
          { "strictness" : "soft", "file" : "eq_armour_gloves_ar_soft" } 
        ]
      },
      {
        'condition' : 'ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_gloves_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_gloves_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_gloves_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_gloves_ev_soft" }
        ]
      },
      {
        'condition' : 'es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_gloves_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_gloves_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_gloves_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_gloves_es_soft" }
        ]
      },
      {
        'condition' : 'ar_ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_gloves_ar_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_gloves_ar_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_gloves_ar_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_gloves_ar_ev_soft" } 
        ]
      },
      {
        'condition' : 'ar_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_gloves_ar_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_gloves_ar_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_gloves_ar_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_gloves_ar_es_soft" }
        ]
      },
      {
        'condition' : 'ev_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_gloves_ev_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_gloves_ev_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_gloves_ev_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_gloves_ev_es_soft" }
        ]
      }
    ]
  },
  # ------------------------- 0008.6.3 Boots
  {
    'name' : 'eq_boots_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.6.3",
      "text" : "Boots",
      "tags" : "#armour #boots"
    }
  },
  # {
  #   'name' : 'eq_boots_bases_block',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "eq_armour_boots_bases" },
  #     { "strictness" : "strict", "file" : "eq_armour_boots_bases" },
  #     { "strictness" : "regular", "file" : "eq_armour_boots_bases" },
  #     { "strictness" : "soft", "file" : "eq_armour_boots_bases" }
  #   ] 
  # },
  {
    'name' : 'eq_boots_block',
    'type' : 'class-block',
    'subtype' : 'boots',
    'classes' : [
      {
        'condition' : 'ar',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_boots_ar_uber" },
          { "strictness" : "strict", "file" : "eq_armour_boots_ar_strict" },
          { "strictness" : "regular", "file" : "eq_armour_boots_ar_regular" },
          { "strictness" : "soft", "file" : "eq_armour_boots_ar_soft" } 
        ]
      },
      {
        'condition' : 'ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_boots_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_boots_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_boots_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_boots_ev_soft" }
        ]
      },
      {
        'condition' : 'es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_boots_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_boots_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_boots_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_boots_es_soft" }
        ]
      },
      {
        'condition' : 'ar_ev',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_boots_ar_ev_uber" },
          { "strictness" : "strict", "file" : "eq_armour_boots_ar_ev_strict" },
          { "strictness" : "regular", "file" : "eq_armour_boots_ar_ev_regular" },
          { "strictness" : "soft", "file" : "eq_armour_boots_ar_ev_soft" } 
        ]
      },
      {
        'condition' : 'ar_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_boots_ar_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_boots_ar_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_boots_ar_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_boots_ar_es_soft" }
        ]
      },
      {
        'condition' : 'ev_es',
        'files' : [
          { "strictness" : "uber", "file" : "eq_armour_boots_ev_es_uber" },
          { "strictness" : "strict", "file" : "eq_armour_boots_ev_es_strict" },
          { "strictness" : "regular", "file" : "eq_armour_boots_ev_es_regular" },
          { "strictness" : "soft", "file" : "eq_armour_boots_ev_es_soft" }
        ]
      }
    ]
  },
  # ------------------------- 0008.6.5 Armour init
  {
    'name' : 'eq_armour_init_header',
    'type' : 'header',
    "header-data" : {
      "type" : "3",
      "index" : "0008.6.5",
      "text" : "Armour init",
      "tags" : "#armour #init"
    }
  },
  {
    'name' : 'eq_armour_init_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "eq_armour_init" },
      { "strictness" : "strict", "file" : "eq_armour_init" },
      { "strictness" : "regular", "file" : "eq_armour_init" },
      { "strictness" : "soft", "file" : "eq_armour_init" }
    ] 
  },
  # ------------------------- 0009 Filter init
  {
    'name' : 'filter_init_header',
    'type' : 'header',
    "header-data" : {
      "type" : "1",
      "index" : "0009",
      "text" : "Init",
      "tags" : "#init"
    }
  },
  {
    'name' : 'filter_init_block',
    'type' : 'block',
    'files' : [
      { "strictness" : "uber", "file" : "init" },
      { "strictness" : "strict", "file" : "init" },
      { "strictness" : "regular", "file" : "init" },
      { "strictness" : "soft", "file" : "init" }
    ] 
  }
  # ----------------------------------- filter-footer
  # {
  #   'name' : 'filter_footer',
  #   'type' : 'block',
  #   'files' : [
  #     { "strictness" : "uber", "file" : "footer" },
  #     { "strictness" : "strict", "file" : "footer" },
  #     { "strictness" : "regular", "file" : "footer" },
  #     { "strictness" : "soft", "file" : "footer" }
  #   ] 
  # }
]