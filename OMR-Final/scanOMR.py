import numpy as np
import cv2
import utilities

###############################################
a, b, c, d, e = 0, 1, 2, 3, 4
imgWidth, imgHeight = 600, 700
questions, choices = 10, 5
ans = [c, c, a, d, c, b, d, a, d, c]


###############################################


def read(filename):
    img = cv2.imread(filename)
    return img


def scan(img, saveImgPath):
    # PRE-PROCESSING:
    img = cv2.resize(img, (imgWidth, imgHeight))
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 10, 50)
    imgFinal = img.copy()

    # FINDING ALL CONTOURS:
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)

    # FINDING RECTANGLES:
    rectCon = utilities.rectContour(contours)
    biggestContour = utilities.getCornerPoints(rectCon[0])
    gradePoint = utilities.getCornerPoints(rectCon[1])

    if biggestContour.size != 0 and gradePoint.size != 0:
        cv2.drawContours(imgBiggestContours, biggestContour, -1, (0, 255, 0), 25)
        cv2.drawContours(imgBiggestContours, gradePoint, -1, (255, 0, 0), 25)

        biggestContour = utilities.reorder(biggestContour)
        gradePoint = utilities.reorder(gradePoint)

        # TRANSFORMING PERSPECTIVE:
        p1 = np.float32(biggestContour)
        p2 = np.float32([[0, 0], [imgWidth, 0], [0, imgHeight], [imgWidth, imgHeight]])
        matrix = cv2.getPerspectiveTransform(p1, p2)
        imgWarpColor = cv2.warpPerspective(img, matrix, (imgWidth, imgHeight))

        gp1 = np.float32(gradePoint)
        gp2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
        matrixG = cv2.getPerspectiveTransform(gp1, gp2)
        imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))
        # cv2.imshow("Grade",imgGradeDisplay)

        # APPLY THRESHOLD:
        imgWarpGray = cv2.cvtColor(imgWarpColor, cv2.COLOR_BGR2GRAY)
        imgThresh = cv2.threshold(imgWarpGray, 170, 255, cv2.THRESH_BINARY_INV)[1]

        # GETTING NON-ZERO PIXEL VALUES:

        boxes = utilities.splitBoxes(imgThresh, questions, choices)

        myPixelVal = np.zeros((questions, choices))
        countC, countR = 0, 0
        for image in boxes:
            totalPixels = cv2.countNonZero(image)
            myPixelVal[countR][countC] = totalPixels
            countC += 1
            if countC == choices:
                countR += 1
                countC = 0

        # FINDING INDEX OF MARKINGS:
        myIndex = []
        for x in range(0, questions):
            arr = myPixelVal[x]
            myIndexVal = np.where(arr == np.amax(arr))
            myIndex.append(myIndexVal[0][0])

        # GRADING:
        score = 0
        grading = []
        for q in range(questions):
            option = myIndex[q]
            if option == ans[q]:
                score += 4
                grading.append(1)
            elif option == e:
                score += 0
                grading.append(0)
            else:
                score -= 1
                grading.append(0)
        if score < 0:
            score = 0

        percentage = (score / 40) * 100

        # DISPLAYING ANSWERS:
        imgResult = imgWarpColor.copy()
        utilities.showAnswers(imgResult, myIndex, grading, ans, questions, choices)
        imgRawDrawing = np.zeros_like(imgWarpColor)
        utilities.showAnswers(imgRawDrawing, myIndex, grading, ans, questions, choices)

        imgRawGrade = np.zeros_like(imgGradeDisplay)
        cv2.putText(imgRawGrade, str(score), (70, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 3)

        # INVERSE PERSPECTIVE:
        invMatrix = cv2.getPerspectiveTransform(p2, p1)
        imgInvWarp = cv2.warpPerspective(imgRawDrawing, invMatrix, (imgWidth, imgHeight))
        invMatrixG = cv2.getPerspectiveTransform(gp2, gp1)
        imgInvGradeWarp = cv2.warpPerspective(imgRawGrade, invMatrixG, (imgWidth, imgHeight))

        imgFinal = cv2.addWeighted(imgFinal, 0.5, imgInvWarp, 1, 0)
        imgFinal = cv2.addWeighted(imgFinal, 0.5, imgInvGradeWarp, 1, 0)
        cv2.imwrite(saveImgPath, imgFinal)

    return score, percentage

