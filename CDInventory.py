#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Gleque, 2022-Dec-04, added code and changed 9 TODO's to TODone
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
file_name = ''


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        @staticmethod def cd_id
        @staticmethod def cd_title
        @staticmethod def cd_artist
    """
    # TODone Add Code to the CD class
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = int(cd_id)
        self.cd_title = str(cd_title)
        self.cd_artist = str(cd_artist)
    
    @staticmethod
    def cd_id(self):
      return self.cd_id
    
    @staticmethod
    def cd_title(self):
        return self.cd_title
    
    @staticmethod
    def cd_artist(self):
        return self.cd_artist
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    def load_inventory(file_name):
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = CD(data[0],data[1],data[2])
                lstOfCDObjects.append(dicRow)
            objFile.close()
        except:
         print('No such file exists in that directory')
        
    # TODone Add code to process data to a file
    def save_inventory(file_name):
       """Saves inventory to file
       Arguments:
           file_name
           list
       Returns:
           None.
       """
    try:
        objFile = open(file_name, 'w')
        for row in list:
            lstValues = []
            lstValues.extend([row.cd_id, row.cd_title, row.cd_artist])
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
    except:
        print('No such file exists in that directory')
   


# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
    # TODone add code to show menu to user
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
            
        print()  # Add extra space for layout
        return choice
    
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(lstOfCDObjects):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstOfCDObjects:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    # TODone add code to get CD data from user
    @staticmethod
    def addnew_cd():
        """Allows user to add a cd; includes exception handling if user inputs something erroneous
        
        Args:
            None
            
        Returns:
            intID: Integer that defines CD "row"
            strTitle: string data name of title of CD
            strArtist: string data name of artist
        """
        try:
            intID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
        except:
            print('incorrect input; try again')
        return intID, strTitle, strArtist

# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')  
    elif strChoice == 'a': 
        ID, strTitle, strArtist = IO.addnew_cd()
        IO.addnew_cd(ID, strTitle, strArtist)      
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)     
    elif strChoice == 's':  
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower() 
        if strYesNo == 'y':    
            FileIO.save_inventory(strFileName)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')