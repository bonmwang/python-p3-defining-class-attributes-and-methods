class Album:

    album_count = 0

    def __init__(self, date):
        Album.album_count += 1
        self.release_date = date

Album()
Album()
Album()

Album.album_count