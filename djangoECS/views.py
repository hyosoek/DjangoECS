from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    data = {"result": "success",
            "data": [{"id":"itstudy", "name":"군계"},
                     {"id":"ggangpae1", "name":"아담"},
                     {"id":"tennfin1", "name":"효석"}]}
    return Response(data, status=status.HTTP_200_OK)

# =>urls.py 파일에 요청 처리 코드를 추가

