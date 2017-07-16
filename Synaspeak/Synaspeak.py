# Synaspeak : A Low Wireless Assitive Device for users with Motor Neuron Disabilities using Electro-encephelographic(EEG) methods.
# Synaspeak Developer  : Geeve George
# Credits for Customized Neurosky Python Libraries : Gabriel Maggiotti <gabriel.maggiotti@mercadolibre.com>
# Requirements : Python IDLE 2.7, Bluetooth Libraries (PyBluez), Neurosky Mindwave Headset, Espeak TTS Library, Pyttsx Library    

from MindwaveBLConnector import NeuroskyConnector
from bluetooth.btcommon import BluetoothError
from Syna_parser import  ThinkGearParser, TimeSeriesRecorder
import Syna_blink, Syna_states
from Talk import Talk

import array
import time
import os #for e-speak





conn = NeuroskyConnector()
socket = conn.getConnectionInstance()
recorder = TimeSeriesRecorder()
parser = ThinkGearParser(recorders= [recorder])


w = Syna_blink.Wink()
s = Syna_states.States()
t = Talk()

msg_array = []
wrd_array = []

list_counter = 0
msg_counter = 0
wrd_counter = 0
dash = '-'
dot = '.'

dot_counter = 0
dash_counter = 0
nb_counter = 0


def findexact(msg_array,morse):    #a function that checks if content of msg_array and morse are an exact match
    i=0
    while i < len(msg_array):
        if any(item == msg_array[i] for item in morse):
            return 1
        i+=1

def findexactword(wrd_array,word):    #a function that checks if content of wrd_array and word are an exact match
    j=0
    #print('Inside Find Exact Word')
    while j < len(wrd_array):
        if any(items == wrd_array[j] for items in word):
            return 1
        j+=1

#functions to clear msg & word lists
def clear_ar():
    del msg_array[:]


def clear_wrdar():
    del wrd_array[:]


def insert_wrd(wrd_array,letter):    #a function that concatinates word input


    food = ['FD']
    hay = ['HAY']
    iaf = ['IAF']
    wt = ['WT']
    
    global wrd_counter
    if(wrd_counter==0):
        wrd_array.append(letter)

    else:
        wrd_array = [x + letter for x in wrd_array]
    wrd_counter+=1

#Short command checking by giving a function call to 'findexactword()' , if returns true then: text to speech output using 'e-speak'

    if (findexactword(wrd_array,food)==1):
        print('I want food')
        os.system("espeak 'I want food'")
        wrd_counter=0
        clear_wrdar()

    elif (findexactword(wrd_array,hay)==1):
        print('How are you?')
        os.system("espeak 'How are you'")
        wrd_counter=0
        clear_wrdar()

    elif (findexactword(wrd_array,iaf)==1):
        print('I am fine')
        os.system("espeak 'I am fine'")
        wrd_counter=0
        clear_wrdar()

    elif (findexactword(wrd_array,wt)==1):
        print('I want water')
        os.system("espeak 'I want water'")
        wrd_counter=0
        clear_wrdar()

    elif (wrd_counter==2):
        wrd_counter=0
        clear_wrdar()

    print('Word : ')
    print(wrd_array)        
        



