# Real-Time Facial Recognition

This application performs real-time facial recognition processing on a video stream received via http. It allows the ability to train the system to detect new faces and create alerts. This application is a slight modification of Brandon Joffe's 'Home Surveillance with Facial Recognition' available @ https://github.com/BrandonJoffe/home_surveillance.git

---

### How does it work? ###

The SurveillanceSystem object is the heart of the system. It can process several IPCameras and monitors the system's alerts. A FaceRecogniser object provides functions for training a linear SVM classifier using the face database and includes all the functions necessary to perform face recognition using Openface's pre-trained neural network (thank you Brandon Amos!!). Each IPCamera has its own MotionDetector and FaceDetector object, which are used by other subsequent processes to perform face recognition and person tracking. The FlaskSocketIO object streams jpeg frames (mjpeg) to the client and transfers JSON data using HTTP POST requests and web sockets.


## Installation and Usage ##


---
1) Clone Repo

```
git clone https://github.com/NelsonKadama/fog_node_face_recognition.git
```

2) Pull Docker Image

```
docker pull nkadama/surveillance
```

3) Run Docker image, make sure you mount your User (for MAC) or home (for Ubuntu) directory as a volume so you can access your local files

```
docker run -v /path/to/cloned/repo/:/host -p 5000:5000 -t -i nkadama/surveillance  /bin/bash
```

- Navigate to the fog_node_face_recognition project inside the 'host' directory within your Docker container
- Move into the system directory

```
cd host
cd fog_node_face_recognition
cd system
```
4) Run WebApp.py
```
python WebApp.py
```
- Visit ```localhost:5000 ```
- Login Username: ```admin``` Password ```admin```



# License
---

Copyright 2016, Brandon Joffe, All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

- http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

# References
---

- Video Streaming Code - http://www.chioka.in/python-live-video-streaming-example/
- Flask Web Server GPIO - http://mattrichardson.com/Raspberry-Pi-Flask/
- Openface Project - https://cmusatyalab.github.io/openface/
- Flask Websockets - http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
