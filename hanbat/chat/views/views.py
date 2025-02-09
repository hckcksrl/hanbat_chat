from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from hanbat.chat.interactors.interactor import \
    StudentGetMenuInteractor, \
    DomitoryGetMenuInteractor, \
    StaffGetMenuInteractor


class StaffView(APIView):
    def post(self, request: Request) -> Response:
        menu = StaffGetMenuInteractor().execute(request.data)
        return Response(
            status=status.HTTP_200_OK,
            data=menu
        )


class DomitoryView(APIView):
    def post(self, request: Request) -> Response:
        menu = DomitoryGetMenuInteractor().execute(request.data)
        return Response(
            status=status.HTTP_200_OK,
            data=menu
        )


class StudentView(APIView):
    def post(self, request: Request) -> Response:
        menu = StudentGetMenuInteractor().execute(request.data)
        return Response(
            status=status.HTTP_200_OK,
            data=menu
        )