while socket is not None:
    try:
        data = socket.recv(1000)
        parser.feed(data)


        max = recorder.raw[-100:].max()
        if( w.detectWink(max) ):
            s.addWink()
        count = s.getWinkWithinDelta()

        m_a = ['.-']
        m_b = ['-...']
        m_c = ['-.-.']
        m_d = ['-..']
        m_e = ['.']
        m_f = ['..-.']
        m_g = ['--.']
        m_h = ['....']
        m_i = ['..']
        m_j = ['.---']
        m_k = ['-.-']
        m_l = ['.-..']
        m_m = ['--']
        m_n = ['-.']
        m_o = ['---']
        m_p = ['.--.']
        m_q = ['--.-']
        m_r = ['.-.']
        m_s = ['...']
        m_t = ['-']
        m_u = ['..-']
        m_v = ['...-']
        m_w = ['.--']
        m_x = ['-..-']
        m_y = ['-.--']
        m_z = ['--..']

        l_a = 'A'
        l_b = 'B'
        l_c = 'C'
        l_d = 'D'
        l_e = 'E'
        l_f = 'F'
        l_g = 'G'
        l_h = 'H'
        l_i = 'I'
        l_j = 'J'
        l_k = 'K'
        l_l = 'L'
        l_m = 'M'
        l_n = 'N'
        l_o = 'O'
        l_p = 'P'
        l_q = 'Q'
        l_r = 'R'
        l_s = 'S'
        l_t = 'T'
        l_u = 'U'
        l_v = 'V'
        l_w = 'W'
        l_x = 'X'
        l_y = 'Y'
        l_z = 'Z'
        
        if(dot_counter+dash_counter>=5 or nb_counter == 3):

            print(msg_array)

            if (findexact(msg_array,m_a)==1):    #checking for morse combination match and if true, text to speech speaks the correponding english alphabet

                print('A')
                os.system("espeak 'A'")
                insert_wrd(wrd_array,l_a)

            elif (findexact(msg_array,m_b)==1):
                print('B')
                os.system("espeak 'B'")
                insert_wrd(wrd_array,l_b)

            elif (findexact(msg_array,m_c)==1):
                print('C')
                os.system("espeak 'C'")
                insert_wrd(wrd_array,l_c)

            elif (findexact(msg_array,m_d)==1):
                print('D')
                os.system("espeak 'D'")
                insert_wrd(wrd_array,l_d)

            elif (findexact(msg_array,m_e)==1):
                print('E')
                os.system("espeak 'E'")
                insert_wrd(wrd_array,l_e)

            elif (findexact(msg_array,m_f)==1):
                print('F')
                os.system("espeak 'F'")
                insert_wrd(wrd_array,l_f)

            elif (findexact(msg_array,m_g)==1):
                print('G')
                os.system("espeak 'G'")
                insert_wrd(wrd_array,l_g)

            elif (findexact(msg_array,m_h)==1):
                print('H')
                os.system("espeak 'H'")
                insert_wrd(wrd_array,l_h)

            elif (findexact(msg_array,m_i)==1):
                print('I')
                os.system("espeak 'I'")
                insert_wrd(wrd_array,l_i)

            elif (findexact(msg_array,m_j)==1):
                print('J')
                os.system("espeak 'J'")
                insert_wrd(wrd_array,l_j)

            elif (findexact(msg_array,m_k)==1):
                print('K')
                os.system("espeak 'K'")
                insert_wrd(wrd_array,l_k)

            elif (findexact(msg_array,m_l)==1):
                print('L')
                os.system("espeak 'L'")
                insert_wrd(wrd_array,l_l)

            elif (findexact(msg_array,m_m)==1):
                print('M')
                os.system("espeak 'M'")
                insert_wrd(wrd_array,l_m)

            elif (findexact(msg_array,m_n)==1):
                print('N')
                os.system("espeak 'N'")
                insert_wrd(wrd_array,l_n)

            elif (findexact(msg_array,m_o)==1):
                print('O')
                os.system("espeak 'O'")
                insert_wrd(wrd_array,l_o)

            elif (findexact(msg_array,m_p)==1):
                print('P')
                os.system("espeak 'P'")
                insert_wrd(wrd_array,l_p)

            elif (findexact(msg_array,m_q)==1):
                print('Q')
                os.system("espeak 'Q'")
                insert_wrd(wrd_array,l_q)

            elif (findexact(msg_array,m_r)==1):
                print('R')
                os.system("espeak 'R'")
                insert_wrd(wrd_array,l_r)

            elif (findexact(msg_array,m_s)==1):
                print('S')
                os.system("espeak 'S'")
                insert_wrd(wrd_array,l_s)

            elif (findexact(msg_array,m_t)==1):
                print('T')
                os.system("espeak 'T'")
                insert_wrd(wrd_array,l_t)

            elif (findexact(msg_array,m_u)==1):
                print('U')
                os.system("espeak 'U'")
                insert_wrd(wrd_array,l_u)

            elif (findexact(msg_array,m_v)==1):
                print('V')
                os.system("espeak 'V'")
                insert_wrd(wrd_array,l_v)

            elif (findexact(msg_array,m_w)==1):
                print('W')
                os.system("espeak 'W'")
                insert_wrd(wrd_array,l_w)

            elif (findexact(msg_array,m_x)==1):
                print('X')
                os.system("espeak 'X'")
                insert_wrd(wrd_array,l_x)

            elif (findexact(msg_array,m_y)==1):
                print('Y')
                os.system("espeak 'Y'")
                insert_wrd(wrd_array,l_y)

            elif (findexact(msg_array,m_z)==1):
                print('Z')
                os.system("espeak 'Z'")
                insert_wrd(wrd_array,l_z)

            else:    #if no match found
                print('Not valid morse combination')

            clear_ar()
            
            msg_counter=0
            dash_counter=0
            dot_counter=0
            nb_counter=0
            list_counter=0
            

                
            

                
#------------------------------------Detecting Blinks---------------#
            
        if( count == 2 ):
            print('.')
            dot_counter+=1

            if(list_counter==0):
                msg_array.append('.')
                msg_counter+=1

            else:
                msg_array = [x + dot for x in msg_array]

            list_counter+=1    

            
        elif( count == 3 ):
            print('-')
            dash_counter+=1

            if(list_counter==0):
                msg_array.append('-')
                msg_counter+=1

            else:
                msg_array = [x + dash for x in msg_array]

            list_counter+=1

            
        elif( count==4 ):
            print('Converting Morse to English...')
            nb_counter = 3


        elif( count==5):
            print('Clearing msg and wrd arrays...')
            clear_ar()
            clear_wrdar()
            

                    
                              
                
        count = 0      


    except BluetoothError:
        pass


