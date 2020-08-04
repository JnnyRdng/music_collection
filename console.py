import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()

artist1 = Artist("ABBA")
artist_repository.save(artist1)
artist2 = Artist("Fleetwood Mac")
artist_repository.save(artist2)

artists = artist_repository.select_all()

pdb.set_trace()
