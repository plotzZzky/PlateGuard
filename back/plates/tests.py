from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from users.models import Profile
from .models import ListPlates, Plate


class PlatesTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'temporary',
            'password': '1234x567'}
        self.client = APIClient()
        self.user = User.objects.create_user(**self.credentials)
        self.profile = self.create_office()
        self.client.login()
        self.token = Token.objects.create(user=self.user)  # type:ignore
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def create_office(self):
        office = ListPlates.objects.create(name='test')  # type:ignore
        profile = Profile.objects.create(user=self.user, office=office)  # type:ignore
        return profile

    # get all plates
    def test_get_all_plates_status(self):
        response = self.client.get('/plates/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_plates_content(self):
        response = self.client.get('/plates/')
        self.assertEqual(response['content-type'], "application/json")

    # add new plate
    def test_add_plate_status(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 200)

    def test_add_plate_content(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        self.client.post('/plates/add/', data)
        try:
            query = Plate.objects.get(number=data['number'])  # type:ignore
        except Plate.DoesNotExist:  # type:ignore
            query = None
        self.assertIsNotNone(query)

    def test_add_plate_number_small_to_7_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "123456",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 400)

    def test_add_plate_city_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 400)

    def test_add_plate_no_manufac_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 400)

    def test_add_plate_no_model_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 400)

    def test_add_plate_no_year_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 1,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 400)

    def test_add_plate_no_color_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': '',
            'qru': 43
        }
        response = self.client.post('/plates/add/', data)
        self.assertEqual(response.status_code, 400)

    # edit plate
    def test_edit_plate_status(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        plate = Plate.objects.create(
            number='7654321',
            city=data['city'],
            manufacturer=data['manufac'],
            model=data['model'],
            year=data['year'],
            color=data['color'],
            qru=data['qru'],
            post_name=data['post_name']
        )
        reponse = self.client.post(f'/plates/edit={plate.id}/', data)
        self.assertEqual(reponse.status_code, 200)

    def test_edit_plate_content(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        plate = Plate.objects.create(
            number='7654321',
            city=data['city'],
            manufacturer=data['manufac'],
            model=data['model'],
            year=data['year'],
            color=data['color'],
            qru=data['qru'],
            post_name=data['post_name']
        )
        self.client.post('/plates/edit=1/', data)
        try:
            query = Plate.objects.get(number=7654321)
        except Plate.DoesNotExist:  # type:ignore
            query = None
        self.assertIsNotNone(query)

    def test_edit_plate_number_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "123456",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/edit=1/', data)
        self.assertEqual(response.status_code, 300)

    def test_edit_plate_city_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/edit=1/', data)
        self.assertEqual(response.status_code, 300)

    def test_edit_plate_manufac_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "12",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/edit=1/', data)
        self.assertEqual(response.status_code, 300)

    def test_edit_plate_model_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "12",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/edit=1/', data)
        self.assertEqual(response.status_code, 300)

    def test_edit_plate_color_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "manufac",
            "model": "model",
            'year': 2023,
            'color': '123',
            'qru': 43
        }
        response = self.client.post('/plates/edit=1/', data)
        self.assertEqual(response.status_code, 300)

    def test_edit_plate_year_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "12",
            "model": "model",
            'year': 1900,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/edit=1/', data)
        self.assertEqual(response.status_code, 300)

    def test_edit_plate_no_id_error(self):
        data = {
            "post_name": self.profile.office,
            "number": "1234567",
            "city": "city-",
            "manufac": "12",
            "model": "model",
            'year': 2023,
            'color': 'color',
            'qru': 43
        }
        response = self.client.post('/plates/edit=/', data)
        self.assertEqual(response.status_code, 404)

    # delete plate
    def test_delete_plate_status(self):
        plate = Plate.objects.create(
            number="1234567",
            city="city-",
            manufacturer="manufac",
            model="model",
            year=2023,
            color='color',
            qru=43,
            post_name=self.profile.office,
        )
        response = self.client.delete(f'/plates/del={plate.id}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_plate_content(self):
        Plate.objects.create(
            number="1234567",
            city="city-",
            manufacturer="manufac",
            model="model",
            year=2023,
            color='color',
            qru=43,
            post_name=self.profile.office,
        )
        self.client.delete('/plates/del=1/')
        try:
            query = Plate.objects.get(pk=1)  # type:ignore
        except Plate.DoesNotExist:  # type:ignore
            query = None
        self.assertIsNone(query)

    def test_delete_plate_no_id_error(self):
        Plate.objects.create(
            number="1234567",
            city="city-",
            manufacturer="manufac",
            model="model",
            year=2023,
            color='color',
            qru=43,
            post_name=self.profile.office,
        )
        response = self.client.delete('/plates/del=/')
        self.assertEqual(response.status_code, 404)

