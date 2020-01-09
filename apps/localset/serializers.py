from rest_framework import serializers


class HostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ip = serializers.IPAddressField()
    mac = serializers.IPAddressField()
    vendor = serializers.CharField()
    active = serializers.BooleanField(required=False)


class RegisteredHostSerializer(serializers.Serializer):
    DT_RowId = serializers.IntegerField(source="id", read_only=True)
    id = serializers.IntegerField(read_only=True)
    ip = serializers.IPAddressField()
    mac = serializers.IPAddressField()
    hostname = serializers.CharField()
    subnet = serializers.IPAddressField()
    routes = serializers.IPAddressField()
    dns = serializers.IPAddressField()
