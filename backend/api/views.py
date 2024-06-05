from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.permissions import IsAuthenticatedOrAdminOrMechanic
from api.serializers import (
    CarMainPageSerializer,
    CarSerializer,
    CarTechnicalServicePhotoSerializer,
    CarTechnicalServiceSerializer,
    CreateCarTechnicalServiceSerializer,
    UserRentSerializer
)
from car.models import Car, CarTechnicalService
from car_rent_invest.models import UserRent


class CarViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarMainPageSerializer

    def get_serializer_class(self):
        '''Выбираем сериализатор зависимо от того это каталог на главной
        или получение всей информации об автомобиле
        '''
        if self.action == 'retrieve':
            return CarSerializer
        return self.serializer_class

    def get_queryset(self):
        '''Получаем все не скрытые карточки.'''
        return self.queryset.filter(~Q(card__hide=True))

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsAuthenticatedOrAdminOrMechanic]
    )
    def my_rents(self, request):
        '''Получаем список арендованных автомобилей принадлежащие пользователю.
        '''
        rents = UserRent.objects.filter(user=request.user, complited=False)
        serializer = UserRentSerializer(
            rents, many=True, context={'request': request}
        )
        return Response(serializer.data)


class CarTechnicalServiceViewSet(viewsets.ModelViewSet):

    pagination_class = None
    queryset = CarTechnicalService.objects.all()
    http_method_names = ('delete', 'get', 'patch', 'post')
    serializer_class = CarTechnicalServiceSerializer
    permission_classes = [IsAuthenticatedOrAdminOrMechanic]

    def get_serializer_class(self):
        """Выбирает сериализатор, в зависимости от метода запроса."""
        if self.request.method == 'GET':
            return self.serializer_class
        return CreateCarTechnicalServiceSerializer

    def get_queryset(self):
        '''Получаем сервисы автомобиля.'''
        # TODO убрать хардкод
        # TODO попробовать перенести обработку ошибок в сериализатор
        if self.request.user.is_client and self.action == 'list':
            return self.queryset.filter(author=self.request.user)[0:5]
        elif self.action == 'list':
            return self.queryset[0:10]
        return self.queryset

    @action(
        detail=True,
        methods=['GET']
    )
    def get_photos(self, request, pk=None):
        serializer = CarTechnicalServicePhotoSerializer(
            self.get_object().photos.all(),
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)