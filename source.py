import pyautogui as pgui

def locate_check(image_path : str) -> tuple:
    locate = pgui.locateOnScreen(image_path, grayscale=True, confidence=0.7, region=(3337,595,417,306))
    return locate

def image_locate_click(image_path : str) -> tuple:
    locate = locate_check(image_path)
    x, y = pgui.center(locate)
    pgui.click(x, y, duration=0.5)
    return (x, y)

def main():

    tyuuki = "./tyuukisakujo.png"
    highlight = "./hairaitosakujo.png"

    pgui.hotkey('alt', 'tab')

    
    while True:
        try:
            image_locate_click("./option.png")
            
            if locate_check(tyuuki):
                image_locate_click(tyuuki)
            elif locate_check(highlight):
                image_locate_click(highlight)
            else:
                pass
            pgui.press('home')
        except:
            break

if __name__ == "__main__":
    main()
