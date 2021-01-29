from os import system, name
from pytify.strategy import get_pytify_class_by_platform
from pytify.dbus.metadata import Metadata
import time
import PySimpleGUI as gui

gui.theme('DarkAmber')

spotify = get_pytify_class_by_platform()()
spotify.metadata = Metadata()
metadata = spotify.metadata.get_metadata()

song=spotify.metadata.get_current_playing()
album=metadata['xesam:album']
songlength=(metadata['mpris:length']/(10**6))/60
trackid=metadata['mpris:trackid']
trackurl=metadata['xesam:url']


layout = [	[gui.Text(f"Name of the song: {song}.", key='-SONG-')],
			[gui.Text(f"Album: {album}.", key='-ALBUM-')],
			[gui.Text(f"Song length: {songlength}.", key='-LENGTH-')],
			[gui.Text(f"Track id: {trackid}.", key='-TRACKID-')],
			[gui.Text(f"Track url: {trackurl}.", key='-TRACKURL-')],
			[gui.Button("Refresh")],
            [gui.Button("Next song")],
            [gui.Button("Previous song")],
			[gui.Button("Exit")]
		 ]

window = gui.Window('Spotify Helper', layout)



def clear():

		if name == "nt":
			_ = system("cls")

		else:
			_ = system("clear")


while True:
    event, values = window.read()
    print(event, values)
    if event == gui.WIN_CLOSED or event == 'Exit':
        break


    if event == 'Refresh':
        spotify2 = get_pytify_class_by_platform()
        spotify2.metadata = Metadata()
        metadata2 = spotify.metadata.get_metadata()
        song2 = spotify.metadata.get_current_playing()
        album2 = metadata2['xesam:album']
        songlength2 = (metadata2['mpris:length']/(10**6))/60
        trackid2 = metadata2['mpris:trackid']
        trackurl2 = metadata2['xesam:url']

        window['-SONG-'].update(f"Name of the song: {song2}.")
        window['-ALBUM-'].update(f"Album: {album2}.")
        window['-LENGTH-'].update(f"Song length: {songlength2}.")
        window['-TRACKID-'].update(f"Track id: {trackid2}.")
        window['-TRACKURL-'].update(f"Track url: {trackurl2}.")



    if event == 'Next song':
        spotify.next()

    if event == 'Previous song':
        spotify.prev()
