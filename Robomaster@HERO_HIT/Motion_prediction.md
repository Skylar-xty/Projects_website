# Target Tracking and Aiming System in Complex Motion Environment
I was an algorithm designer and tester in my university's robotics team, participating in Robomaster University Championships Competition (organized by Dajiang Innovation), progressing from provincial and regional competitions to the national finals.

## Algorithms

### Kalman Filter

<details>
  <summary>Click to expand the code</summary>

    ```cpp

    #ifndef HERORM2022_KALMAN_HPP
    #define HERORM2022_KALMAN_HPP

    #include "logger.h"
    #include "util_func.h"
    #include <Eigen/Dense>

    template<int V_X, int V_Z>
    class Kalman {
    public:
        using Matrix_zzd = Eigen::Matrix<double, V_Z, V_Z>;
        using Matrix_xxd = Eigen::Matrix<double, V_X, V_X>;
        using Matrix_zxd = Eigen::Matrix<double, V_Z, V_X>;
        using Matrix_xzd = Eigen::Matrix<double, V_X, V_Z>;
        using Matrix_x1d = Eigen::Matrix<double, V_X, 1>;
        using Matrix_z1d = Eigen::Matrix<double, V_Z, 1>;
        int64_t last_t{0};// 单位ms

    public:
        Matrix_x1d X;// k-1时刻的滤波值，即是k-1时刻的值
        Matrix_xzd K;// Kalman增益
        Matrix_xxd A;// 转移矩阵
        Matrix_zxd H;// 观测矩阵
        Matrix_xxd Q;// 预测过程噪声偏差的方差
        Matrix_zzd R;// 测量噪声偏差，(系统搭建好以后，通过测量统计实验获得)
        Matrix_xxd P;// 估计误差协方差
        double Distance_change{0};
    public:
        Kalman()
        {
            A.setIdentity();
            R = R.setIdentity();
            R(0, 0) = 4 * pow(180 / Util::PI, 2);// 角度测量值方差
            R(1, 1) = 400 * pow(180 / Util::PI, 2);// 角度测量值方差
            R(2, 2) = 4 * pow(180 / Util::PI, 2);// 角度测量值方差

            Q = Q.setIdentity();
            Q(0, 0) = 33;
            Q(1, 1) = 328280;
            Q(2, 2) = 33000;
            Q(3, 3) = 1 ;
            Q(5, 5) = 0.01 * pow((180.0 / Util::PI), 2);
            Q(6, 6) = 100.0 * pow((180.0 / Util::PI), 2);
            P = P.setIdentity();
            H << 1, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 1, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 1, 0;
        }
        bool judgeDistanceDelta(double distance){
            // record error
            if(distance - X(3, 0) > 1 && Distance_change < 5)
            {
                Distance_change ++;
                return false;
            }
            //if Distance_change>4时，force to reset Distance
            else if(Distance_change > 4)
            {
                Distance_change = 0;
                X(3, 0) = distance;
            }
            return true;
        }

        Kalman(Matrix_xxd A, Matrix_zxd H, Matrix_xxd Q, Matrix_zzd R, Matrix_x1d init, double t) { reset(A, H, Q, R, init, t); }

        void reset(Matrix_xxd A, Matrix_zxd H, Matrix_xxd Q, Matrix_zzd R, Matrix_x1d init, double t)
        {
            this->A = A;
            this->H = H;
            this->P = Matrix_xxd::Zero();
            this->Q = Q;
            this->R = R;
            X = init;
            last_t = t;
        }

        void reset(Matrix_x1d init, int64_t t)
        {
            X = init;
            last_t = t;
        }

        void reset(double yaw ,double distance ,double pitch)
        {
            A.setIdentity();
            P.setIdentity();
            K.setIdentity();
            X << yaw, 0.0, 0.0, distance, 0.0,0.0, pitch, 0.0;
            //last_t = t;
        }

        Matrix_x1d update(Matrix_z1d z_k, int64_t t)
        {
            if (t - last_t < 0)
            {
                LOGE("fatal error");
                exit(-1);
            }
            // time term in T
            A(0, 1) = static_cast<double>((t - last_t) * 0.001);
            A(0, 2) = static_cast<double>(0.5 * (t - last_t) * 0.001 * (t - last_t) * 0.001);
            A(1, 2) = static_cast<double>((t - last_t) * 0.001);
            A(3, 4) = static_cast<double>((t - last_t) * 0.001);
            A(4, 5) = static_cast<double>((t - last_t) * 0.001);
            A(6, 7) = static_cast<double>((t - last_t) * 0.001);
            last_t = t;

            // predict step
            Matrix_x1d p_x_k = A * X;// The prior estimate of **x** is given by the posterior estimate from the previous time step and the input information.

            // calculate the covariance
            P = A * P * A.transpose() + Q;// 计算先验均方差 p(n|n-1)=A^2*p(n-1|n-1)+q

            // 计算kalman增益
            P = A * P * A.transpose() + Q; // Calculate the prior covariance: p(n|n-1) = A^2 * p(n-1|n-1) + q

            // Calculate the Kalman gain
            K = P * H.transpose() * (H * P * H.transpose() + R).inverse(); // Kg(k) = P(k|k-1) * H' / (H * P(k|k-1) * H' + R)

            // Correct the result, i.e., compute the filtered value
            X = p_x_k + K * (z_k - H * p_x_k); // Use the residual to improve the estimate of x(t), giving the posterior estimate: X(k|k) = X(k|k-1) + Kg(k) * (Z(k) - H * X(k|k-1))

            // Update the posterior covariance
            P = (Matrix_xxd::Identity() - K * H) * P; // Calculate the posterior covariance: P[n|n] = (1 - K[n] * H) * P[n|n-1]

            return X;

            }
      };

    #endif//HERORM2022_KALMAN_HPP 
    
    ```

</details> 

## Videos

Here are some videos during testing and real performance.

The Figure shows the UI of our robots when the target mobile armor was moving in both X, Y directions with different moving speeds.
Green notation meanings:

1. tracking: Now, the robot is tracking the same enemy robot.

2. target_X, target_Y, target_Z: THe world coordinate after conversion of the enemy armor center.

3. final_yaw, final_pitch: 

4. Armor_Type: 0 represents small size of armor, 1 represents big size of armor.

5. no gyro!: The target armor's motion is not in the "gyro" mode(which means doing self-rotation).

6. dir: right represents the target is moving right in the UI.

7. bullet_speed: the set bullet speed of our robot.

<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./test.mp4" type="video/mp4">
  Fig1: Mobile Armor Plate Recognition, Coordinate Computation, and Tracking UI Interface
</video>

This Figure shows the performance of our robot shooting the outpost (one kind of devices in the competition). The successful rate is 100%.
<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./demo1-1.mp4" type="video/mp4">
  The performance of the shooting algorithms.
</video>


<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./demo2-1.mp4" type="video/mp4">
</video>

Below are some of the live streamings of one game in the National Robomaster Finals. 
<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./real.mp4" type="video/mp4">
  Our team is the red side, you can focus on two number-five robots having one-to-one shooting.
</video>

<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./real.mp4" type="video/mp4">
  First-view UI videos showcasing the target infomation and shooting solution.
</video>

