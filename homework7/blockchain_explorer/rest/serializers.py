from rest_framework import serializers

from .models import Tx, Block


class TxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tx
        fields = ['id', 'from_addr', 'to_addr', 'value', 'timestamp']


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['number', 'txs', 'timestamp']
