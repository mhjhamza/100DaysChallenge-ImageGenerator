import cv2
import imutils

def generate_image(challenge_name = 'MLCode', current_day = 100, background_image = 'red'):

    border_image_path = 'text_'+ str(current_day) +'.png'
    background_image_path = background_image + '.png'

    border_mask = cv2.imread(border_image_path, cv2.COLOR_RGB2GRAY)
    background_image = cv2.imread(background_image_path)

    background_image[border_mask >= 125] = (255)
    h,w,c = background_image.shape

    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 3
    fontColor              = (255,255,255)
    lineType               = 5
    text = '#100DaysOf' + challenge_name 
    text_w, text_h = cv2.getTextSize(text, font, fontScale, lineType)[0]
    center = ( int(w/2) - int(text_w/ 2),200)
    cv2.putText(background_image, text, 
        center, 
        font, 
        fontScale,
        fontColor,
        lineType)


    cv2.imshow('To-Be-Downloaded', background_image)
    cv2.imwrite('To-Be-Downloaded.jpg', background_image)
    cv2.waitKey()

generate_image()