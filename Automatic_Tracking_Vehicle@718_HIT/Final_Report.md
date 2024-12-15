# Project Report
This STM32-based project is under the selection process of 718 laboratory(primary team for robotics team) in Nov. 2021.
- **Developed** a smart car based on the STM32 as the main control board, a power module, and an L298N electric drive module, capable of automatically tracking and remotely retrieving blocks using a robotic arm in specific areas.
- **Utilized** an infrared photocell and ADC to collect voltage signals and used serial port debugging to identify tracks.
- **Developed** a tracking and maze algorithm enabling the car to navigate out of unknown maze environments while tracking.
- **Used** a Bluetooth module with a serial port to achieve remote control of the car and the robotic arm servo.

## (I) Design Concept

### 1. Components and Hardware Configuration
The electrical control system of the line-following vehicle consists of the following modules: 
- **Main Control Board**: A microcontroller minimum system.
- **Photoelectric Sensors**: Infrared photoelectric reflection sensors (referred to as photoelectric pairs) detect black lines by capturing voltage variations.
- **Power Supply Module**: Provides power to the system.
- **HC-05 Bluetooth Module**: Enables wireless control of the vehicle.
- **L298N Motor Driver Module**: Converts PWM signals from the main control board into higher-power electrical signals to drive the motors.

The mechanical drive system includes:
- **Four DC Motors**: The two left motors are connected in parallel to the motor output "B" of the motor driver, while the two right motors are connected to "A". Speeds are controlled via ENA (for the right side) and ENB (for the left side) using PWM signals.
- **Two Servos**: 
  - Servo 1 is connected to `TIM1_CH3` and controls the lifting angle of the robotic arm. A high-torque servo (25 kg) is used due to the arm's weight.
  - Servo 2 is connected to `TIM1_CH4` and controls the gripper mechanism, utilizing an MG90s metal gear digital servo.

### 2. Pin Assignments
- **Motor Control**: 
  - Right motors are connected to output "A" of the motor driver, with speed controlled by ENA (`TIM1_CH1`). Forward/reverse directions are controlled by `PB6` and `PB7`. 
  - Left motors are connected to output "B", with speed controlled by ENB (`TIM1_CH2`). Forward/reverse directions are controlled by `PC6` and `PC7`.

- **Servo Control**: 
  - Servo 1 (`TIM1_CH3`) for robotic arm lifting.
  - Servo 2 (`TIM1_CH4`) for gripper operation.

- **Photoelectric Sensors**: 
  - `LEFTLEFT` to `ADC1_CH7`, `LEFT` to `ADC1_CH11`, `MID` to `ADC1_CH12`, `RIGHT` to `ADC1_CH13`, `RIGHTRIGHT` to `ADC1_CH2`, and `FRONT` to `ADC1_CH0`.

- **UART Connections**: 
  - UART5 connects to a USB-to-TTL adapter for debugging and threshold calibration of photoelectric sensors.
  - UART4 connects to the HC-05 Bluetooth module for receiving commands.

### 3. Turning Mechanism
The vehicle uses differential drive for turning, as the two front wheels cannot yaw. 
- Left and right motors' directions are controlled by GPIO (`PC6`, `PC7` for left; `PB6`, `PB7` for right).
- Turning angles depend on motor speed and delay durations. Example functions:

```c
void RightTurn(void) {
    MotorRightLeft_CH1(0);  // Clockwise
    MotorRightLeft_CH2(1);  // Clockwise

    TIM_SetCompare1(TIM1, 10000);
    TIM_SetCompare2(TIM1, 10000);
    delay_nms(570); // Delay for 90° right turn
}

void LeftTurn(void) {
    MotorRightLeft_CH1(1);  // Clockwise
    MotorRightLeft_CH2(0);  // Clockwise

    TIM_SetCompare1(TIM1, 10000);
    TIM_SetCompare2(TIM1, 10000);
    delay_nms(520); // Delay for 90° left turn
}
```

### 4. Line Following Method
The photoelectric sensors detect reflected infrared signals:
- **White surfaces**: Signal reflected; sensor outputs low voltage.
- **Black surfaces**: Signal absorbed; sensor outputs high voltage.

#### Algorithm:
- **Initial Design**: Using only `LEFT` and `RIGHT` sensors for both straight-line following and 90° turns. A software filtering mechanism verifies high voltage signals to adjust the vehicle’s direction or detect intersections for turning.
- **Improved Design**: Added `LEFTLEFT` and `RIGHTRIGHT` sensors for more reliable straight-line following and intersection detection.

## (II) Implementation of Basic Functions

### 1. PWM Signal Output
The PWM signals for motor control are generated using the `TIM1` timer channels. This unified setup simplifies initialization and maintenance.

### 2. ADC Voltage Sampling
Photoelectric sensors are tested by observing voltage changes using an oscilloscope. Thresholds for black line detection are determined via serial debugging. Example code:

```c
u16 Get_Adc(u8 ch) {
    ADC_RegularChannelConfig(ADC1, ch, 1, ADC_SampleTime_239Cycles5);
    ADC_SoftwareStartConvCmd(ADC1, ENABLE);

    while (!ADC_GetFlagStatus(ADC1, ADC_FLAG_EOC));
    return ADC_GetConversionValue(ADC1);
}
```

### 3. Bluetooth and Serial Communication
Bluetooth controls the vehicle’s movement and servos using predefined commands. Example UART interrupt handler:

```c
void DEBUG_USART_IRQHandler(void) {
    uint8_t ucTemp;
    uint8_t ucTemp1;

    if (USART_GetITStatus(DEBUG_USARTx, USART_IT_RXNE) != RESET) {
        ucTemp1 = USART_ReceiveData(DEBUG_USARTx);
        ucTemp = USART_ReceiveData(DEBUG_USARTx);

        if (ucTemp == '5') {
            cnt += 100;
            SetSteerAngle3(cnt);
        } else if (ucTemp == '6') {
            cnt -= 100;
            SetSteerAngle3(cnt);
        }
    }
}
```

### 4. Automatic Control Logic
In the (4+2) sensor configuration:
- `LEFT`, `RIGHT` for straight-line following.
- `LEFTLEFT`, `RIGHTRIGHT` for detecting intersections.

Example forward control with PI feedback:

```c
void Forward(void) {
    int Err = 0;
    while (status % 2 == 0) {
        Err = Err + (Get_Adc(11) - Get_Adc(13));
        TIM_SetCompare1(TIM1, 12000 - Get_Adc(13) * 2.5 + Err * 0.25);
        TIM_SetCompare2(TIM1, 12000 - Get_Adc(11) * 2.5 - Err * 0.25);
        delay_nms(15);
    }
}
```

## (III) Issues and Solutions

1. **Initial Design Limitations**: Two-sensor control struggled with simultaneous line following and turning. Solution: Improved algorithm with additional sensors.
2. **Missed Turns**: Added delay and condition checks to ensure successful detection and turning at intersections.
3. **Dead-End Detection**: Adjusted logic for more reliable detection and U-turn execution.

## (IV) Post-Competition Reflection

Despite challenges during the competition, the team gained valuable experience in coding, hardware design, and collaboration. The process highlighted the importance of thorough preparation, on-site testing, and robust hardware connections. These lessons will drive future improvements and innovation in engineering projects.


Electrical Control Subgroup.
