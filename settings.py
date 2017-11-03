"""
Settings class

Read optional config file which simply lists options in
the following way:

SETTING1=value1
SETTING2=value2
etc.
"""
from requests import structures
from copy import copy
from pygame.colordict import THECOLORS as COLORS


class SettingsError(ValueError):
    pass


class Settings:
    def __init__(self, config_file=None):
        # defaults holds a case insensitive dictionary
        self.__defaults = structures.CaseInsensitiveDict()
        default_values = (('FPS', 30),
                          ('WINDOWWIDTH', 1024),
                          ('WINDOWHEIGHT', 768),
                          ('YMAX', 1),
                          ('BACKGROUND', 'black'),
                          ('buttonCount', 10),
                          ('buttonGap', 10),
                          ('buttonWidth', 40),
                          ('buttonHeight', 40))

        self.__defaults['FPS'] = 30
        self.__defaults['WINDOWWIDTH'] = 1024
        self.__defaults['WINDOWHEIGHT'] = 768
        self.__defaults['YMAX'] = 1
        self.__defaults['BACKGROUND'] = 'black'

        self.__settings = copy(self.__defaults)
        if config_file is not None:
            # TODO: Copy value from config file
            # TODO: Security sanity check. Make sure all values in config file exist in defaults dict
            pass

        self._sanity_check()
        self._calculated_values()

    def _sanity_check(self):
        if self.__settings['BACKGROUND'] not in colordict:
            raise SettingsError('{} is not a valid color.'.format(self.__settings['BACKGROUND']))

        # Types
        int_types = ['FPS', 'WINDOWWIDTH', 'WINDOWHEIGHT', 'YMAX',
                     'buttonCount', 'buttonGap', 'buttonWidth', 'buttonHeight']
        for t in int_types:
            try:
                self.__settings[t] = int(self.__settings[t])
            except Exception as e:
                raise SettingsError('Setting {} with value {} is not an integer.'.format(t, self.__settings[t]))

        # Colors
        color_types = ('BACKGROUND',)
        for c in color_types:
            try:
                if self.__settings[c] not in COLORS:
                    raise SettingsError('Not a valid color')
            except SettingsError:
                raise SettingsError('Setting {} with value {} is not a color.'.format(c, self.__settings[c]))

    def _calculated_values(self):
        try:
            # TODO: Replace with a safe version of numexpr or AST
            self.__settings['XMAX'] = self.__settings['WINDOWWIDTH'] / self.__settings['WINDOWHEIGHT'] * self.__settings['YMAX']
        except Exception as e:
            raise SettingsError('Error calculated XMAX: {}'.format(e))

        try:
            # TODO: Replace with a safe version of numexpr or AST
            WINDOWWIDTH = self.__settings['WINDOWWIDTH']
            buttonWidth = self.__settings['buttonWidth']
            buttonGap = self.__settings['buttonGap']
            self.__settings['buttonMargin'] = (WINDOWWIDTH - (buttonWidth * 10 + buttonGap * 9)) // 2
        except Exception as e:
            raise SettingsError('Error calculated XMAX: {}'.format(e))

    def settings(self):
        # Make an immutable dictionary so people can't fuck with the settings.
        return copy(self.__settings)