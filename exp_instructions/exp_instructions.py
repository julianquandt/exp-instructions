import pygame
from psychopy import visual
from psychopy import event as ev

scrInfo = pygame.display.Info()
#rgb-colors
white = (255,255,255)

def quitExp():
    quitDlg = gui.Dlg(title="Quit Experiment?")
    quitDlg.addText("Quit Experiment?")
    quitDlg.show()  # show dialog and wait for OK or Cancel
    if quitDlg.OK:
        pygame.quit()
        sys.exit()
    else:
       pass


# ---------------------------------------Instructions---------------------------#


def showInstructions(Screen, aTime, instrDict, instrPath, backKey = "backspace", nextKey = "space", *args):

    page = 0
    instr_screen = Screen
    while page in range(len(instrDict.get(aTime))):

        if type(Screen) == visual.window.Window:
            while page in range(len(instrDict.get(aTime))):
                curPage = visual.SimpleImageStim(instr_screen, image=instrPath + instrDict.get(aTime)[page])
                curPage.draw()
                Screen.flip()
                instrKeys = ev.waitKeys(keyList=[backKey, nextKey, 'escape'])
                if instrKeys[0] == backKey and page > 0 and instrDict.get(aTime)[page - 1] != "trainingTime":
                    page = page - 1
                    if backKey == "y" or backKey == "9":
                        return False
                elif instrKeys[0] == nextKey:
                    page += 1
                    if nextKey == "n":
                        return True
                elif instrKeys[0] == 'escape':
                    quitExp()
        else:
            instr_page = pygame.image.load(instrPath + instrDict.get(aTime)[page]).convert_alpha()

            Screen.fill(white)
            Screen.blit(instr_page, (int(scrInfo.current_w/2-instr_page.get_rect().size[0]/2),
                                     int(scrInfo.current_h / 2 - instr_page.get_rect().size[1] / 2)))  # draw instructions page

            for arg in args:
                extra_img = pygame.image.load(arg[0]).convert_alpha()
                extra_img = pygame.transform.scale(extra_img, (arg[2][0], arg[2][1]))
                Screen.blit(extra_img, (arg[1][0], arg[1][1]))  # draw instructions page

            pygame.display.update()

            for event in pygame.event.get():  # check whether an event occurred

                # ask whether experiment should be quit when ESCAPE is pressed
                if event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    if key_name == "escape":
                        quitExp()
                    elif key_name == backKey:
                        if backKey == "y" or backKey == "9":
                            return False
                        elif page > 0:
                            page -= 1
                    elif key_name == nextKey or nextKey == "9":
                        if nextKey == "n":
                            return True
                        page += 1
