import requests
import pandas as pd

def fetchAlbumsByTags(tags, amountByTag = 25):
    albums = pd.DataFrame(columns=['mbid', 'name', 'tags', 'cover_url'])

    for _, tag in tags.iterrows():
        print(f'[ALBUM FETCH] fetch tag: {tag["name"]}')

        partialAlbums = fetchAlbumsByTag(tag['name'], sampleAmount=amountByTag)
        albums = pd.concat([albums, partialAlbums], ignore_index=True)

    albums    
    
    return albums

def fetchAlbumsByTag(tag, sampleAmount = -1):
    albums = pd.DataFrame(columns=['mbid', 'name', 'tags', 'cover_url'])

    releaseGroupData = requests.get(f'https://musicbrainz.org/ws/2/release-group?query=primarytype:Album%20AND%20tag:{tag}&offset=0&fmt=json').json()

    requestOffset = 0
    requestMaxAlbum = releaseGroupData['count'] if sampleAmount == -1 else sampleAmount
    requestAmountAlbum = len(releaseGroupData['release-groups'])

    requestOffset = 0
    while requestOffset * requestAmountAlbum < requestMaxAlbum:
        print(f'[ALBUM FETCH] fetch offset: {requestOffset * requestAmountAlbum}, fetched amount {requestOffset * requestAmountAlbum + requestAmountAlbum}')

        partialReleaseGroups = requests.get(f'https://musicbrainz.org/ws/2/release-group?query=primarytype:Album%20AND%20tag:{tag}&offset={requestOffset * requestAmountAlbum}&fmt=json').json()
    
        if (partialReleaseGroups.get('error') is not None):
            continue

        for partialReleaseGroup in partialReleaseGroups['release-groups']:
            cover = requests.get(f'http://www.coverartarchive.org/release-group/{partialReleaseGroup["id"]}')

            if (cover.status_code == 404):
                continue

            albums.loc[len(albums.index)] = [partialReleaseGroup['id'], partialReleaseGroup['title'], tag, cover.json()['images'][0]['thumbnails']['small']]

        requestOffset += 1

    return albums

tags = pd.read_csv('./sortedTags.csv')
albums = fetchAlbumsByTags(tags, amountByTag=100)
albums.to_csv('sortedAlbums.csv')
print(len(albums), albums.cover_url.nunique())

# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_rows', None)

# albums = pd.read_csv('./sortedAlbums.csv')
# print(albums.sort_values(by='cover_url'))