import cv2
import mediapipe as mp
import pyttsx3
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
engine = pyttsx3.init()
# For static images:
IMAGE_FILES = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      )
      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    cv2.imwrite(
        '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
    # Draw hand world landmarks.
    if not results.multi_hand_world_landmarks:
      continue
    for hand_world_landmarks in results.multi_hand_world_landmarks:
      mp_drawing.plot_landmarks(
        hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

def letter1(): #A - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'A'
    if hand_landmarks.landmark[5].y < hand_landmarks.landmark[8].y and\
            hand_landmarks.landmark[9].y < hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y and\
            hand_landmarks.landmark[4].y < hand_landmarks.landmark[6].y and\
            hand_landmarks.landmark[4].x > hand_landmarks.landmark[6].x and\
            hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek
        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter2(): #B - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'B'
    if hand_landmarks.landmark[6].y > hand_landmarks.landmark[8].y and\
            hand_landmarks.landmark[10].y > hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[14].y > hand_landmarks.landmark[16].y and\
            hand_landmarks.landmark[18].y > hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[4].x <= hand_landmarks.landmark[13].x and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek
        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter3(): #E - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'E'
    if hand_landmarks.landmark[6].y < hand_landmarks.landmark[8].y and\
            hand_landmarks.landmark[10].y < hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[14].y < hand_landmarks.landmark[16].y and\
            hand_landmarks.landmark[18].y < hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[4].x <= hand_landmarks.landmark[13].x and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y: #bilek
        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter4(): #F - Righthand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'F'
    if hand_landmarks.landmark[8].y >= hand_landmarks.landmark[4].y >= hand_landmarks.landmark[6].y and\
            hand_landmarks.landmark[4].x >= hand_landmarks.landmark[8].x and\
            hand_landmarks.landmark[10].y > hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[14].y > hand_landmarks.landmark[16].y and\
            hand_landmarks.landmark[18].y > hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y: #bilek

        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter5(): #D - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'D'
    if hand_landmarks.landmark[4 and 12 and 16 and 20].y > hand_landmarks.landmark[8].y and\
            hand_landmarks.landmark[4 and 12 and 16 and 20].x > hand_landmarks.landmark[8].x and\
            hand_landmarks.landmark[12 and 16 and 20].y >= hand_landmarks.landmark[4].y and\
            hand_landmarks.landmark[11 and 15 and 19].x <= hand_landmarks.landmark[12 and 16 and 20].x and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y and hand_landmarks.landmark[0].y: #bilek
        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter6(): #G - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'G'
    if hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and\
            hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y and\
            hand_landmarks.landmark[8].x > hand_landmarks.landmark[6].x and\
            hand_landmarks.landmark[12].x < hand_landmarks.landmark[10].x and\
            hand_landmarks.landmark[16].x < hand_landmarks.landmark[14].x and\
            hand_landmarks.landmark[20].x < hand_landmarks.landmark[18].x and\
            hand_landmarks.landmark[6].y > hand_landmarks.landmark[4].y:
        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter7():#I Rightland
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'I'
    if hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y and\
            hand_landmarks.landmark[10].y < hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and\
            hand_landmarks.landmark [4].x <= hand_landmarks.landmark[11].x and\
            hand_landmarks.landmark [18].y > hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y: #bilek

        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter8(): #V Rigthland
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'V'
    if hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and\
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y and\
        hand_landmarks.landmark[6].y > hand_landmarks.landmark[8].y and\
        hand_landmarks.landmark[10].y > hand_landmarks.landmark[12].y and\
        hand_landmarks.landmark[11].x > hand_landmarks.landmark[15].x and\
        hand_landmarks.landmark[4].x >= hand_landmarks.landmark[14 and 18].x and\
        hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter9(): #W Rigtland
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'W'
    if hand_landmarks.landmark [20].y > hand_landmarks.landmark[17].y and\
        hand_landmarks.landmark[16 and 20 ].y >= hand_landmarks.landmark[8 and 12].y and\
        hand_landmarks.landmark[14].y > hand_landmarks.landmark[16].y and\
        hand_landmarks.landmark[10].y > hand_landmarks.landmark[12].y and\
        hand_landmarks.landmark[6].y > hand_landmarks.landmark[8].y and\
        hand_landmarks.landmark[4].x<= hand_landmarks.landmark[20].x and\
        hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter10():  #U Rigtland
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'U'
    if hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y and\
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and\
        hand_landmarks.landmark[10].y > hand_landmarks.landmark[12].y and\
        hand_landmarks.landmark[6].y > hand_landmarks.landmark[8].y and\
        hand_landmarks.landmark[4].x <= hand_landmarks.landmark[11].x and\
        hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[17].y < hand_landmarks.landmark[1].y < hand_landmarks.landmark[0].y: #bilek
     cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter11(): #L - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'L'
    if hand_landmarks.landmark[9].y < hand_landmarks.landmark[12].y and\
         hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y and\
         hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y and\
         hand_landmarks.landmark[6].y > hand_landmarks.landmark[8].y and\
         hand_landmarks.landmark[2].y > hand_landmarks.landmark[4].y and\
        hand_landmarks.landmark[4].x > hand_landmarks.landmark[5].x and\
         hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter12(): #M - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'M'
    if hand_landmarks.landmark[5].y < hand_landmarks.landmark[8].y and\
       hand_landmarks.landmark[9].y < hand_landmarks.landmark[12].y and\
       hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y and\
       hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y and\
       hand_landmarks.landmark[4].x <= hand_landmarks.landmark[15].x and\
       hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter13(): #S - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'S'
    if hand_landmarks.landmark[5].y < hand_landmarks.landmark[8].y and\
            hand_landmarks.landmark[9].y < hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y and\
            hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[4].x < hand_landmarks.landmark[11].y and\
            hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter14(): #O -RigtHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'O'
    if hand_landmarks.landmark[8 and 12 and 16 and 20].y >= hand_landmarks.landmark[4].y and\
       hand_landmarks.landmark[7 and 11 and 15 and 19].x <= hand_landmarks.landmark[8 and 12 and 16 and 20].x and\
       hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek


       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter15(): #J RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'J'
    if hand_landmarks.landmark[15].y > hand_landmarks.landmark[13].y and\
        hand_landmarks.landmark[11].y > hand_landmarks.landmark[9].y and\
        hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y and\
        hand_landmarks.landmark [17].y > hand_landmarks.landmark[20].y and\
        hand_landmarks.landmark[4].x <= hand_landmarks.landmark[7].x and\
        hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter16(): #N RigtHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'N'
    if hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y and\
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and\
        hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and\
        hand_landmarks.landmark[8].y > hand_landmarks.landmark[3].y and\
        hand_landmarks.landmark[4].x <= hand_landmarks.landmark[11 and 15].y and\
        hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)


def letter17(): #T - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'T'
    if hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y and\
            hand_landmarks.landmark[9].y < hand_landmarks.landmark[12].y and\
            hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y and\
            hand_landmarks.landmark[5].y < hand_landmarks.landmark[8].y and\
            hand_landmarks.landmark[4].x <= hand_landmarks.landmark[6].x and\
       hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter18(): #C -RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'C'
    if hand_landmarks.landmark[7 and 11 and 15 and 19].x <= hand_landmarks.landmark[8 and 12 and 16 and 20].x and\
       hand_landmarks.landmark[4].x <= hand_landmarks.landmark[5].x and\
       hand_landmarks.landmark[0].x < hand_landmarks.landmark[1].x and hand_landmarks.landmark[0].y > hand_landmarks.landmark[1].y > hand_landmarks.landmark[17].y: #bilek

       cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter19(): #P - RightHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'P'
    if hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y and\
         hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y and\
         hand_landmarks.landmark[10].y > hand_landmarks.landmark[12].y and\
        hand_landmarks.landmark[6].y > hand_landmarks.landmark[8].y and\
        hand_landmarks.landmark[4].x <= hand_landmarks.landmark[6].x:

         cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)

