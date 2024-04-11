from abc import ABC, abstractmethod


class Sensor(ABC):
    sensor_id: str

    @abstractmethod
    def read_data(self) -> None:
        ...


class TemperatureSensor(Sensor):
    __slots__ = ('__temperature', '__spatial_distribution')
    sensor_id = '232424142'

    def __init__(self, temperature: float, spatial_distribution: str) -> None:
        self.temperature = temperature
        self.spatial_distribution = spatial_distribution
        self.__sensor_id = ''

    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        if isinstance(value, float):
            self.__temperature = value

    @property
    def spatial_distribution(self) -> str:
        return self.__spatial_distribution

    @spatial_distribution.setter
    def spatial_distribution(self, value: str) -> None:
        if isinstance(value, str):
            self.__spatial_distribution = value

    def read_data(self)->str:
        self.sensor_id = TemperatureSensor.sensor_id
        print('Temperature Sensor has an id of ',self.sensor_id)


class HumiditySensor(Sensor):
    __slots__ = ('__humidity', '__location')
    sensor_id = '3123131313'

    def __init__(self, humidity: int, location: str) -> None:
        self.humidity = humidity
        self.location = location
        self.sensor_id = ''

    @property
    def humidity(self) -> int:
        return self.__humidity

    @humidity.setter
    def humidity(self, value: int) -> None:
        self.__humidity = value

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        self.__location = value

    def read_data(self) -> str:
        self.sensor_id = HumiditySensor.sensor_id
        print('humidity sensor has an id of ',self.sensor_id)

class LightSensor(Sensor):
    __slots__ = ('__light_intensity')
    sensor_id = '32321313131'

    def __init__(self, light_intensity: int) -> None:
        self.light_intensity = light_intensity
        self.sensor_id = ''

    @property
    def light_intensity(self) -> int:
        return self.__light_intensity

    @light_intensity.setter
    def light_intensity(self, value: int) -> None:
        self.__light_intensity = value

    def read_data(self)->str:
        self.sensor_id = LightSensor.sensor_id
        print('light sensor has an id of ',self.sensor_id)


class SensorManager:
    __slots__ = ('__sensors')

    def __init__(self, sensors: list[Sensor]) -> None:
        self.__sensors = sensors

    @property
    def sensors(self):
        return self.__sensors

    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)

    def remove_sensor(self, sensor: Sensor) -> None:
        self.sensors.remove(sensor)

    def read_from_sensors(self):
        for i in self.sensors:
            i.read_data()

temp_sensor=TemperatureSensor(37.5,'warmer near windows')
humid_sensor=HumiditySensor(1000,'US')
light_sensor=LightSensor(2000)

sensor_manager=SensorManager([temp_sensor,humid_sensor,light_sensor])
sensor_manager.add_sensor(LightSensor(3000))

print(sensor_manager.sensors)
sensor_manager.remove_sensor(light_sensor)
print(sensor_manager.sensors)
sensor_manager.read_from_sensors()