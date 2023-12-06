import tkinter, random, time

cv_width = 500
cv_height = 600
santa1_y = 66
santa2_y = cv_height - 66
santa3_y = 66
santa_posun = 2

cv = tkinter.Canvas(width=cv_width, height=cv_height)
cv.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa1 = cv.create_image(cv_width * 1 // 6, santa1_y, image=image_santa)
santa2 = cv.create_image(cv_width * 3 // 6, santa2_y, image=image_santa)
santa3 = cv.create_image(cv_width * 5 // 6, santa3_y, image=image_santa)
while True:
    cv.update()
    time.sleep(0.01)
    cv.move(santa1, 0, santa_posun)
    cv.move(santa2, 0, -1 * santa_posun)
    cv.move(santa3, 0, santa_posun)
    santa1_y += santa_posun
    santa2_y -= santa_posun
    santa3_y += santa_posun
    if santa1_y == cv_height - 66:
        cv.delete(santa1)
        cv.delete(santa2)
        cv.delete(santa3)
        santa1 = cv.create_image(cv_width * 1 // 6, santa1_y, image=image_santa)
        santa2 = cv.create_image(cv_width * 3 // 6, cv_height - 66, image=image_santa)
        santa3 = cv.create_image(cv_width * 5 // 6, 66, image=image_santa)
        while santa1_y >= 0:
            cv.update()
            time.sleep(0.01)
            cv.move(santa1, 0, -1 * santa_posun)
            cv.move(santa2, 0, -1 * santa_posun)
            cv.move(santa3, 0, santa_posun)
            santa1_y -= santa_posun
            santa2_y -= santa_posun
            santa3_y += santa_posun
            if santa1_y == 66:
                cv.delete(santa1)
                cv.delete(santa2)
                cv.delete(santa3)
                santa1 = cv.create_image(cv_width * 1 // 6, santa1_y, image=image_santa)
                santa2 = cv.create_image(cv_width * 3 // 6, cv_height - 66, image=image_santa)
                santa3 = cv.create_image(cv_width * 5 // 6, 66, image=image_santa)


cv.mainloop()