"""
 
All coordinates assume a screen resolution of 1920x1080, and Firefox 
maximized with the Bookmarks Toolbar disabled and a zoom of 100%.
"""

import ImageGrab
import os
import time
import win32api, win32con, win32clipboard
import ImageOps
from numpy import *
import random
import urllib2

#main function - run this to start the program
def startTheWarpDrive():
    a = screenGrab();
    #while (a.getpixel((1058, 567)) != (255, 255, 255)):
    while (a.getpixel((1283, 917)) != (255, 255, 255)):
        a = screenGrab();
        #setMouse(676, 174);
        #time.sleep(0.1);
        #leftClick();
        time.sleep(2);

    print "YOU DID A THING";
    #setMouse(757, 569);
    setMouse(748, 922);
    time.sleep(0.1);
    leftClick();
    time.sleep(0.1);
    leftClick();
    time.sleep(0.1);
    leftClick();
    time.sleep(0.1);
    pressKey("ctrl");
    pressKey("c");
    time.sleep(0.1);
    depressKey("ctrl");
    depressKey("c");

    win32clipboard.OpenClipboard();
    inp = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT);
    win32clipboard.CloseClipboard();

    arr = inp.split(' ');

    if (arr[0] == "connect"):
        response = urllib2.urlopen(arr[1]);
        html = response.read();
        print html;

        urlArr = list(split_by_n(html, 320));

        for i in range(0, len(urlArr)):
            win32clipboard.OpenClipboard();
            win32clipboard.EmptyClipboard();
            win32clipboard.SetClipboardText(urlArr[i], win32clipboard.CF_UNICODETEXT);
            win32clipboard.CloseClipboard();

            #setMouse(720, 651);
            setMouse(1007, 1001);
            leftClick();
            time.sleep(0.1);
            pressKey("ctrl");
            pressKey("v");
            time.sleep(0.1);
            depressKey("ctrl");
            depressKey("v");

            toggleKey("enter");

            time.sleep(0.1);
            setMouse(1909, 1029);
            time.sleep(0.1);
            leftClick();

    #elif (arr[0] == "search"):

    else:
        setMouse(720, 651);
        leftClick();
        type("I'm sorry, I can't do that Dave.");
        toggleKey("enter");



def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n];
        seq = seq[n:];

# base functions

xPad = 0;
yPad = 0;

def getRand(a, b):
    return int(math.floor((random.random() * (b - a + 1)) + a));

def getRandFloat(a, b):
    return ((random.random() * (b - a)) + a);

def type(string):
    for i in range (0, len(string)):
        isShifty = string[i] in VK_CODE.keys();
        isShifty = not isShifty;
        if (string[i].isupper() | isShifty):
            shiftKey(string[i].lower());
        else:
            toggleKey(string[i]);

def shiftKey(char):
    if char in VK_CODE.keys():
        win32api.keybd_event(0xA0, 0, 0, 0);
        toggleKey(char);
        win32api.keybd_event(0xA0, 0, 2, 0);
    elif char in SHIFT.keys():
        win32api.keybd_event(0xA0, 0, 0, 0);
        toggleKeyManual(SHIFT[char]);
        win32api.keybd_event(0xA0, 0, 2, 0);
    else:
        print "ERROR: Attempted to type unknown character '" + char + "'.";

def toggleKey(key):
    toggleKeyManual(VK_CODE[key]);

def toggleKeyManual(key):
    win32api.keybd_event(key, 0, 0, 0);
    time.sleep(0.1);
    win32api.keybd_event(key, 0, 2, 0);

def pressKeyManual(key):
    win32api.keybd_event(key, 0, 0, 0);

def depressKeyManual(key):
    win32api.keybd_event(key, 0, 2, 0);

def pressKey(key):
    pressKeyManual(VK_CODE[key]);

def depressKey(key):
    depressKeyManual(VK_CODE[key]);
    

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
    time.sleep(.1);
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);
    print "Click.";

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
    time.sleep(.1);
    print 'left Down';
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);
    time.sleep(0.1);
    print 'left release';

def setMouse(x, y):
    win32api.SetCursorPos((xPad + x, yPad + y));

def getMouse():
    x,y = win32api.GetCursorPos();
    x = x - xPad;
    y = y - yPad;
    print "Accessed mouse at x: " + str(x) + " y: " + str(y);

def screenGrab():
    box = (0, 0, 1920, 1080);
    im = ImageGrab.grab(box);
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im;

# holds all keyboard codes

SHIFT = {')':0x30,
         '!':0x31,
         '@':0x32,
         '#':0x33,
         '$':0x34,
         '%':0x35,
         '^':0x36,
         '&':0x37,
         '*':0x38,
         '(':0x39,
         ':':0xBA
         };

VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           ' ':0x20,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0
           };

def main():
    pass;
 
if __name__ == '__main__':
    main();
