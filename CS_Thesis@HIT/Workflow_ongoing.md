# Introdution
In the Internet of Vehicles (IoV), frequent communication between vehicles and roadside units (RSUs) is required for tasks such as position updates, driving status, and traffic information. During this transmission process, data may face security issues such as malicious node attacks, data tampering, and replay attacks. Therefore, ensuring data security and credibility, while rapidly identifying and isolating malicious nodes, is an important research topic.

- Data Security Issues: Data in the IoV is vulnerable to threats such as man-in-the-middle attacks and eavesdropping during transmission. Ensuring the security of data transmission is crucial.  

- Data Credibility Issues: In the IoV, the volume of data exchanged between vehicles is enormous, but malicious nodes may send false data. Ensuring the authenticity and integrity of the data is key.

This project aims to ensure vehicle identity authentication through PKI and to evaluate the trustworthiness of vehicle data dynamically via a trust management mechanism, thereby constructing a secure and reliable vehicular network data authentication system.
The system mainly consists of two parts:

1. PKI Identity Authentication Layer
Based on elliptic curve cryptography for public key encryption and digital signature algorithms, each vehicle is assigned a unique public and private key to achieve bidirectional encrypted communication and identity authentication.

2. Trust Management Layer
Based on the vehicle's historical behavior and communication records, the trust value of the vehicle is dynamically adjusted. Nodes with low trust values are automatically isolated to reduce the risk of malicious data propagation.