from azureAuth import auth
from azurePrepare import upload_tags, Upload_Images_to_Azure
# from fetchTags import fetchMostUsedTags
# from fetchCover import fetchAlbumsByTags

import pandas as pd

if __name__ == '__main__':
    custom_vision_project, training_client, _ = auth()

    # tags = pd.read_csv('./sortedTags.csv')
    # upload_tags(tags, custom_vision_project, training_client)

    # albums = pd.read_csv('./sortedAlbums.csv')
    # Upload_Images_to_Azure(albums, custom_vision_project, training_client)
