from rest_framework import serializers
from buildings.models import Building, BuildingFloorSpace, LtSpaceType
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('id', 'building_name', 'num_floors')


class BuildingFloorSpaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BuildingFloorSpace
        geo_field = "multi_poly"
        fields = ('id', 'short_name', 'floor_num', 'multi_poly', 'fk_building', 'fk_building_floor',
                  'room_external_id', 'space_type')