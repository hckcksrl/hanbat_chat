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
        data = {
                "version": "2.0",
                "data": {
                    "location": '교직원 식당'
                }
        }
        if not menu:
            data['data']['lunch_menu'] = '운영 안함'
            return Response(status=status.HTTP_200_OK, data=data)

        times = ['breakfast', 'lunch', 'dinner']
        foods = ['bf_menu', 'lunch_menu', 'dinner_menu']
        for food, time, i in zip(foods, times, menu):
            data['data'][time] = i.time
            data['data'][food] = i.menu
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class DomitoryView(APIView):
    def post(self, request: Request) -> Response:
        menu = DomitoryGetMenuInteractor().execute(**request.data)
        return Response(status=status.HTTP_200_OK)


class StudentView(APIView):
    def post(self, request: Request) -> Response:
        menu = StudentGetMenuInteractor().execute(**request.data)
        return Response(status=status.HTTP_200_OK)

