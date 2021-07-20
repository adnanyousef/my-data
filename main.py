from datasette.app import Datasette
app = Datasette(files=['./data/data.db']).app()

