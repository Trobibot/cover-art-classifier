import requests

class Predicator():

    endpoint    = None
    key         = None

    def __init__(self, endpoint, key) -> None:
        self.endpoint   = 'https://northeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/48c49e54-a67c-4aa6-a580-712053096527/classify/iterations/Iteration2'
        self.key        = '449c88fc21fe45f38bf2fea2198ae3c4'

    def __prepareUrlFor(self, type):
        return f'{self.endpoint}/{type}?Prediction-key={self.key}'
 
    def PredictFromUrl(self, imageUrl):
        return requests.post(url=self.__prepareUrlFor('url'), json={'url': imageUrl}).json()['predictions']
        
    def PredictFromPath(self, imagePath):
        with (open(imagePath, 'rb')) as imageBuffer:
            return requests.post(url=self.__prepareUrlFor('image'), files={'media': imageBuffer}).json()['predictions']
        
    def PredictFromBuffer(self, imageBuffer):
        return requests.post(url=self.__prepareUrlFor('image'), files={'media': imageBuffer}).json()['predictions']


