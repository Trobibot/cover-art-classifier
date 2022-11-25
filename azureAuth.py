from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

from classes.predicator import Predicator

def auth():
    try:
        project_id              = '48c49e54-a67c-4aa6-a580-712053096527'
        iteration_name          = 'Iteration2'

        training_endpoint       = 'https://northeurope.api.cognitive.microsoft.com/'
        training_key            = '449c88fc21fe45f38bf2fea2198ae3c4'
        training_credentials    = ApiKeyCredentials(in_headers={"Training-key": training_key})
        training_client         = CustomVisionTrainingClient(training_endpoint, training_credentials)

        prediction_endpoint     = f'https://northeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/{project_id}/classify/iterations/{iteration_name}'
        prediction_key          = '449c88fc21fe45f38bf2fea2198ae3c4'
        prediction_client       = Predicator(prediction_endpoint, prediction_key)
        
        custom_vision_project   = training_client.get_project(project_id)

        if(custom_vision_project):
            print("auth success")

        return custom_vision_project, training_client, prediction_client
    
    except Exception as ex:
        print(ex)
