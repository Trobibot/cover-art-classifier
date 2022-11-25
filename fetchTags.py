import requests
import pandas as pd

def fetchMostUsedTags(amount = 50, sampleAmount = -1, doCreateCsv = False):
    tags = pd.DataFrame(columns=['mbid', 'name'])
    
    releaseGroupData = requests.get(f'https://musicbrainz.org/ws/2/release-group?query=primarytype:Album%20AND%20tag:*&offset=0&fmt=json').json()

    requestOffset = 0
    requestMaxTag = releaseGroupData['count'] if sampleAmount == -1 else sampleAmount
    requestAmountTag = len(releaseGroupData['release-groups'])

    while requestOffset * requestAmountTag < requestMaxTag:
        print(f'[TAG FETCH] fetch offset: {requestOffset}, fetched amount {requestOffset * requestAmountTag + requestAmountTag}')
        print(requestOffset * requestAmountTag, requestMaxTag)
        
        partialReleaseGroups = requests.get(f'https://musicbrainz.org/ws/2/release-group?query=primarytype:Album%20AND%20tag:*&offset={requestOffset}&fmt=json').json()
        
        if (partialReleaseGroups.get('error') is not None):
            continue

        for partialReleaseGroup in partialReleaseGroups['release-groups']:
            for partialReleaseGroupTag in partialReleaseGroup['tags']:
                tags.loc[len(tags.index)] = [None, partialReleaseGroupTag['name']]
        
        requestOffset += 1

    if (doCreateCsv):
        tags.name.value_counts().head(amount).to_csv('sortedTags.csv')

    return tags.name.value_counts().head(amount)

fetchMostUsedTags()
