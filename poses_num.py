import cv2
import mediapipe as mp
import math
import numpy as np
import random as rd
digitos_azar=[]
for i in range(3):
    digitos_azar.append(rd.randint(0,9))
print(digitos_azar)

variable=str(digitos_azar[0])+" "+str(digitos_azar[1])+" "+str(digitos_azar[2])
print(variable)
mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose
#pose_imagen=mp_pose.Pose(static_image_mode=True)
pose_video=mp_pose.Pose(static_image_mode=False)

def detectpose(image, pose, display=True):
    output_image=image.copy()
    image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results=pose.process(image_rgb) 
    height, width, _ =image.shape
    landmarks=[]
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS)
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x * width), int(landmark.y * height), int(landmark.z * width)))
    if display:
        cv2.imshow("Image", output_image)
    else:
        return output_image, landmarks


def calcule_angle(frame, punto1, punto2, punto3):
    x1, y1, _ = punto1
    x2, y2, _ = punto2
    x3, y3, _ = punto3
    #visualizacion

    cv2.line(frame,(x1,y1),(x2,y2),(255,255,0),5)
    cv2.line(frame,(x2,y2),(x3,y3),(255,255,0),5)
    cv2.line(frame,(x1,y1),(x3,y3),(255,255,0),10)
    contorno=np.array([[x1,y1], [x2,y2], [x3,y3]])
    cv2.fillPoly(frame, pts=[contorno], color=(128,0,250))

    
    cv2.circle(frame,(x1,y1),6,(0,255,255),-1)
    cv2.circle(frame,(x2,y2),6,(128,0,250),-1)
    cv2.circle(frame,(x3,y3),6,(255,191,0),-1)
    angle=math.degrees(math.atan2(y3-y2, x3-x2)-math.atan2(y1-y2, x1-x2))
    if angle<0:
        angle+=360
    cv2.putText(frame,str(int(angle)),(x2+30, y2), 1, 1.5, (0,0,0), 2)

    return angle


def class_pose(landmarks, output_image, display= False):
    label="no detection!"

    left_muñeca=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value])
    print("left_muneca: {}".format(left_muñeca))

    right_muñeca=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])
    print("right_muneca: {}".format(right_muñeca))

    left_elbow_angle=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
    print("left_elbow: {}".format(left_elbow_angle))
    
    right_elbow_angle=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])
    print("right_elbow: {}".format(right_elbow_angle))
    
    left_shoulder_angle=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    print("left_shoulder: {}".format(left_shoulder_angle))
    
    right_shoulder_angle=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])
    print("right_shoulder: {}".format(right_shoulder_angle))
    
    left_knee_angle=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                   landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
    print("left_knee: {}".format(left_knee_angle))

    right_knee_angle=calcule_angle(output_image, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    print("right_knee: {}".format(right_knee_angle))
    print("***************")

    if (150<left_muñeca<200) and (150<right_muñeca<200):
        if (140<left_elbow_angle<280) and (80<right_elbow_angle<130):
            if (30<left_shoulder_angle<90) and (30<right_shoulder_angle<90):
                if (160<left_knee_angle<195) and (160<right_knee_angle<195):
                    label="numero 0"
                    

    if (150<left_elbow_angle<200) and (150<right_elbow_angle<200):
        if (0<left_shoulder_angle<30) and (0<right_shoulder_angle<30):
            if (160<left_knee_angle<195) and (160<right_knee_angle<195):
                label="numero 1"
    
    if (170<left_muñeca<270) and (170<right_muñeca<270):
        if (170<left_elbow_angle<210) and (170<right_elbow_angle<210):
            if (200<left_shoulder_angle<280) and (70<right_shoulder_angle<130):
                if (40<left_knee_angle<100) and (40<right_knee_angle<100):
                    label="numero 2"

    if (190<left_muñeca<230) and (160<right_muñeca<210):
        if (160<left_elbow_angle<220) and (150<right_elbow_angle<210):
            if (190<left_shoulder_angle<260) and (70<right_shoulder_angle<120):
                if (165<left_knee_angle<195) and (165<right_knee_angle<195):
                    label="numero 3"
    
    if (170<left_elbow_angle<200) and (230<right_elbow_angle<290):
        if (0<left_shoulder_angle<50) and (80<right_shoulder_angle<120):
            if (165<left_knee_angle<195) and (165<right_knee_angle<195):
                label="numero 4"

    if (160<left_muñeca<220) and (160<right_muñeca<220):
        if (160<left_elbow_angle<220) and (150<right_elbow_angle<220):
            if (140<left_shoulder_angle<160) and (140<right_shoulder_angle<160):
                if (165<left_knee_angle<195) and (165<right_knee_angle<195):
                    label="numero 5"

    if (100<left_muñeca<170) and (100<right_muñeca<170):
        if (140<left_elbow_angle<190) and (150<right_elbow_angle<220):
            if (100<left_shoulder_angle<160) and (200<right_shoulder_angle<260):
                if (180<left_knee_angle<230) and (250<right_knee_angle<300):
                    label="numero 6"
    
    if (170<left_muñeca<240) and (170<right_muñeca<240):
        if (180<left_elbow_angle<220) and (180<right_elbow_angle<220):
            if (0<left_shoulder_angle<30) and (45<right_shoulder_angle<110):
                if (165<left_knee_angle<195) and (165<right_knee_angle<195):
                    label="numero 7"

    if (150<left_muñeca<200) and (150<right_muñeca<200):
        if (80<left_elbow_angle<120) and (240<right_elbow_angle<290):
            if (120<left_shoulder_angle<170) and (120<right_shoulder_angle<170):
                if (200<left_knee_angle<280) and (75<right_knee_angle<130):
                    label="numero 8"
    
    if (180<left_muñeca<220) and (140<right_muñeca<180):
        if (100<left_elbow_angle<150) and (250<right_elbow_angle<300):
            if (180<left_shoulder_angle<230) and (75<right_shoulder_angle<110):
                if (165<left_knee_angle<195) and (165<right_knee_angle<195):
                    label="numero 9"
    
    cv2.rectangle(output_image, (50,130), (250,175), (0,0,0), cv2.FILLED)

    #ESCRIBIR EN LOS RECTANGULOS
    cv2.putText(output_image, str(label), (60,160), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)

    if display:
        cv2.imshow("Image", output_image)
    else:
        return output_image, landmarks


camara_video= cv2.VideoCapture(0)
camara_video.set(3,1280)
camara_video.set(4,960)
cv2.namedWindow("Pose Classification", cv2.WINDOW_NORMAL)
while camara_video.isOpened():
    ret, frame=camara_video.read()
    if ret==False:
        break
    frame=cv2.flip(frame,1)
    frame_height, frame_width, _= frame.shape
    frame=cv2.resize(frame,(int(frame_width*(640/frame_height)),640))
    frame, landmarks=detectpose(frame,pose_video,display=False)

    if landmarks:
        frame, _=class_pose(landmarks,frame,display=False)

    cv2.rectangle(frame, (50,30), (260,80), (0,0,0), cv2.FILLED)

    #ESCRIBIR EN LOS RECTANGULOS
    cv2.putText(frame, "aleatorio: "+str(variable), (60,60), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)
    
    cv2.imshow("videocam",frame)
    if cv2.waitKey(1)==ord("a"):
        break
camara_video.release()
cv2.destroyAllWindows()
