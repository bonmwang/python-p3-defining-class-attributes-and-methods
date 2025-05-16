class Album:
    album_count = 258

    def __init__(self, date):
        self.release_date = date

album = Album(1991)
album.release_date
Album.album_count

joshua_tree = Album(1987)
joshua_tree.album_count
Album.album_count += 1
Album.album_count