import sys
import traceback

from io import StringIO

import pygame
import pygame_gui

from pygame_gui.elements import UITextBox

class stocks(pygame_gui.elements.UIWindow):
    def __init__(self, pos, manager):
        super().__init__(
            pygame.Rect(pos, (400,300)),
            manager,
            window_display_title='stocks',
            object_id='#stocks',
            resizable=True
        )
        self.instructions = pygame_gui.elements.ui_label.UILabel(
            relative_rect=pygame.Rect(0, 0, 368, 50),
            text="Type in a NYSE Stock Symbol to get Started!",
            manager=manager,
            container=self,
            object_id='#intructions',
            anchors={
                'left': 'left',
                'right': 'right',
                'top': 'top',
                'bottom': 'bottom'
            }
        )
        print("Enter Name of Stock to Continue!")
        self.input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(0, -35, 368, 30),
            manager=manager,
            container=self,
            anchors={
                'left': 'left',
                'right': 'right',
                'top': 'bottom',
                'bottom': 'bottom'
            }
        )


