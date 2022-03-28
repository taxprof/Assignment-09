#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Tessa D, Mar 2022, modified for assignment 09
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    #displays menu
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
            
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        
        #subloop that processes CD track data 
        
        while True: 
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            #displays the submenu
            
            #adds track info to CD
            if strChoice == 'a': 
                tplTrack = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrack,cd)
                continue
            
            #displays track data
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue
            
            #removes track from CD
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                
                try:
                    intTrackIndex = int(input('Please select a track from the list\n'))
                    cd.remove_track(intTrackIndex)
                except: 
                    print('Error: Please enter an integer')
                    
                continue
                
            elif strChoice == 'x':
                break
            
            else:
                print('Error: Selection not available. Please select from the list.\n')
                

        
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        
    else:
        print('General Error')