"""
	3 November 2018
	Retrieves list of .mp3 files converted from YouTube with missing metadata,
	in the format "Artist - Song Name (Video).mp3" eyed3 and updates title and 
	artist names
"""

try:
    import os
    import eyed3

    # get current path
    currentPath = os.getcwd()
    print(currentPath)
    
	# arrange all files (assuming they are .mp3) into a list
    from os import listdir
    allFiles = os.listdir(currentPath)
    
	# # list all current files
    # print("\nCURRENT CONFIGURATION\n")
	
	# # enumerate(stuff) returns an index counter too
    # for i, file in enumerate(allFiles):
        # print(str(i) + ": " + file)
		
    # filter music and change if pirated or converted
    print("\nCHANGE IMPLEMENTATION\n")

    for i, file in enumerate(allFiles):
        # print("Current: " + file)

		# check for converted youtube to mp3 format "artist - name.mp3"
        if " - " in file:
            theArtist = []
            theTitle = []
            
            # determine artist name
            location = file.find(" - ") # returns -1 if not found
            # print("Dash '-' at location {}: ".format(location) + file)
            theArtist = file[:(location)]
            
			# check for bracketted video tag and determine song title
            if "video)" in file.lower():
                locationVid = file.find("(")
                theTitle = file[location + 3:locationVid - 1]
                print("Bracketted video found!")
            
            # without bracketted video tags
            else:
                theTitle = file[location + 3:-4] # -4 to ignore .mp3
                print("Non-bracketted video.")
				
            try:
                audiofile = eyed3.load(file)
                audiofile.tag.title = theTitle
                audiofile.tag.artist = theArtist
                audiofile.tag.save()
                os.rename(file, (theTitle + ".mp3")) # rename file; .mp3 needed to specify file format, else id3 unavailable			
            
            # Note: special characters like é will trigger exception
            except AttributeError: # in the event tag has no attribute
                print("Error, unable to process: {}. Please do manually.".format(file))
                continue

    print("Code completed.")

except KeyboardInterrupt:
	pass