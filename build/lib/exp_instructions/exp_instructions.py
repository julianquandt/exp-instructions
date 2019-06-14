import pygame, os, sys
from psychopy import visual, gui
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

cwd = os.getcwd()

# ---------------------------------------Instructions---------------------------#


def showInstructions(Screen, aTime, instrDict, instrPath, backKey = "backspace", nextKey = "space", trigger_return = False, *args):
    '''

    :param Screen:          PG.Screen:  A pygame Screen object
    :param aTime:           STR:        key in a dictionary (file-name) indicating what sequence of instrucitons should be displayed
    :param instrDict:       STR:        name of the dictionary that contains the instructions
    :param instrPath:       STR:        file path to folder containing instruction images
    :param backKey:         STR:        letter or number indicating the name of the key to go back to last slide
    :param nextKey:         STR:        letter or number indicating the name of the key to go back to last slide
    :param trigger_return:  BOOL:       indicator for whether the TRUE for nextKey and FALSE for backKey should be returned
    :param args:            ARGS:       additional arguments (pictures) that can be displayed #TODO: change this to kwargs
    :return:                BOOL:       TRUE/FALSE if trigger_return = True
    '''
    page = 0
    instr_path_os = os.path.normpath(instrPath)
    instr_screen = Screen
    while page in range(len(instrDict.get(aTime))):
        instr_img_path = os.path.join(*[cwd, instr_path_os, instrDict.get(aTime)[page]])
        if type(Screen) == visual.window.Window:

            while page in range(len(instrDict.get(aTime))):
                curPage = visual.SimpleImageStim(instr_screen, image=instr_img_path)
                curPage.draw()
                Screen.flip()
                instrKeys = ev.waitKeys(keyList=[backKey, nextKey, 'escape'])
                if instrKeys[0] == backKey and page > 0 and instrDict.get(aTime)[page - 1] != "trainingTime": #TODO: edit
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
            instr_page = pygame.image.load(instr_img_path).convert_alpha()

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
                        if page > 0:
                            page -= 1
                        if trigger_return:
                            return False
                    elif key_name == nextKey:
                        page += 1
                        if trigger_return:
                            return True
