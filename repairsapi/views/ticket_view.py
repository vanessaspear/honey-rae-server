"""View module for handling requests for ticket data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from repairsapi.models import ServiceTicket


class TicketView(ViewSet):
    """Honey Rae API tickets view"""

    def list(self, request):
        """Handle GET requests to get all tickets

        Returns:
            Response -- JSON serialized list of tickets
        """

        tickets = ServiceTicket.objects.all()
        serialized = TicketSerializer(tickets, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single ticket

        Returns:
            Response -- JSON serialized ticket record
        """

        ticket = ServiceTicket.objects.get(pk=pk)
        serialized = TicketSerializer(ticket, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class TicketSerializer(serializers.ModelSerializer):
    """JSON serializer for tickets"""
    class Meta:
        model = ServiceTicket
        fields = ('id', 'description', 'emergency', 'date_completed', 'customer_id', 'employee_id')