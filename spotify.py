from os import system, name
from pytify.strategy import get_pytify_class_by_platform
from pytify.dbus.metadata import Metadata
import time

spotify = get_pytify_class_by_platform()()
spotify.metadata = Metadata()
metadata = spotify.metadata.get_metadata()

def clear():

		if name == "nt":
			_ = system("cls")

		else:
			_ = system("clear")

while True:
	print("Please choose an option:\n\n")
	print("1. Informations about the song that is being played.")
	print("2. Interact with Spotify app.")


	print("\n\n")
	choice=input()
	clear()

	if choice=="1":
		song=spotify.metadata.get_current_playing()
		album=metadata['xesam:album']
		songlength=(metadata['mpris:length']/(10**6))/60
		trackid=metadata['mpris:trackid']
		trackurl=metadata['xesam:url']

		print(f"Name of the song:\t\t|	{song}\n")
		print(f"Album:\t\t\t\t|	{album}\n")
		print(f"Song length:\t\t\t|	{songlength}\n")
		print(f"Track id:\t\t\t|	{trackid}\n")
		print(f"Track url:\t\t\t|	{trackurl}\n")

		while True:
			time.sleep(10)
			spotify2=get_pytify_class_by_platform()
			spotify2.metadata=Metadata()
			metadata2 = spotify.metadata.get_metadata()
			song2=spotify.metadata.get_current_playing()
			album2=metadata2['xesam:album']
			songlength2=(metadata2['mpris:length']/(10**6))/60
			trackid2=metadata2['mpris:trackid']
			trackurl2=metadata2['xesam:url']

			if song!=song2:
				clear()
				print(f"Name of the song:\t\t|	{song2}\n")
				print(f"Album:\t\t\t\t|	{album2}\n")
				print(f"Song length:\t\t\t|	{songlength2}\n")
				print(f"Track id:\t\t\t|	{trackid2}\n")
				print(f"Track url:\t\t\t|	{trackurl2}\n")
				song=song2;


	if choice=="2":


		print(f"1. Play/pause the song.")
		print(f"2. Skip the song.")
		print(f"3. Play the previous song.")

		interact=input()

		if interact=="1":
			print("The song is played/paused.")
			spotify.play_pause()

		elif interact=="2":
			print(f"Playing now the next song.")
			spotify.next()

		elif interact=="3":
			print(f"Playing now the previous song.")
			spotify.prev()

	print("\n\n")
	input("Press any key to continue.")

	clear()