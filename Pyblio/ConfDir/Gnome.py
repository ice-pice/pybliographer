from Pyblio import Config

Config.define ('gnome/columns', """ A list of the fields displayed
on the main screen of the interface """,
               Config.List (Config.String ()))

Config.define ('gnome/tooltips', """ A boolean indicating if
tooltips are enabled """, Config.Boolean ())

Config.define ('gnome/native-as-default', """ Should we edit the
entries in their native format by default ? """, Config.Boolean ())

Config.define ('gnome/searched', """ List of searchable fields """,
               Config.List (Config.String ()))

# --------------------------------------------------

Config.set ('gnome/searched', ['Author', 'Title', 'Abstract', 'Date'])

Config.set ('gnome/tooltips', 1)

Config.set ('gnome/native-as-default', 0)

Config.set ('gnome/columns', ('Author', 'Date', 'Title'))
