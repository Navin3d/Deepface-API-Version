from deepface import DeepFace
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
metrics = ["cosine", "euclidean", "euclidean_l2"]


@api_view(["POST"])
def verify(request):
    if request.method == "POST":
        data = request.data
        result = DeepFace.verify(img1_path=data["img1_path"], img2_path=data["img2_path"], model_name=models[1],
                                 enforce_detection=False)
        return Response(data=result, status=status.HTTP_200_OK)


@api_view(["POST"])
def find(request):
    if request.method == "POST":
        data = request.data
        result = DeepFace.find(img_path=data["img_path"], db_path=data["db_path"], model_name=models[1],
                               distance_metric=metrics[1])
        return Response(data=result, status=status.HTTP_200_OK)


@api_view(["POST"])
def analize(request):
    if request.method == "POST":
        data = request.data
        result = DeepFace.analyze(img_path=data["img_path"], actions=('age', 'gender', 'race', 'emotion'))
        return Response(data=result, status=status.HTTP_200_OK)
