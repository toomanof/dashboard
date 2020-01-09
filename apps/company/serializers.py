from rest_framework import serializers

from .models import NetDevices, Departments, Employee


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class NetDevicesSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    employee_name = serializers.CharField(read_only=True)
    host_ip = serializers.CharField(read_only=True)

    class Meta:
        model = NetDevices
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
