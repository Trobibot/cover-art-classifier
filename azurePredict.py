from azureAuth import auth

def predictFromPath(imgPath = None):
    if (imgPath is None):
        return None

    _, _, prediction_client = auth()

    return prediction_client.PredictFromPath(imgPath)

def predictFromBuffer(imgBuffer = None):
    if (imgBuffer is None):
        return None

    _, _, prediction_client = auth()

    return prediction_client.PredictFromBuffer(imgBuffer)


def predictFromUrl(imgUrl = None):
    if (imgUrl is None):
        return None

    _, _, prediction_client = auth()

    return prediction_client.PredictFromUrl(imgUrl)