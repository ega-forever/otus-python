from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tx, Block
from .serializers import TxSerializer, BlockSerializer


@api_view(['GET'])
def index(request):
    return Response({"status": "ok"})


@api_view(['GET'])
def get_txes(request):
    txs = Tx.objects.all()
    txs_count = Tx.objects.count()

    serialized = TxSerializer(txs, many=True)

    return Response({
        "items": serialized.data,
        "count": txs_count
    })

@api_view(['GET'])
def get_blocks(request):
    blocks = Block.objects.all()
    blocks_count = Block.objects.count()

    serialized = BlockSerializer(blocks, many=True)

    return Response({
        "items": serialized.data,
        "count": blocks_count
    })
