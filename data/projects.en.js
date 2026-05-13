window.PROJECTS = [
    {
        "id":  1,
        "name":  "STM32-based pH detection system",
        "description":  "Real-time liquid pH monitoring, display and alarm extension.",
        "tech":  "pH sensor, STM32F103, OLED, buzzer",
        "access":  "Paid access"
    },
    {
        "id":  2,
        "name":  "STM32 multi-parameter environment monitoring system",
        "description":  "Collects pressure and humidity data, displays readings and supports key and motor control.",
        "tech":  "STM32F103, pressure sensor, humidity sensor, keys, OLED, motor driver, LED",
        "access":  "Paid access"
    },
    {
        "id":  3,
        "name":  "Microcontroller smart water heater temperature control system",
        "description":  "Automatic heating, constant-temperature control, OLED display and key operation.",
        "tech":  "Development board, OLED, keys, LED, heating module",
        "access":  "Paid access"
    },
    {
        "id":  4,
        "name":  "STM32 timer-based digital clock",
        "description":  "Uses timers for time keeping and implements a basic digital clock display.",
        "tech":  "Timer, OLED, keys, LED",
        "access":  "Paid access"
    },
    {
        "id":  5,
        "name":  "STM32 WiFi IoT smart clock",
        "description":  "Adds WiFi time synchronization and remote control to a digital clock.",
        "tech":  "Timer, WiFi module, OLED, keys",
        "access":  "Paid access"
    },
    {
        "id":  6,
        "name":  "STM32 serial communication data transceiver",
        "description":  "Sends and receives serial data for device communication tests and debugging.",
        "tech":  "Serial module, development board",
        "access":  "Paid access"
    },
    {
        "id":  7,
        "name":  "STM32 CubeMX DC voltage detection system",
        "description":  "Uses a development board and CubeMX configuration to detect and report DC voltage through serial communication.",
        "tech":  "ALIENTEK NANO, STM32F4, CubeMX, serial port",
        "access":  "Paid access"
    },
    {
        "id":  8,
        "name":  "STM32 voice-recognition smart information display",
        "description":  "Controls OLED display content through voice commands.",
        "tech":  "STM32F103RCT6, LD3320A, 7-pin OLED, SPI",
        "access":  "Paid access"
    },
    {
        "id":  9,
        "name":  "STM32 electronic password lock",
        "description":  "Runs password verification on an embedded board and supports host-side unlocking logic.",
        "tech":  "PC decoding, Wildfire board, F103C8, potentiometer, smoke sensor",
        "access":  "Paid access"
    },
    {
        "id":  10,
        "name":  "STM32 ambient light and temperature-humidity sensing system",
        "description":  "Uses a potentiometer and smoke sensor to monitor environmental states.",
        "tech":  "F103C8, potentiometer, smoke sensor",
        "access":  "Paid access"
    },
    {
        "id":  11,
        "name":  "STM32 multi-sensor air quality monitor",
        "description":  "Integrates multiple gas sensors for harmful gas detection.",
        "tech":  "STM32F103, MQ4, MQ5, ESP01S, fan, OLED",
        "access":  "Paid access"
    },
    {
        "id":  12,
        "name":  "STM32 multi-position servo control system",
        "description":  "Controls six servos for multi-degree-of-freedom motion, suitable for robots or robotic arms.",
        "tech":  "STM32F103C8T6, MG90S, serial module, PWM, keys",
        "access":  "Paid access"
    },
    {
        "id":  13,
        "name":  "STM32 dual-channel DAC/PWM signal output system",
        "description":  "Generates analog output and PWM signals for waveform and motor-control experiments.",
        "tech":  "F103, dual DAC, dual PWM, keys",
        "access":  "Paid access"
    },
    {
        "id":  14,
        "name":  "STM32 Bluetooth stepper motor remote control system",
        "description":  "Controls a stepper motor through Bluetooth APP and integrates temperature, humidity, weight and LED display.",
        "tech":  "F103, stepper motor, HC-05, LEDs, OLED, DHT11, HX711, buttons, Bluetooth APP",
        "access":  "Paid access"
    },
    {
        "id":  15,
        "name":  "Infrared remote dual-motor speed control system",
        "description":  "Uses infrared remote control for independent control of two servos or motors.",
        "tech":  "F103, ASR board, OLED, two servos, infrared switch",
        "access":  "Paid access"
    },
    {
        "id":  16,
        "name":  "STM32 Aliyun greenhouse environment monitoring system",
        "description":  "Collects temperature, humidity, pressure and light data and uploads it for cloud visualization.",
        "tech":  "STM32F103, ESP01S, temperature/humidity, pressure, light, OLED, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  17,
        "name":  "STM32 four-axis robot servo control system",
        "description":  "Controls a four-axis robot and connects to a mini-program for interaction.",
        "tech":  "ESP32C3, four-axis robot, mini-program",
        "access":  "Paid access"
    },
    {
        "id":  18,
        "name":  "STM32 multi-vital-sign monitoring system",
        "description":  "Collects GPS, heart rate, SpO2, motion and temperature-humidity data.",
        "tech":  "NEO-6M GPS, MAX30102, MPU6050, buzzer, DHT11",
        "access":  "Paid access"
    },
    {
        "id":  19,
        "name":  "Smart agriculture scheduled irrigation control system",
        "description":  "Detects soil moisture, light intensity and time data to control irrigation automatically.",
        "tech":  "PCB, dual MCU, WiFi, soil moisture, light, DS18B20, water pump, relay, RTC",
        "access":  "Paid access"
    },
    {
        "id":  20,
        "name":  "Infrared remote automatic curtain control system",
        "description":  "Controls curtain opening and closing with infrared remote control, temperature-humidity sensing and voice broadcast.",
        "tech":  "Curtain model, F1 board, 1838 IR, stepper motor, DHT11, light sensor, keys, JQ8900",
        "access":  "Paid access"
    },
    {
        "id":  21,
        "name":  "STM32 fingerprint Bluetooth access control system",
        "description":  "Uses fingerprint recognition and Bluetooth communication for secure identity verification and remote control.",
        "tech":  "F103, AS608 fingerprint, HC-05, DHT11, buzzer, OLED",
        "access":  "Paid access"
    },
    {
        "id":  22,
        "name":  "STM32 voice-triggered safety alarm system",
        "description":  "Provides voice prompts and alarms with light, water level and infrared detection.",
        "tech":  "F103, JQ8900, water level module, light module, IR module, LED",
        "access":  "Paid access"
    },
    {
        "id":  23,
        "name":  "STM32 wearable multi-vital-sign wristband",
        "description":  "Integrates heart rate, SpO2, temperature, smoke and motion sensing for health monitoring.",
        "tech":  "F103, OneNET, MAX30102, DS18B20, smoke sensor, OLED, MPU6050, ESP01S",
        "access":  "Paid access"
    },
    {
        "id":  24,
        "name":  "STM32 RTOS real-time environment monitoring system",
        "description":  "Uses RT-Thread to manage multiple monitoring tasks for efficient data collection and processing.",
        "tech":  "F103, RT-Thread, MQ2, DHT11, buzzer, ESP01S, NEO-6M GPS",
        "access":  "Paid access"
    },
    {
        "id":  25,
        "name":  "STM32 modular embedded system program design",
        "description":  "Shows a complete embedded development process with system framework and program flowcharts.",
        "tech":  "F103, strain gauge, OLED, Visio system diagrams, flowcharts",
        "access":  "Paid access"
    },
    {
        "id":  26,
        "name":  "STM32 cloud-based smart agriculture remote monitoring system",
        "description":  "Connects a WeChat mini-program and OneNET to monitor soil, light and water remotely.",
        "tech":  "STM32, UniApp, mini-program, OneNET, sensors, relay, Hall voltage module",
        "access":  "Paid access"
    },
    {
        "id":  27,
        "name":  "STM32 infrared flame detection and automatic alarm system",
        "description":  "Combines infrared and smoke sensors for fire warning and alarm control.",
        "tech":  "F103, E18-D80NK, OLED, JQ8900, HC-05, flame sensor, APP, relay",
        "access":  "Paid access"
    },
    {
        "id":  28,
        "name":  "STM32 smart water flow metering and control system",
        "description":  "Detects water level, turbidity and pH, and supports cloud remote monitoring.",
        "tech":  "F103, OneNET, UniApp, pump, DS18B20, pH, turbidity, buzzer, OLED",
        "access":  "Paid access"
    },
    {
        "id":  29,
        "name":  "STM32 automatic pet feeder and environment monitor",
        "description":  "Performs scheduled feeding and monitors pet environment through wind and gas sensors with cloud access.",
        "tech":  "F103, wind sensor, MQ4, MQ7, ESP01S, DHT11, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  30,
        "name":  "STM32 smart pet feeding and environment monitoring system",
        "description":  "Combines feeding, gas, light, sound and actuator modules for pet environment management.",
        "tech":  "F103, keys, ESP01S, Aliyun, DHT11, OLED, MQ2, buzzer, IR, JQ8900, SG90",
        "access":  "Paid access"
    },
    {
        "id":  31,
        "name":  "STM32 OneNET dust concentration monitoring system",
        "description":  "Collects dust, temperature-humidity and light data and uploads it to OneNET.",
        "tech":  "F103, ESP01S, MPU6050, AT24CXX, EEPROM, DS18B20, buzzer, pressure sensor",
        "access":  "Paid access"
    },
    {
        "id":  32,
        "name":  "STM32 multi-source indoor environment monitoring system",
        "description":  "Integrates dust, temperature, light, voice, fan and servo modules for linked control.",
        "tech":  "F103, UniApp, Android APP, ESP01S, ZPH01, MLX90614, JQ8900, OneNET, fan, SG90, OLED",
        "access":  "Paid access"
    },
    {
        "id":  33,
        "name":  "STM32 voice-recognition smart home control terminal",
        "description":  "Uses voice commands to control lights, fans, motors and display modules.",
        "tech":  "OLED, TTS, ESP01S, DHT11, Aliyun, JQ8900, light sensor, speaker",
        "access":  "Paid access"
    },
    {
        "id":  34,
        "name":  "STM32 offline voice smart device control system",
        "description":  "Optimizes and extends a smart device control system for better stability and practicality.",
        "tech":  "Smart car, F103, OLED, MQ2, DHT11, flame sensor, ESP01S, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  35,
        "name":  "STM32 HAL local voice recognition system",
        "description":  "Uses HAL and CubeMX for WiFi connection, voice recognition and PIR detection.",
        "tech":  "HAL, CubeMX, OLED, WiFi, Aliyun, ASRPRO, HC-05, PWM light, PIR, keys",
        "access":  "Paid access"
    },
    {
        "id":  36,
        "name":  "STM32 Aliyun indoor CO2 monitoring system",
        "description":  "Collects CO2, temperature, humidity and light data and supports APP remote viewing.",
        "tech":  "F103, light sensor, JW01 CO2 sensor, DHT11, ESP01S, Aliyun, APP",
        "access":  "Paid access"
    },
    {
        "id":  37,
        "name":  "STM32 pedometer with three-axis sensor",
        "description":  "Uses step counting and GPS to record movement traces and health data.",
        "tech":  "F103, MPU6050, step algorithm, fall detection, NEO-6M, DS18B20, ESP01S, MAX30102, OneNET",
        "access":  "Paid access"
    },
    {
        "id":  38,
        "name":  "STM32 smart agricultural greenhouse monitoring system",
        "description":  "Monitors pH, TDS, soil moisture, water temperature and cloud communication.",
        "tech":  "STM32, pH, TDS, soil moisture, DS18B20, ESP01S, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  39,
        "name":  "STM32 Aliyun indoor air quality monitor",
        "description":  "Detects PM2.5, methanol, formaldehyde, CO2 and temperature-humidity with cloud upload.",
        "tech":  "Development board, LCD, gas sensors, SP30 CO2, DHT11, ESP01S, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  40,
        "name":  "STM32 voice-recognition smart sorting bin",
        "description":  "Uses voice commands to control a smart bin, with light and smoke sensing.",
        "tech":  "Smart car base, servo bin, ASRPRO, L298N, HC-05, light sensor",
        "access":  "Paid access"
    },
    {
        "id":  41,
        "name":  "STM32 distributed smart environment monitoring node",
        "description":  "Collects temperature, smoke, light and display data with cloud upload and remote monitoring.",
        "tech":  "STM32F103, DHT11, MQ2, SR06 IR, ESP01S, OLED, Aliyun, buzzer, LED",
        "access":  "Paid access"
    },
    {
        "id":  42,
        "name":  "STM32 OneNET agricultural greenhouse monitoring system",
        "description":  "Collects light, soil moisture and water level data and uploads it to OneNET.",
        "tech":  "F103, DHT11, light, soil moisture, OneNET, UniApp, ESP01S, JW01",
        "access":  "Paid access"
    },
    {
        "id":  43,
        "name":  "Smart fish tank scheduled feeding and circulation system",
        "description":  "Handles scheduled feeding, water level control, PVC heating and buzzer alarms.",
        "tech":  "F103, relay pump, ESP01S, PVC heating, buzzer, OLED, Aliyun, DS18B20, turbidity, stepper motor",
        "access":  "Paid access"
    },
    {
        "id":  44,
        "name":  "STM32 alcohol detection and alarm system",
        "description":  "Detects alcohol concentration and shows alarm status through OLED and buzzer.",
        "tech":  "F103C6T6, MQ3, buzzer, OLED, report",
        "access":  "Paid access"
    },
    {
        "id":  45,
        "name":  "STM32 supermarket entrance people counting and anti-theft system",
        "description":  "Implements line tracking, ultrasonic obstacle avoidance, Bluetooth control and PC GUI display.",
        "tech":  "STM32 car, IR tracking, ultrasonic, Bluetooth, PCB, report",
        "access":  "Paid access"
    },
    {
        "id":  46,
        "name":  "Infrared learning universal remote controller",
        "description":  "Uses IR and CH340 serial communication, with a Python script for PC volume/control actions.",
        "tech":  "F103, Python PC tool, HC-05, APP, CH340 serial board",
        "access":  "Paid access"
    },
    {
        "id":  47,
        "name":  "STM32 ultrasonic ranging and environment application system",
        "description":  "Combines ultrasonic ranging, smoke, temperature, WiFi and cloud functions.",
        "tech":  "F103, MQ2, DHT11, ultrasonic sensor, ESP01S, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  48,
        "name":  "STM32 smart security monitoring node",
        "description":  "Supports local and remote control with PIR, WiFi and cloud platforms.",
        "tech":  "F103, HCSR501, ESP01S, Aliyun, OneNET, UniApp, Android APP",
        "access":  "Paid access"
    },
    {
        "id":  49,
        "name":  "STM32 smart air purifier control system",
        "description":  "Monitors TVOC, CO2, formaldehyde, light and water level and controls fan, pump and heater.",
        "tech":  "STM32F1, ESP01S, TVOC, CO2, JW01, DHT11, Aliyun APP, pump, buzzer, fan, heater",
        "access":  "Paid access"
    },
    {
        "id":  50,
        "name":  "STM32 Bluetooth smart LED dimming system",
        "description":  "Uses a mobile APP to control lighting, fan, sensors and cloud-linked thresholds.",
        "tech":  "F103, stepper motor, L9110 fan, DHT11, ESP01S, Aliyun, relay pump, OLED, buzzer, JW01",
        "access":  "Paid access"
    },
    {
        "id":  51,
        "name":  "STM32 adaptive light adjustment system",
        "description":  "Implements light sensing, filtering, smoke detection and cloud upload.",
        "tech":  "F103, light control circuit, ESP01S, Aliyun, MQ2, DHT11",
        "access":  "Paid access"
    },
    {
        "id":  52,
        "name":  "STM32 MPU6050 motion health wristband",
        "description":  "Performs attitude calculation, complementary filtering, OLED display and cloud upload.",
        "tech":  "F103, MAX30102, MPU6050, Mahony filter, OLED, DS18B20, ESP01S, Aliyun",
        "access":  "Paid access"
    },
    {
        "id":  53,
        "name":  "STM32 JW01 formaldehyde detector",
        "description":  "Collects gas and temperature-humidity data and displays it through an STM32 system.",
        "tech":  "JW01 gas sensor, DHT11, STM32F103 board",
        "access":  "Paid access"
    },
    {
        "id":  54,
        "name":  "STM32 WiFi APP smart home environment monitor",
        "description":  "Collects temperature, humidity, smoke and light data and controls fan and relay through a mobile APP.",
        "tech":  "OLED, DHT11, MQ2, light sensor, relay, WiFi APP",
        "access":  "Paid access"
    },
    {
        "id":  55,
        "name":  "STM32 ADC voltage acquisition and ultrasonic ranging system",
        "description":  "Provides key control, ADC voltage sampling and ultrasonic distance measurement.",
        "tech":  "STM32, ADC, HC-SR04, keys",
        "access":  "Paid access"
    },
    {
        "id":  56,
        "name":  "STM32 SIM remote data transmission system",
        "description":  "Links STM32 with a SIM module for SMS alarms, remote collection or IoT communication.",
        "tech":  "SIM module, STM32, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  57,
        "name":  "SHT31 indoor temperature-humidity monitor",
        "description":  "Collects temperature and humidity data and communicates through IIC.",
        "tech":  "SHT31, IIC, STM32",
        "access":  "Paid access"
    },
    {
        "id":  58,
        "name":  "Infrared and light sensor environment display system",
        "description":  "Detects infrared events and light level and displays data on OLED.",
        "tech":  "IR sensor, light sensor, OLED, STM32",
        "access":  "Paid access"
    },
    {
        "id":  59,
        "name":  "STM32 three-channel ADC and PSD ranging system",
        "description":  "Performs multi-channel analog acquisition and distance measurement.",
        "tech":  "ADC, PSD distance sensor, STM32",
        "access":  "Paid access"
    },
    {
        "id":  60,
        "name":  "AD5933 impedance measurement and analysis system",
        "description":  "Measures, processes and displays impedance parameters for material or bio-impedance scenarios.",
        "tech":  "AD5933, IIC, STM32, impedance measurement",
        "access":  "Paid access"
    },
    {
        "id":  61,
        "name":  "STM32F407 multi-attitude and eight-channel data acquisition system",
        "description":  "Integrates attitude sensors and multi-channel ADC acquisition for motion and analog signal monitoring.",
        "tech":  "STM32F407, MPU6050, 8-channel ADC",
        "access":  "Paid access"
    },
    {
        "id":  62,
        "name":  "OneNET cloud temperature-humidity IoT monitor",
        "description":  "Uploads environmental data to a cloud platform through MQTT.",
        "tech":  "OneNET, MQTT, DHT11, STM32",
        "access":  "Paid access"
    },
    {
        "id":  63,
        "name":  "STM32 multifunction environment monitoring and interaction system",
        "description":  "Integrates display, clock, storage, serial communication and temperature-humidity acquisition.",
        "tech":  "TFTLCD, RTC, EEPROM, DHT11, serial port",
        "access":  "Paid access"
    },
    {
        "id":  64,
        "name":  "STM32 low-power data acquisition and Flash storage system",
        "description":  "Supports AD acquisition, low-power operation and local Flash data storage.",
        "tech":  "ADC, Flash, low power, STM32",
        "access":  "Paid access"
    },
    {
        "id":  65,
        "name":  "STM32 dual-DAC output and ADC acquisition system",
        "description":  "Provides two-channel analog output and input acquisition for signal generation and capture.",
        "tech":  "DAC, ADC, STM32",
        "access":  "Paid access"
    },
    {
        "id":  66,
        "name":  "Serial-controlled 42 stepper motor driver system",
        "description":  "Controls stepper motor direction, speed and angle through serial commands.",
        "tech":  "42 stepper motor, serial port, STM32",
        "access":  "Paid access"
    },
    {
        "id":  67,
        "name":  "PC-based serial temperature-humidity monitoring system",
        "description":  "Uploads sensor data from the MCU to a PC for real-time display and review.",
        "tech":  "DHT11, serial communication, PC software, STM32",
        "access":  "Paid access"
    },
    {
        "id":  68,
        "name":  "STM32 dual-ADC acquisition and stepper motor control system",
        "description":  "Combines dual-channel sampling with motor control.",
        "tech":  "ADC, stepper motor, STM32",
        "access":  "Paid access"
    },
    {
        "id":  69,
        "name":  "STM32 integrated light, servo and motor control system",
        "description":  "Controls LED, servo and DC motor linkage for smart car or actuator demos.",
        "tech":  "LED, servo, motor, PWM",
        "access":  "Paid access"
    },
    {
        "id":  70,
        "name":  "LM386 sound signal acquisition and analysis system",
        "description":  "Samples audio analog signals through ADC for noise or sound-control applications.",
        "tech":  "LM386, ADC, STM32",
        "access":  "Paid access"
    },
    {
        "id":  71,
        "name":  "Multi-sensor indoor environment safety monitor",
        "description":  "Collects temperature, humidity and smoke concentration and supports alarm expansion.",
        "tech":  "DS18B20, DHT11, MQ2, STM32",
        "access":  "Paid access"
    },
    {
        "id":  72,
        "name":  "STM32 temperature, smoke, flame and voice alarm system",
        "description":  "Detects temperature, smoke and flame and drives stepper motor and voice alarm modules.",
        "tech":  "Temperature sensor, MQ2, flame sensor, ULN2003, voice module",
        "access":  "Paid access"
    },
    {
        "id":  73,
        "name":  "STM32 16-channel ADC data acquisition system",
        "description":  "Performs multi-channel analog signal acquisition for industrial or lab data logging.",
        "tech":  "16-channel ADC, STM32",
        "access":  "Paid access"
    },
    {
        "id":  74,
        "name":  "STM32F4 formaldehyde gas detection and Bluetooth transmission system",
        "description":  "Collects formaldehyde data and sends it through Bluetooth.",
        "tech":  "STM32F4, formaldehyde sensor, HC-06",
        "access":  "Paid access"
    },
    {
        "id":  75,
        "name":  "Ultrasonic distance measurement system",
        "description":  "Measures distance for obstacle avoidance, liquid level or ranging scenarios.",
        "tech":  "IOE-SR05, STM32, timer",
        "access":  "Paid access"
    },
    {
        "id":  76,
        "name":  "STM32 ultraviolet detection and temperature-control actuator system",
        "description":  "Displays data on OLED, indicates states with LEDs and controls heating/cooling.",
        "tech":  "OLED, UV sensor, LED, heating/cooling module",
        "access":  "Paid access"
    },
    {
        "id":  77,
        "name":  "STM32F407 smart lighting and environment sensing control system",
        "description":  "Uses infrared, ultrasonic and light sensing with PWM LED brightness control.",
        "tech":  "STM32F407, IR sensor, ultrasonic, LDR, PWM",
        "access":  "Paid access"
    },
    {
        "id":  78,
        "name":  "STM32 PC clock, alarm and OLED display system",
        "description":  "Implements RTC clock, alarm settings, serial communication and OLED interaction.",
        "tech":  "DS1302, OLED, CH340, PC software",
        "access":  "Paid access"
    },
    {
        "id":  79,
        "name":  "MAX30102 heart rate and SpO2 acquisition with OLED waveform",
        "description":  "Collects heart rate and SpO2 data and displays waveform and parameters on OLED.",
        "tech":  "MAX30102, OLED, STM32",
        "access":  "Paid access"
    },
    {
        "id":  80,
        "name":  "PC-based 18-channel data acquisition and visualization system",
        "description":  "Uploads multi-channel data through serial communication for PC visualization.",
        "tech":  "18-channel acquisition, serial port, PC software",
        "access":  "Paid access"
    },
    {
        "id":  81,
        "name":  "Electric energy metering and monitoring system",
        "description":  "Collects voltage, current and power data for energy monitoring and analysis.",
        "tech":  "Energy metering module, STM32, serial port",
        "access":  "Paid access"
    },
    {
        "id":  82,
        "name":  "Load-cell electronic scale measurement system",
        "description":  "Acquires, filters and displays weight data.",
        "tech":  "Load cell, ADC, STM32",
        "access":  "Paid access"
    },
    {
        "id":  83,
        "name":  "Relay timer and power calculation system",
        "description":  "Controls timed relay switching and calculates load runtime or energy data.",
        "tech":  "Relay, timer, power calculation, STM32",
        "access":  "Paid access"
    },
    {
        "id":  84,
        "name":  "Voice-interactive stepper motor and OLED system",
        "description":  "Controls stepper motor actions through a voice module and displays status on OLED.",
        "tech":  "Voice module, OLED, stepper motor, SRF06",
        "access":  "Paid access"
    },
    {
        "id":  85,
        "name":  "STM32 elevator environment sensing and servo control system",
        "description":  "Simulates elevator environment detection and door control using PIR, temperature-humidity and servo.",
        "tech":  "SG90, DHT11, OLED, PIR sensor",
        "access":  "Paid access"
    },
    {
        "id":  86,
        "name":  "OneNET multi-sensor smart environment monitoring system",
        "description":  "Uploads temperature, smoke, light and flame data to the cloud and supports relay linkage.",
        "tech":  "OneNET, DHT11, MQ2, light sensor, flame sensor, relay",
        "access":  "Paid access"
    },
    {
        "id":  87,
        "name":  "STM32F4 health monitoring and attitude detection system",
        "description":  "Integrates heart rate, SpO2, attitude detection and OLED display.",
        "tech":  "STM32F4, MAX30102, MPU6050, OLED",
        "access":  "Paid access"
    },
    {
        "id":  88,
        "name":  "APP-controlled smart water level and voice actuator system",
        "description":  "Links APP control with water level detection, voice prompt and servo action.",
        "tech":  "STM32F407, APP, voice module, water level sensor, SG90",
        "access":  "Paid access"
    },
    {
        "id":  89,
        "name":  "STM32 SD card data storage and file management system",
        "description":  "Reads and writes SD card data for offline data logging and file management.",
        "tech":  "SD card, SPI, STM32",
        "access":  "Paid access"
    },
    {
        "id":  90,
        "name":  "PC-based four-channel ADC data visualization system",
        "description":  "Samples four analog channels and displays waveforms and values on a PC.",
        "tech":  "Four-channel ADC, serial port, PC software, STM32",
        "access":  "Paid access"
    },
    {
        "id":  91,
        "name":  "LCD1602 multi-parameter environment alarm system",
        "description":  "Collects temperature-humidity, liquid level and pressure data with buzzer alarm.",
        "tech":  "LCD1602, sensors, buzzer",
        "access":  "Paid access"
    },
    {
        "id":  92,
        "name":  "MPU6050 and ESP01S wireless attitude monitoring system",
        "description":  "Collects attitude data and transmits it wirelessly with OLED status display.",
        "tech":  "MPU6050, ESP01S, OLED, STM32",
        "access":  "Paid access"
    },
    {
        "id":  93,
        "name":  "STM32 smart dormitory environment monitoring system",
        "description":  "Collects dormitory environment data, controls devices and displays system status for smart-home style projects.",
        "tech":  "STM32, sensors, OLED, relay",
        "access":  "Paid access"
    },
    {
        "id":  94,
        "name":  "STM32 smart voice garbage bin system",
        "description":  "Implements voice interaction, automatic lid opening and status prompts.",
        "tech":  "Voice module, servo, sensors, STM32",
        "access":  "Paid access"
    },
    {
        "id":  95,
        "name":  "STM32 aquaculture environment monitoring and control system",
        "description":  "Monitors aquaculture environment and controls alarms and actuators.",
        "tech":  "Water level/environment sensors, relay, STM32",
        "access":  "Paid access"
    },
    {
        "id":  96,
        "name":  "STM32 sound-aware environment monitoring system",
        "description":  "Combines sound detection and environmental sensing for security or abnormal-sound alarms.",
        "tech":  "Sound sensor, STM32, OLED",
        "access":  "Paid access"
    },
    {
        "id":  97,
        "name":  "PC-based five-channel ADC data acquisition system",
        "description":  "Performs five-channel sampling and real-time PC curve display.",
        "tech":  "Five-channel ADC, STM32, PC software",
        "access":  "Paid access"
    },
    {
        "id":  98,
        "name":  "Matrix sensor network PC monitoring system",
        "description":  "Collects matrix sensor data and manages it through serial communication and PC visualization.",
        "tech":  "Matrix acquisition, PC software, STM32",
        "access":  "Paid access"
    },
    {
        "id":  99,
        "name":  "STM32F4 HC-05 Bluetooth communication control system",
        "description":  "Implements Bluetooth communication for mobile control and wireless data transmission.",
        "tech":  "HC-05, STM32F4, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  100,
        "name":  "STM32 digital oscilloscope",
        "description":  "Samples analog signals, displays waveforms and analyzes basic parameters.",
        "tech":  "ADC, timer, OLED/LCD, STM32",
        "access":  "Paid access"
    },
    {
        "id":  101,
        "name":  "STM32 ADC-DAC digital filtering experiment platform",
        "description":  "Performs signal acquisition, DAC output and FIR/IIR digital filtering.",
        "tech":  "ADC, DAC, FIR, IIR, STM32",
        "access":  "Paid access"
    },
    {
        "id":  102,
        "name":  "RS485 industrial data acquisition system",
        "description":  "Uses ADC acquisition, timer trigger, DMA transmission and RS485 communication.",
        "tech":  "ADC, DMA, RS485, STM32",
        "access":  "Paid access"
    },
    {
        "id":  103,
        "name":  "STM32 frequency meter and square-wave acquisition system",
        "description":  "Measures square-wave frequency and displays signal parameters.",
        "tech":  "Frequency meter, timer, ADC, STM32",
        "access":  "Paid access"
    },
    {
        "id":  104,
        "name":  "TCS3200 color recognition and serial display system",
        "description":  "Reads color sensor data and outputs recognition results through serial communication.",
        "tech":  "TCS3200, serial port, STM32",
        "access":  "Paid access"
    },
    {
        "id":  105,
        "name":  "LD3322 voice recognition control system",
        "description":  "Provides offline voice recognition for embedded control scenarios.",
        "tech":  "LD3322, STM32, voice recognition",
        "access":  "Paid access"
    },
    {
        "id":  106,
        "name":  "RGB lighting PC control system",
        "description":  "Sends PC commands to control RGB LED color and brightness.",
        "tech":  "RGB LED, serial port, PC software, PWM",
        "access":  "Paid access"
    },
    {
        "id":  107,
        "name":  "HC-SR501 PIR security system",
        "description":  "Detects human infrared signals and triggers alarms or relay actions.",
        "tech":  "HC-SR501, relay, STM32",
        "access":  "Paid access"
    },
    {
        "id":  108,
        "name":  "STM32 servo-controlled electromagnetic launch experiment platform",
        "description":  "Uses servo angle control with an electromagnetic launch structure for experiments.",
        "tech":  "STM32, servo, electromagnetic launch module",
        "access":  "Paid access"
    },
    {
        "id":  109,
        "name":  "STM32 smart home environment monitoring and APP remote control system",
        "description":  "Collects temperature-humidity and flame data and supports mobile APP remote viewing and control.",
        "tech":  "STM32, WiFi module, DHT11, flame sensor, APP",
        "access":  "Paid access"
    },
    {
        "id":  110,
        "name":  "STM32 SIM remote alarm and data reporting system",
        "description":  "Uses a SIM module for remote SMS/network communication and unattended alarms.",
        "tech":  "STM32, SIM module, serial communication, SMS/network",
        "access":  "Paid access"
    },
    {
        "id":  111,
        "name":  "STM32 multi-sensor cloud environment monitoring system",
        "description":  "Collects light and temperature-humidity data, uploads to OneNET and supports relay linkage.",
        "tech":  "Wildfire F1 board, DHT11, light sensor, ESP8266, OneNET, relay",
        "access":  "Paid access"
    },
    {
        "id":  112,
        "name":  "STM32 barcode recognition and voice broadcast smart control system",
        "description":  "Combines scanning, ultrasonic ranging, stepper motor and voice module for automatic control.",
        "tech":  "QT960 scanner, ultrasonic module, stepper motor, voice module, STM32",
        "access":  "Paid access"
    },
    {
        "id":  113,
        "name":  "STM32 three-axis stepper motor motion control and counting system",
        "description":  "Coordinates three stepper motors with OLED display and infrared counting.",
        "tech":  "STM32, stepper motors, OLED, IR counting module",
        "access":  "Paid access"
    },
    {
        "id":  114,
        "name":  "STM32 OneNET smart security environment monitoring system",
        "description":  "Integrates temperature-humidity, smoke, water level and flame sensors with cloud upload.",
        "tech":  "STM32, DHT11, MQ2, water level sensor, flame sensor, ESP8266, OneNET, OLED",
        "access":  "Paid access"
    },
    {
        "id":  115,
        "name":  "STM32F103ZE RTC clock and LCD display system",
        "description":  "Uses RTC for time display and calibration through an LCD interface.",
        "tech":  "STM32F103ZE, RTC, LCD",
        "access":  "Paid access"
    },
    {
        "id":  116,
        "name":  "STM32 smart alarm clock and PC setting system",
        "description":  "Implements RTC timing, OLED display, alarm settings and PC interaction.",
        "tech":  "STM32, DS1302, OLED, PC software, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  117,
        "name":  "STM32 SD card data storage and file management project",
        "description":  "Writes sensor or runtime data to an SD card for offline data logging.",
        "tech":  "STM32, SD card, SPI/FATFS",
        "access":  "Paid access"
    },
    {
        "id":  118,
        "name":  "STM32F103C8 TFT color display control system",
        "description":  "Drives a 1.3-inch TFT display for text, graphics and status interfaces.",
        "tech":  "STM32F103C8, 1.3-inch TFT LCD, SPI",
        "access":  "Paid access"
    },
    {
        "id":  119,
        "name":  "STM32 DHT22 high-precision temperature-humidity acquisition system",
        "description":  "Uses DHT22 for environmental data acquisition with expansion for display and alarms.",
        "tech":  "STM32, DHT22, GPIO, data acquisition",
        "access":  "Paid access"
    },
    {
        "id":  120,
        "name":  "STM32 ultrasonic ranging and distance alarm system",
        "description":  "Measures distance and supports alarm expansion for parking, liquid level or obstacle avoidance.",
        "tech":  "STM32, HC-SR04, buzzer, OLED",
        "access":  "Paid access"
    },
    {
        "id":  121,
        "name":  "STM32 basketball court sports data monitoring system",
        "description":  "Collects sports or court data and provides statistics, display and alarm prompts.",
        "tech":  "STM32, sensor acquisition, data display, statistics",
        "access":  "Paid access"
    },
    {
        "id":  122,
        "name":  "STM32F030 IIC slave communication design",
        "description":  "Uses CubeMX to configure STM32F030 as an IIC slave device.",
        "tech":  "STM32F030, CubeMX, IIC, slave communication",
        "access":  "Paid access"
    },
    {
        "id":  123,
        "name":  "STM32F407 serial-controlled OLED display system",
        "description":  "Receives serial data and displays it on an OLED screen.",
        "tech":  "STM32F407, OLED, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  124,
        "name":  "STM32F4 WiFi provisioning and mobile APP temperature-humidity monitor",
        "description":  "Connects to WiFi AP provisioning and communicates with a mobile APP for remote readings.",
        "tech":  "STM32F4, CubeIDE, LCD, WiFi AP, APP, DHT11",
        "access":  "Paid access"
    },
    {
        "id":  125,
        "name":  "STM32 smart metering and data statistics system",
        "description":  "Collects pulse or sensor data and displays metering/statistical results.",
        "tech":  "STM32, metering acquisition, display module, keys",
        "access":  "Paid access"
    },
    {
        "id":  126,
        "name":  "STM32 PWM output and motor speed experiment system",
        "description":  "Outputs PWM signals and adjusts duty cycle for motor or servo control.",
        "tech":  "STM32, timer, PWM, motor/servo",
        "access":  "Paid access"
    },
    {
        "id":  127,
        "name":  "STM32 multi-parameter environment detection and PC monitoring system",
        "description":  "Integrates temperature-humidity, smoke, weighing and ultrasonic modules with OLED and PC viewing.",
        "tech":  "STM32, DHT11, MQ2, ultrasonic, weighing module, OLED, PC software",
        "access":  "Paid access"
    },
    {
        "id":  128,
        "name":  "STM32 infrared detection and target counting system",
        "description":  "Detects passing objects and performs counting, prompts and display.",
        "tech":  "STM32, IR sensor, OLED/digital tube, buzzer",
        "access":  "Paid access"
    },
    {
        "id":  129,
        "name":  "STM32 square-wave frequency measurement and PWM duty-cycle analysis system",
        "description":  "Measures frequency and parameters of PWM or square-wave signals.",
        "tech":  "STM32, timer, input capture, PWM, frequency measurement",
        "access":  "Paid access"
    },
    {
        "id":  130,
        "name":  "STM32 elevator environment sensing and servo control project",
        "description":  "Uses PIR, temperature-humidity and OLED display to simulate elevator environment and door control.",
        "tech":  "STM32, SG90, DHT11, OLED, PIR",
        "access":  "Paid access"
    },
    {
        "id":  131,
        "name":  "STM32 18-channel PC data acquisition system",
        "description":  "Collects multi-channel data and uploads it to PC software for display.",
        "tech":  "STM32, 18-channel acquisition, PC software, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  132,
        "name":  "STM32 smart bin automatic lid and environment detection system",
        "description":  "Uses ultrasonic detection to open the lid and monitors temperature-humidity and smoke.",
        "tech":  "STM32, ultrasonic, SG90, DHT11, MQ2, OLED",
        "access":  "Paid access"
    },
    {
        "id":  133,
        "name":  "STM32F407 formaldehyde detection and Bluetooth display system",
        "description":  "Collects formaldehyde data, displays it on OLED and sends it through Bluetooth.",
        "tech":  "STM32F407, ZE08-CH2O, OLED, HC-06",
        "access":  "Paid access"
    },
    {
        "id":  134,
        "name":  "STM32 fingerprint access control and stepper motor system",
        "description":  "Uses fingerprint recognition to trigger stepper-motor lock or door actions.",
        "tech":  "STM32, ATK301 fingerprint, stepper motor, access control",
        "access":  "Paid access"
    },
    {
        "id":  135,
        "name":  "STM32 voice broadcast and Bluetooth control system",
        "description":  "Receives Bluetooth commands and provides smart voice prompts or broadcasts.",
        "tech":  "STM32, voice module, Bluetooth module, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  136,
        "name":  "Dual-STM32 Bluetooth smart fire-fighting linkage system",
        "description":  "Uses Bluetooth between two MCUs to collect smoke and temperature data and trigger alarm or pump actions.",
        "tech":  "Dual STM32, HC-05, MQ2, DHT11, OLED, buzzer, relay, pump",
        "access":  "Paid access"
    },
    {
        "id":  137,
        "name":  "STM32 Aliyun data upload and serial communication system",
        "description":  "Uploads collected data to Aliyun IoT through serial-connected network modules.",
        "tech":  "STM32, serial communication, Aliyun IoT, WiFi module",
        "access":  "Paid access"
    },
    {
        "id":  138,
        "name":  "STM32 Bluetooth smart dormitory environment monitoring system",
        "description":  "Monitors smoke, light, temperature-humidity and infrared states through a mobile Bluetooth interface.",
        "tech":  "STM32, Bluetooth, smoke sensor, light sensor, DHT11, IR sensor",
        "access":  "Paid access"
    },
    {
        "id":  139,
        "name":  "STM32 heart rate monitoring and PC health management system",
        "description":  "Collects heart-rate data and shows or analyzes it on PC software.",
        "tech":  "STM32, heart rate sensor, PC software, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  140,
        "name":  "STM32 gesture recognition smart interaction control system",
        "description":  "Uses gesture, distance and light detection for contactless LED or peripheral control.",
        "tech":  "STM32, gesture module, HCSR05, LED, LDR",
        "access":  "Paid access"
    },
    {
        "id":  141,
        "name":  "STM32 voice-controlled smart waste sorting system",
        "description":  "Uses voice commands and OLED prompts to drive multiple servos for sorting actions.",
        "tech":  "STM32F103ZET6, voice module, SG90, OLED",
        "access":  "Paid access"
    },
    {
        "id":  142,
        "name":  "STM32 GY33 color recognition sorting system",
        "description":  "Uses a color sensor to identify targets and can drive servos or motors for sorting.",
        "tech":  "STM32, GY33, OLED, servo/motor",
        "access":  "Paid access"
    },
    {
        "id":  143,
        "name":  "STM32 liquid level, pressure and environment safety monitoring system",
        "description":  "Collects liquid level, pressure and temperature-humidity data and alarms on abnormal values.",
        "tech":  "STM32, LCD1602, liquid level sensor, pressure sensor, buzzer, temperature-humidity module",
        "access":  "Paid access"
    },
    {
        "id":  144,
        "name":  "STM32 gas station safety monitoring and Bluetooth control system",
        "description":  "Detects temperature, smoke/CO and supports Bluetooth communication, relay control and buzzer alarm.",
        "tech":  "STM32, Bluetooth, DS18B20, OLED, relay, MQ7, buzzer",
        "access":  "Paid access"
    },
    {
        "id":  145,
        "name":  "STM32 infant care and environment alarm system",
        "description":  "Collects infant care and environment data with local display and abnormal alarms.",
        "tech":  "STM32, temperature-humidity sensor, sound/PIR detection, OLED, buzzer",
        "access":  "Paid access"
    },
    {
        "id":  146,
        "name":  "STM32 blood pressure and heart rate health monitoring system",
        "description":  "Collects blood pressure and heart rate data with display and abnormal reminders.",
        "tech":  "STM32, blood pressure module, heart rate sensor, OLED/LCD, alarm module",
        "access":  "Paid access"
    },
    {
        "id":  147,
        "name":  "STM32 FR1002 face recognition access control system",
        "description":  "Uses face recognition for identity authentication and controls relay, motor or lock actions.",
        "tech":  "STM32, FR1002 face recognition, relay/lock, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  148,
        "name":  "STM32 aquaculture water quality monitoring and automatic control system",
        "description":  "Monitors aquaculture water parameters and controls pumps, aeration or alarms by threshold.",
        "tech":  "STM32, water quality sensors, temperature sensor, relay, pump, OLED",
        "access":  "Paid access"
    },
    {
        "id":  149,
        "name":  "FreeRTOS posture and heart-rate multi-task monitoring system",
        "description":  "Uses FreeRTOS to run attitude acquisition, heart-rate acquisition and APP communication tasks.",
        "tech":  "STM32, FreeRTOS, MPU6050, heart rate sensor, APP, serial communication",
        "access":  "Paid access"
    },
    {
        "id":  150,
        "name":  "STM32 sound detection and smart alarm system",
        "description":  "Samples environmental or abnormal sound and links display, alarm and control modules.",
        "tech":  "STM32, sound sensor, OLED, buzzer, relay",
        "access":  "Paid access"
    },
    {
        "id":  151,
        "name":  "STM32 OLED temperature-humidity display system",
        "description":  "Collects temperature-humidity data and displays it on OLED.",
        "tech":  "STM32, DHT11/DHT22, OLED, IIC",
        "access":  "Paid access"
    },
    {
        "id":  152,
        "name":  "STM32 OneNET dual-weighing smart monitoring system",
        "description":  "Collects dual load-cell data, uploads to OneNET and supports threshold alarms.",
        "tech":  "STM32, dual load cells, HX711, ESP8266, OneNET",
        "access":  "Paid access"
    },
    {
        "id":  153,
        "name":  "STM32F103ZET6 minimum system board schematic design",
        "description":  "Designs power, clock, reset and download circuits for an STM32 minimum system board.",
        "tech":  "STM32F103ZET6, schematic, power circuit, clock/reset, download interface",
        "access":  "Paid access"
    },
    {
        "id":  154,
        "name":  "STM32 ST7789 color TFT display system",
        "description":  "Drives a 1.3-inch TFT screen for text, graphics and status UI display.",
        "tech":  "STM32, 1.3-inch TFT LCD, ST7789, SPI",
        "access":  "Paid access"
    },
    {
        "id":  155,
        "name":  "ASRPRO offline voice recognition smart control system",
        "description":  "Recognizes offline voice commands and can control lights, fans, relays and other peripherals.",
        "tech":  "ASRPRO, STM32/microcontroller, voice recognition, relay",
        "access":  "Paid access"
    },
    {
        "id":  156,
        "name":  "ESP8266 Aliyun smart home IoT system",
        "description":  "Connects devices to Aliyun through ESP8266 for data upload and remote control.",
        "tech":  "ESP8266, Aliyun IoT, smart home, APP/cloud platform",
        "access":  "Paid access"
    },
    {
        "id":  157,
        "name":  "STM32 multifunction electronic clock and smart fan control system",
        "description":  "Combines RTC clock, TFT display, key settings, LED prompts and relay fan control.",
        "tech":  "STM32F1, CubeMX, DS1302, TFT LCD, keys, LED, relay, fan",
        "access":  "Paid access"
    },
    {
        "id":  158,
        "name":  "STM32 Bluetooth smart curtain control system",
        "description":  "Uses Bluetooth commands to adjust a three-level stepper motor curtain with temperature-humidity sensing.",
        "tech":  "STM32, HC-05, stepper motor, DHT11, curtain model",
        "access":  "Paid access"
    },
    {
        "id":  159,
        "name":  "STM32 PC-controlled motor start-stop system",
        "description":  "Uses PC commands to start, pause and report motor state through serial communication.",
        "tech":  "STM32, PC software, serial communication, motor driver",
        "access":  "Paid access"
    },
    {
        "id":  160,
        "name":  "STM32 heart rate and SpO2 health monitoring system",
        "description":  "Collects heart rate and blood oxygen data with local display and abnormal prompts.",
        "tech":  "STM32, heart rate/SpO2 module, OLED/LCD, buzzer",
        "access":  "Paid access"
    },
    {
        "id":  161,
        "name":  "STM32 ESP8266 smart security monitoring system",
        "description":  "Combines photoelectric, temperature-humidity, smoke and flame detection with WiFi upload and alarms.",
        "tech":  "STM32, ESP8266, photoelectric sensor, DHT11, MQ2, flame sensor",
        "access":  "Paid access"
    },
    {
        "id":  162,
        "name":  "STM32 Hall sensor speed measurement system",
        "description":  "Collects rotational speed pulses and displays or alarms on motor/turntable speed.",
        "tech":  "STM32, Hall sensor, timer, speed algorithm, OLED",
        "access":  "Paid access"
    },
    {
        "id":  163,
        "name":  "STM32 voice alarm clock and PC management system",
        "description":  "Implements alarm clock, temperature-humidity acquisition, voice broadcast and PC parameter setting.",
        "tech":  "STM32, PC software, voice module, DHT11, RTC/timer",
        "access":  "Paid access"
    },
    {
        "id":  164,
        "name":  "STM32 smart desk lamp and power monitoring system",
        "description":  "Controls lamp brightness and measures current, voltage and power for energy monitoring.",
        "tech":  "STM32, smart lamp, current/voltage sampling, power monitoring, LED dimming",
        "access":  "Paid access"
    },
    {
        "id":  165,
        "name":  "Dual-STM32 wireless communication and data exchange system",
        "description":  "Transfers data between two STM32 nodes for remote acquisition, control and state synchronization.",
        "tech":  "Dual STM32, wireless module, serial communication, data exchange",
        "access":  "Paid access"
    },
    {
        "id":  166,
        "name":  "STM32 Aliyun multi-parameter health environment monitoring system",
        "description":  "Collects posture, heart-rate/blood-pressure and temperature-humidity data and uploads to Aliyun.",
        "tech":  "STM32F103, ESP01S, Aliyun, APP, MPU6050, heart-rate/blood-pressure module, DHT11",
        "access":  "Paid access"
    },
    {
        "id":  167,
        "name":  "4G fire-fighting management and remote alarm system",
        "description":  "Collects fire-safety data, communicates through 4G and reports abnormal conditions remotely.",
        "tech":  "STM32, 4G module, fire monitoring, remote alarm",
        "access":  "Paid access"
    },
    {
        "id":  168,
        "name":  "STM32 factory air quality monitoring and automatic ventilation system",
        "description":  "Monitors factory air conditions and controls fans or ventilation equipment by threshold.",
        "tech":  "STM32, air quality sensor, relay, fan, OLED",
        "access":  "Paid access"
    },
    {
        "id":  169,
        "name":  "STM32 smart health weighing and voice broadcast system",
        "description":  "Collects weight and health data, broadcasts results and can expand to WiFi upload.",
        "tech":  "STM32F103, ESP01S, TTS, HX711, load cell, heart-rate/blood-pressure module",
        "access":  "Paid access"
    },
    {
        "id":  170,
        "name":  "Dual-STM32 cloud-based smart fire and security linkage system",
        "description":  "Two STM32 boards collect smoke, flame and IR data, upload through WiFi and support Bluetooth APP alarms.",
        "tech":  "Dual STM32F103, ESP01S, Bluetooth, buzzer, smoke sensor, flame sensor, photoelectric IR sensor",
        "access":  "Paid access"
    },
    {
        "id":  171,
        "name":  "STM32 temperature-humidity and pH environment monitoring system",
        "description":  "Collects temperature-humidity and pH data with display, threshold alarms and data records.",
        "tech":  "STM32, temperature-humidity sensor, pH sensor, OLED, PCB",
        "access":  "Paid access"
    },
    {
        "id":  172,
        "name":  "STM32 multi-parameter water quality monitoring system",
        "description":  "Measures pH, turbidity, TDS, temperature-humidity and water level for water quality evaluation and alarm.",
        "tech":  "STM32F103, pH sensor, turbidity sensor, TDS sensor, temperature-humidity sensor, water level sensor",
        "access":  "Paid access"
    },
    {
        "id":  173,
        "name":  "STM32 Aliyun air quality smart regulation system",
        "description":  "Collects temperature-humidity, light and air-quality data, uploads to Aliyun and controls fan, relay, buzzer and LED.",
        "tech":  "STM32, WiFi module, Aliyun, DHT11, GM1566, MQ135, relay, fan, LED, OLED",
        "access":  "Paid access"
    }
];
