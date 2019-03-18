# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from .views import TeamMemberList, TeamMemberDetail
from .models import TeamMember
from .serializers import TeamMemberSerializer
from rest_framework.renderers import JSONRenderer


class TeamAPITest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.team_member = TeamMember.objects.create(
            first_name='Ellie', last_name='Ellington',
            email='ellie.ellington@ellie.com', phone_number='1390539393',
            admin_role=True)
        self.incorrect_pk = 999

    def test_list(self):
        request = self.factory.get('/team_members/')
        response = TeamMemberList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_list_failure(self):
        """
        NOTE: Using client for this test because factory returned 200
        """
        response = self.client.get('/team_member/')
        self.assertEqual(response.status_code, 404)

    def test_put_team_member(self):
        self.team_member.phone = 357685797
        self.team_member.admin_role = False
        serializer = TeamMemberSerializer(self.team_member)
        content = JSONRenderer().render(serializer.data)
        request = self.factory.put('/team_members/', data=content,
                                   content_type='application/json')
        response = TeamMemberDetail.as_view()(request, pk=self.team_member.pk)
        self.assertEqual(response.status_code, 200)

    def test_put_team_member_failure(self):
        serializer = TeamMemberSerializer(self.team_member)
        content = JSONRenderer().render(serializer.data)
        request = self.factory.put('/team_members/', data=content,
                                   content_type='application/json')
        response = TeamMemberDetail.as_view()(request, pk=self.incorrect_pk)
        self.assertEqual(response.status_code, 404)

    def test_post_team_member(self):
        data = {
            'first_name': 'Pika', 
            'last_name': 'Chu',
            'email': 'pika.chu@pokeball.com', 
            'phone_number': '4578435688',
            'admin_role': False
        }
        content = JSONRenderer().render(data)
        request = self.factory.post('/team_members/', data=content,
                                    content_type='application/json')
        response = TeamMemberList.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_post_team_member_failure_incorrect_content(self):
        """
        'first' should be 'first_name'
        'last' should be 'last_name'
        """
        data = {
            'first': 'Pika', 
            'last': 'Chu',
            'email': 'pika.chu@pokeball.com', 
            'phone_number': '4578435688',
            'admin_role': False
        }
        content = JSONRenderer().render(data)
        request = self.factory.post('/team_members/', data=content,
                                    content_type='application/json')
        response = TeamMemberList.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_post_team_member_failure_missing_content(self):
        """
        Missing 'first_name' and 'last_name fields'
        """
        data = {
            'email': 'pika.chu@pokeball.com', 
            'phone_number': '4578435688',
            'admin_role': False
        }
        content = JSONRenderer().render(data)
        request = self.factory.post('/team_members/', data=content,
                                    content_type='application/json')
        response = TeamMemberList.as_view()(request)
        self.assertEqual(response.status_code, 400)

    def test_delete_team_member(self):
        request = self.factory.delete('/team_members/')
        response = TeamMemberDetail.as_view()(request, pk=self.team_member.pk)
        self.assertEqual(response.status_code, 204)

    def test_delete_team_member_failure(self):
        request = self.factory.delete('/team_members/')
        response = TeamMemberDetail.as_view()(request, pk=self.incorrect_pk)
        self.assertEqual(response.status_code, 404)
