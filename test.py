from azureAuth import auth
from azurePrepare import upload_tags, Upload_Images_to_Azure
from fetchTags import fetchMostUsedTags
from fetchCover import fetchAlbumsByTags

if __name__ == '__main__':
    custom_vision_project, training_client = auth()

    tags = fetchMostUsedTags(sampleAmount=1000, doCreateCsv=True)
    upload_tags(tags, custom_vision_project, training_client)

    covers = fetchAlbumsByTags(tags)
    Upload_Images_to_Azure(covers, custom_vision_project, training_client)