def letter20(): # Q - RigtHand
    font = cv2.FONT_HERSHEY_PLAIN
    text = 'Q'
    if hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y and\
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and\
        hand_landmarks.landmark[12].y >hand_landmarks.landmark[10].y and\
        hand_landmarks.landmark[5].y > hand_landmarks.landmark[8].y and\
        hand_landmarks.landmark[2].y > hand_landmarks.landmark[4].y:

        cv2.putText(image, text, (10, 50), font, 4, (0, 0, 255), 3)








def main():

    if hand_landmarks == letter1():
        letter1()
    elif hand_landmarks == letter2():
        letter2()
    elif hand_landmarks == letter3():
        letter3()
    elif hand_landmarks == letter4():
        letter4()
    elif hand_landmarks == letter5():
        letter5()
    elif hand_landmarks == letter6():
        letter6()
    elif hand_landmarks == letter7():
        letter7()
    elif hand_landmarks == letter8():
        letter8()
    elif hand_landmarks == letter9():
        letter9()
    elif hand_landmarks == letter10():
        letter10()
    elif hand_landmarks == letter11():
        letter11()
    elif hand_landmarks == letter12():
        letter12()
    elif hand_landmarks == letter13():
        letter13()
    elif hand_landmarks == letter14():
        letter14()
    elif hand_landmarks == letter15():
        letter15()
    elif hand_landmarks == letter16():
        letter16()
    elif hand_landmarks == letter17():
        letter17()
    elif hand_landmarks == letter18():
        letter18()
    elif hand_landmarks == letter19():
        letter19()
    elif hand_landmarks == letter20():
        letter20()

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:

        main()



        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == ord("q"):
      break
cap.release()
