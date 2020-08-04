import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("ABBA")
artist_repository.save(artist1)
artist2 = Artist("Fleetwood Mac")
artist_repository.save(artist2)

album1 = Album("Greatest Hits", "Pop", artist1)
album_repository.save(album1)
album2 = Album("Rumours", "Classic Rock", artist2)
album_repository.save(album2)
album3 = Album("Voulez-Vous", "Pop", artist1)
album_repository.save(album3)

artists = artist_repository.select_all()

album1.title = "Greatest Hits Vol. 2"
album_repository.update(album1)

found_album = album_repository.select(album2.id)
print(found_album.artist.__dict__)

found_albums = artist_repository.albums(artist1)
for album in found_albums:
    print(album.__dict__)

album_repository.delete(album3.id)

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)


pdb.set_trace()
