# Excluded source names

The upstream addon defines internal IDs, error codes, test character names, sample NPC names,
and colored wrapper strings as name fields. These are not treated as translation keys
without evidence they are displayed. This is deliberate: translating control IDs could
change action routing.

The 415 name-only human-readable strings selected for zhCN are translated in the locale
table. In-game checks are still needed to confirm each call site runs through L.tr().
