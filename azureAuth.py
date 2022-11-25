from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

def auth():
    try:
        training_endpoint   = 'https://northeurope.api.cognitive.microsoft.com/'
        training_key        = '449c88fc21fe45f38bf2fea2198ae3c4'
        project_id          = '48c49e54-a67c-4aa6-a580-712053096527'

        credentials             = ApiKeyCredentials(in_headers={"Training-key": training_key})
        training_client         = CustomVisionTrainingClient(training_endpoint, credentials)
        custom_vision_project   = training_client.get_project(project_id)

        if(custom_vision_project):
            print("auth success")

        return custom_vision_project, training_client
    
    except Exception as ex:
        print(ex)