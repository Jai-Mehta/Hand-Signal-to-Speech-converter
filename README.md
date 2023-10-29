# Hand-Signal-to-Speech-converter
"Talking Hand: A Hand Signal to Speech Converter" is an innovative application developed to assist physically challenged individuals in communicating through hand signals. This repository contains the code and documentation for the application, which uses Computer Vision (CV) and Machine Learning (ML) techniques.


# Talking Hand: A Hand Signal to Speech Converter

**Author**: Jai Anish Mehta

**Email**: jaimehta@cs.stonybrook.edu

**Affiliation**: Department of Computer Science, Stony Brook University, Stony Brook, New York, USA

**SBU ID**: 114834757

## Abstract

The field of Human-Computer Interaction (HCI) has seen significant advancements, with a focus on improving the efficiency of interaction between humans and computers. One area where this can make a profound impact is assisting individuals with physical challenges who cannot speak. Communication can be especially challenging for them, as not everyone understands sign language. To address this issue, the "Talking Hand" application has been developed, which serves as a Hand Signal to Speech converter. This application takes real-time video input, converts it to speech, and plays the speech as audio. This paper discusses the development of the application and its potential benefits for physically challenged individuals.

## Keywords

- Computer Vision (CV)
- YOLOv3
- Machine Learning (ML)
- Classification

## 1. Introduction

As technology advances, the aim is to improve the quality of life and increase comfort. Many innovations arise from the desire to automate or facilitate tasks. This technology can be particularly valuable for individuals with physical challenges. Prosthetic limbs, electronic wheelchairs, and hearing aids are examples of technology designed to assist physically disabled individuals. Inspired by these ideas, the "Talking Hand" application was developed to help people who cannot speak and use hand signals for communication.

People who rely on sign language for communication, often using American Sign Language (ASL), may require a translator to communicate with those who do not understand ASL. The "Talking Hand" application eliminates the need for a translator by converting hand-sign videos into text or speech, making communication more accessible to a wider audience.

## 2. Motivation

The motivation behind the "Talking Hand" application was to create a customizable hand-sign language to speech converter. This application allows users to record custom hand signals and create custom sentences. By providing this flexibility, it becomes more user-friendly and adaptable, especially for those who may not be trained in ASL. Additionally, a "Cancel" feature was added for user convenience.

## 3. Related Works

Several research efforts in HCI have explored similar applications, each with varying approaches to input and classification. Some applications use motion sensors in gloves to detect hand movements and predict hand signs. Apple, for instance, uses pulse detection in their Apple Watch to classify hand gestures based on pulse patterns. However, there has been limited research on integrating YOLOv3 for speech output in hand sign recognition applications.

## 4. Methodology

The development of the "Talking Hand" application is divided into five major stages:

1. **Data Collection**: A dataset of custom hand signs was collected using a laptop camera to ensure data quality and simulate real-world conditions.

2. **Data Labeling**: The collected data was labeled using the "labelImg" Python application, generating labeled images with bounding boxes and class labels.

3. **Transfer Learning**: Transfer learning was employed using a pre-trained YOLOv3 model, adapting it to the custom hand signs dataset.

4. **Classification**: Real-time video input is processed by the trained model, and hand signs are classified. The classification output includes the label and prediction accuracy.

5. **Text to Speech**: The application uses the "pyttsx3" library for text-to-speech conversion, transforming the labels into speech played as audio.

## 5. Implementation

- **Stage I: Data Collection**: Custom dataset created using a laptop camera to capture various hand signs.

- **Stage II: Data Labeling**: "labelImg" application used for labeling, producing labeled images with bounding boxes and class labels.

- **Stage III: Transfer Learning**: Transfer learning on a pre-trained YOLOv3 model, customized for the custom hand signs dataset.

- **Stage IV: Classification**: Real-time video input processed, and hand signs classified, generating output labels.

- **Stage V: Text to Speech**: "pyttsx3" library used for text-to-speech conversion, playing the labels as speech.

## 6. Evaluation

The "Talking Hand" application's performance was evaluated by having 10 users perform each of the six hand signs five times. The average prediction accuracy for each class is as follows:

- **Family**: 80%
- **I Love You**: 89%
- **Thank You**: 96%
- **Cold**: 90%
- **My Custom Sentence**: 78%
- **Cancel**: 93%

The "Family" and "My Custom Sentence" signs had lower accuracy due to their similarity and difficulty in precise performance. With a larger, more diverse dataset, prediction accuracy could be significantly improved.

## 7. Discussion

The "Talking Hand" application introduces the concept of customizable hand signs and their conversion into speech. Future enhancements include converting entire sentences to speech with punctuation and enabling the application to start with a clap or finger snap for user convenience.

## 8. Conclusion

The "Talking Hand" application, developed at Stony Brook University, is a significant step in assisting physically challenged individuals with communication. It leverages Computer Vision, Machine Learning, and Human-Computer Interaction to provide a customizable hand-sign to speech conversion solution. While the current prediction accuracy is promising, further improvements are possible with a larger and more diverse dataset.

## 9. References

1. [How to Perform Object Detection with YOLOv3 in Keras](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/)
2. [LabelImg](https://github.com/heartexlabs/labelImg)
3. [Darknet](https://github.com/AlexeyAB/darknet)
4. [pyttsx3](https://pypi.org/project/pyttsx3/)
# Hand-Signal-to-Speech-converter
