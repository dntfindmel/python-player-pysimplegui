import PySimpleGUI as sg
import os
from utils.music_utilities import get_files_inside_directory_not_recursive, play_sound, is_sound_playing, pause_sounds, stop_sounds, unpause

sg.theme('DarkPurple4')
song_title_col = [
    [sg.Text(text='Press play', justification='center', background_color='black', text_color='#B026FF',
             size=(200, 0), font='tahoma', key='song_title')],
]

info = [
    [sg.Text('Player by Melyssa Moya', background_color='black', text_color='#B026FF', font='tahoma')],
]

playing_now = [
    [sg.Text(background_color='black', size=(200, 0), text_color='#B026FF', font='tahoma, 12', key='playing_now')],
]

GO_BACK_IMAGE_PATH = 'images\\back.png'
GO_FORWARD_IMAGE_PATH = 'images\\next.png'
PLAY_SONG_IMAGE_PATH = 'images\\play.png'
PAUSE_SONG_IMAGE_PATH = 'images\\pause.png'
ALBUM_COVER_IMAGE_PATH = 'images\\8bit.png'

main = [
    [sg.Canvas(background_color='black', size=(480, 20), pad=None)],
    [sg.Column(layout=info, justification='center', element_justification='center', 
               background_color='black')],
    [
        sg.Canvas(background_color='black', size=(40, 350), pad=None),
        sg.Image(filename=ALBUM_COVER_IMAGE_PATH, size=(350, 350), pad=None),
        sg.Canvas(background_color='black', size=(40, 350), pad=None)],
    [sg.Canvas(background_color='black', size=(480, 10), pad=None)],
    [sg.Column(song_title_col, background_color='black', justification='c', element_justification='c')],
    [sg.Text('_' * 80, background_color='black', text_color='#B026FF')],
    [
        sg.Canvas(background_color='black', size=(99, 200), pad=None),
        sg.Image(pad=(10, 0), filename=GO_BACK_IMAGE_PATH, enable_events=True,
                 size=(35, 44), key='go_back', background_color='black'),
        sg.Image(filename=PLAY_SONG_IMAGE_PATH, size=(64, 64), pad=(10, 0), enable_events=True, key='play', background_color='black'),
        sg.Image(filename=PAUSE_SONG_IMAGE_PATH, size=(58, 58), pad=(10,0), enable_events=True, key='pause', background_color='black'),
        sg.Image(filename=GO_FORWARD_IMAGE_PATH, size=(35, 44), pad=(10, 0), enable_events=True, key='next', background_color='black' )],
    [sg.Column(layout=playing_now, justification='center', element_justification='center', background_color='black', pad=None)]
    
]

window = sg.Window('Python Player', layout=main, size=(480, 730), background_color='black', finalize=True, grab_anywhere=True, resizable=False,)

directory = sg.popup_get_folder('Select Your Music Directory')

directory_songs = get_files_inside_directory_not_recursive(directory)
song_count = len(directory_songs)
current_song = 0

def update_display():
    window['song_title'].update(os.path.basename(
        directory_songs[current_song]))
    window['playing_now'].update(
        f'Playing: {os.path.basename(directory_songs[current_song])}'
    )

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'play':
        if is_sound_playing():
            pass
        if is_sound_playing() == False:
            #play_sound(directory_songs[current_song])
            #update_display()
            directory = sg.popup_get_folder('Select Your Music Directory')
            

        
    elif event == 'pause':
        if is_sound_playing():
            pause_sounds()
        else:
            unpause()
        pass
        
    elif event == 'next':
        if current_song + 1 < song_count:
            stop_sounds()
            current_song += 1
            play_sound(directory_songs[current_song])
            update_display()
                
        else:
            print('Reached last song')
        pass
        
    elif event == 'go_back':
        if current_song + 1 <= song_count and current_song > 0:
            stop_sounds()
            current_song -= 1
            play_sound(directory_songs[current_song])
            update_display()
        else:
            print('Reached first song')
    