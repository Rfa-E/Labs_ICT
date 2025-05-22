# Deliverable Session 04 - Information and Communication Technology

## Rafael Antonio Echevarria Silva

En esta sesión tenemos como objetivo comunicar los sensores del Sense Hat con la Raspberry Pi utilizando Python.

[https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/]

### A. Reading of the sensor information

Tenemos 8 sensores en total en la Raspberry Pi, 3 de ellos ambientales y 5 de medidas internas. Para los tres primeros podemos mirar que funciones hace en la página web anterior en la sección de "Sensing the environment", donde podemos ver ejemplos de como medir la presión, la temperatura y la humedad.

```python
sense.get_pressure()
sense.get_temperature()
sense.get_humidity()
```

Para los 5 sensores IMU, podemos utilizar la sección "Detecting movement" en donde nos explica como funcionan los sensores y como utilizarlos, aparte de que variables son las que retorna al llamar a la función.

```python
sense.get_compass() 
sense.get_compass_raw() #Units (x, y, z) from the magnetometer 
sense.get_gyroscope_raw()
sense.get_accelerometer_raw()
sense.get_orientation()
```
