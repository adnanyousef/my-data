from datasette.app import Datasette
app = Datasette(files=['har_desktop.db', 'har_mobile.db']).app()

