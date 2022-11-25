from azureAuth import auth

def predictFromImage(img = None):
    if (img is None):
        return None

    _, _, prediction_client = auth()

    return prediction_client.PredictFromImage(img)



def predictFromUrl(url = None):
    if (url is None):
        return None

    _, _, prediction_client = auth()

    return prediction_client.PredictFromUrl(url)