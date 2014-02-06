"""
Tamer Wahba
twahba1@binghamton.edu
Michael Mones
mmones1@binghamton.edu

Analysis

A deck of 33 cards labeled from 3 to 35 is shuffled. Then 9 cards are
removed. Each player starts with 11 chips. On each turn the player has
2 options: to put down one of the chips or take the card. Chips count as
-1 point each while the cards count as positive face value, and unbroken
number sequences are counted as the lowest number of the sequence only.
The winner is the player who has the least points after all cards have
been dealt.

The UI is separated into pages, sequentially, buttons are used to invoke
methods that validate data and go to forwards or backwards in the page order

Uses
classes
 game
 player
 card
 collections.Counter
modules
 tkinter
 tikinter.dialog
 tkinter.messagebox
 tkinter.ttk
 urllib.request
 urllib.parse
"""
from game import *
from player import *
from card import *
from tkinter import *
from tkinter.dialog import *
from collections import Counter
import tkinter.messagebox as messagebox
from tkinter.ttk import *
import urllib.request
import urllib.parse

DEFAULT_PLAYERS = 3
MIN_PLAYERS = 3
MAX_PLAYERS = 5
MAX_NAME_LENGTH = 10

# windows and widget dimensions
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 400
GAME_WIDTH = 550
GAME_HEIGHT = 200
ENTRY_DIVIDER = 16

# Indexes for widgets of players
RADIO = 0
CARDS_VAR = 1
CARDS_LBL = 2
CHIPS_VAR = 3
CHIPS_LBL = 4
FRAME = 5

SPACE = " "

# Dialog box options
SAME_PLAYERS = 0
NEW_PLAYERS = 1
QUIT = 2
MAIN_MENU = 3
UPLOAD = 4

URL = 'http://127.0.0.1:8000/games/highscores'

RULES = 'A deck of 33 cards labeled from 3 to 35 is shuffled. Then 9 random '\
        'cards are removed from each game. Each player starts with 11 chips. '\
        'On each turn the player has 2 options: to put down one of the chips '\
        'to pass his turn or take the card. Chips count as -1 point each '\
        'while the cards count as positive face value, and unbroken number '\
        'sequences are counted as the lowest number of the sequence only. '\
        'The winner is the player who has the least points after all cards '\
        'have been dealt.'


class MainWindow:
    """Main window for No Thanks game"""
    def __init__(self):
        self.__window = Tk()
        self.__window.title("No Thanks!")
        self.__window.iconbitmap(default="icon.ico")
        # don't allow window to be resized
        self.__window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        # don't show 'resize arrows' on sides of window
        self.__window.resizable(0, 0)

        style = Style()
        # override pressed and active appearance for all button
        style.map('TButton',
                  foreground=[('pressed', 'orange'), ('active', 'blue')],
                  background=[('pressed', '!disabled', 'orange'),
                              ('active', 'white')])
        # override background color for all other widget used
        style.configure('TFrame', background='#ABD')
        style.configure('TButton', background='#ABD')
        style.configure('TLabel', background='#ABD')
        style.configure('TRadiobutton', background='#ABD')
        style.configure('TMenubutton', background='#ABD')

        self.__picFrame = Frame(self.__window)

        self.__startupPic = PhotoImage(file="mainPic.gif")
        self.__imgLabel = Label(self.__picFrame, image=self.__startupPic,
                                borderwidth=0)

        self.__imgLabel.pack(side="top", fill="both")
        self.__picFrame.pack(side="top", fill="both")

        self.page0()

        # start listener
        self.__window.mainloop()

    def page0(self):
        self.__pageFrame = Frame(self.__window)

        self.__joinGameButton = Button(self.__pageFrame, text="Join game",
                                       command=self.goToJoinGamePage)
        self.__createGameButton = Button(self.__pageFrame, text="Create game",
                                         command=self.goToPage1)
        self.__rulesButton = Button(self.__pageFrame, text="Rules",
                                    command=self.showRules)
        self.__highscoresButton = Button(self.__pageFrame, text="High Scores",
                                         command=self.showHighScore)

        self.__pageFrame.pack(fill=BOTH, expand=Y)
        self.__joinGameButton.grid(column=0, row=0, sticky=N+S+E+W)
        self.__createGameButton.grid(column=1, row=0, sticky=N+S+E+W)
        self.__highscoresButton.grid(column=2, row=0, sticky=N+S+E+W)
        self.__rulesButton.grid(column=3, row=0, sticky=N+S+E+W)

    # unpack previous page and invoke page 0
    def goToPage0(self):
        self.__pageFrame.pack_forget()
        del self.__pageFrame
        self.page0()

    def showRules(self):
        messagebox.showinfo('RULES', RULES)

    def goToJoinGamePage(self):
        messagebox.showinfo('SOON', 'This feature is coming soon')

    # unpack previous page and invoke page 1
    def goToPage1(self):
        self.__pageFrame.pack_forget()
        del self.__pageFrame
        # don't allow window to be resized
        self.__window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        # don't show 'resize arrows' on sides of window
        self.__window.resizable(0, 0)

        self.__picFrame.pack(side="top", fill="both")
        self.page1()

    def page1(self):
        self.__pageFrame = Frame(self.__window)

        self.__numPlayerLabel = Label(self.__pageFrame,
                                      text=" Select number of players:")

        self.__numPlayersVar = IntVar(value=DEFAULT_PLAYERS)

        # display selection when menu is not active
        self.__menuBtn = Menubutton(self.__pageFrame,
                                    textvariable=self.__numPlayersVar)

        # create menu widget, disallow it to be removed from it's position
        self.__menu = Menu(self.__menuBtn, tearoff=0)

        # populate drop down menu with number choices, don't allow check mark
        #  to appear next to selected entry
        for num in range(MIN_PLAYERS, MAX_PLAYERS + 1):
            self.__menu.add_radiobutton(label=str(num),
                                        variable=self.__numPlayersVar,
                                        value=num, indicatoron=0)

        self.__menuBtn.config(menu=self.__menu)

        self.__nextButton = Button(self.__pageFrame, text="Next",
                                   command=self.goToPage2)
        self.__backButton = Button(self.__pageFrame,
                                   text="Back", command=self.goToPage0)

        self.__pageFrame.rowconfigure(0, weight=0)
        self.__pageFrame.rowconfigure(1, weight=1)
        self.__pageFrame.rowconfigure(2, weight=0)
        self.__pageFrame.columnconfigure(0, weight=0)
        self.__pageFrame.columnconfigure(1, weight=1)
        self.__pageFrame.columnconfigure(2, weight=0)

        self.__backButton.grid(row=1, column=2, sticky=N+S+E+W)
        self.__numPlayerLabel.grid(row=0, column=0, sticky=N+W)
        self.__menuBtn.grid(row=0, column=1, sticky=N+S+E+W)
        self.__nextButton.grid(row=0, column=2, sticky=N+S+E+W)
        self.__pageFrame.grid(sticky=N+S+E+W)
        self.__pageFrame.pack(fill=BOTH, expand=Y)

        self.__menuBtn.focus()

    # unpack previous page and invoke page 2
    def goToPage2(self):
        self.__pageFrame.pack_forget()
        del self.__pageFrame
        self.page2()

    def page2(self):
        self.__pageFrame = Frame(self.__window)
        self.__entryFrame = Frame(self.__pageFrame)
        self.__playerNameVars = []  # put here or with initialization!!

        self.__pageFrame.columnconfigure(0, weight=1)
        self.__pageFrame.columnconfigure(1, weight=0, minsize=150)
        self.__pageFrame.columnconfigure(2, weight=0)

        rowNum = 0
        for player in range(self.__numPlayersVar.get()):
            self.__pageFrame.rowconfigure(rowNum, weight=1)
            self.__playerNameVars.append(StringVar())
            label = Label(self.__pageFrame, text="Enter player %i" %
                          (player + 1))
            entry = Entry(self.__pageFrame,
                          textvariable=self.__playerNameVars[player],
                          width=int(WINDOW_WIDTH/ENTRY_DIVIDER))
            label.grid(row=rowNum, column=0, sticky=W)
            entry.grid(row=rowNum, column=1, sticky=N+S+E+W)

            entry.bind("<Return>", self.goToPage3)
            rowNum += 1

        self.__startButton = Button(self.__pageFrame, text="Start Game",
                                    command=self.goToPage3)
        self.__backButton = Button(self.__pageFrame, text="Back",
                                   command=self.goToPage1)
        self.__startButton.grid(row=0, column=2, rowspan=2, sticky=N+S+E+W)
        self.__backButton.grid(row=2, column=2, sticky=N+S+E+W)

        self.__pageFrame.pack(fill=BOTH, expand=Y)

    # unpack previous page and invoke page 3
    def goToPage3(self, event=None):
        boolNameList = []
        for name in self.__playerNameVars:
            boolNameList.append(bool(name.get()))  # need to check for space
        # check that all entry boxes have a valid string
        if self.validateNames():
            self.__pageFrame.pack_forget()
            del self.__pageFrame
            self.__picFrame.pack_forget()

            self.__window.minsize(width=GAME_WIDTH, height=GAME_HEIGHT)
            self.__window.resizable(0, 0)
            # invoke page 3
            self.page3()

    # validate the entered names of the players
    #   check that names are of MAX_NAME_LENGTH, are not empty, do not start
    #   with a space, and are unique for each player. Show errors based on
    #   each case
    def validateNames(self):
        valid = False
        boolNameList = [bool(name.get()) for name in self.__playerNameVars]
        self.__playerNameList = [name.get() for name in self.__playerNameVars]
        if not (False in boolNameList):
            if not (True in [name[0] == SPACE
                    for name in self.__playerNameList]):
                if len((Counter(self.__playerNameList).keys())) ==\
                        self.__numPlayersVar.get():
                    if not (False in [len(name) < MAX_NAME_LENGTH
                            for name in self.__playerNameList]):
                        valid = True
                    else:
                        messagebox.showerror('ERROR',
                                             "Players' names cannot exceed "
                                             "length %i" % MAX_NAME_LENGTH)
                else:
                    messagebox.showerror('ERROR',
                                         'Players must have unique names.')
            else:
                messagebox.showerror('ERROR', 'Player name cannot begin '
                                     'with a space.')
        else:
            messagebox.showerror('ERROR', 'Must enter names for all players!')
        return valid

    def page3(self):
        # used to stop players fro posting scores multiple times
        self.dialogShown = False
        self.__playerWidgets = {}

        Style().configure('M.TFrame', bg='red')
        self.__pageFrame = Frame(self.__window, style='M.TFrame')

        # string var for name of player in turn
        self.__playerTurnVar = StringVar()
        self.__deckChipCountVar = StringVar()

        # frame to specify turn of player
        self.__turnFrame = Frame(self.__pageFrame)

        for name in self.__playerNameList:
            # create variable for use before adding it to the dictionary
            tempFrame = Frame(self.__turnFrame)
            self.__playerWidgets[name] = [
                Radiobutton(tempFrame,
                            text=name + " has",
                            value=name,
                            variable=self.__playerTurnVar,
                            state=DISABLED),
                StringVar(value="no cards"),
                Label(tempFrame, state=DISABLED),
                StringVar(value="11 chips"),
                Label(tempFrame, state=DISABLED),
                tempFrame]
            self.__playerWidgets[name][CARDS_LBL].config(
                textvariable=self.__playerWidgets[name][CARDS_VAR])
            self.__playerWidgets[name][CHIPS_LBL].config(
                textvariable=self.__playerWidgets[name][CHIPS_VAR])

        self.__game = Game(self.__playerNameList)

        self.__playerTurnVar.set(self.__game.getCurrentPlayerName())

        self.__playerTurnLabel = Label(self.__turnFrame,
                                       text="Player Order: ",
                                       state=DISABLED)

        self.__takeCardButton = Button(self.__pageFrame, text="Take Card",
                                       command=self.currentPlayerTakeCard)

        self.__addChipButton = Button(self.__pageFrame, text="Add Chip",
                                      command=self.currentPlayerAddChip)

        self.canvas = Canvas(self.__pageFrame, width=96, height=144, bg='grey')
        self.__imgList = {}
        for card in self.__game.getDeck()[::-1]:
            value = card.getValue()
            self.__imgList[value] = PhotoImage(file=card.getPicPath())
            self.canvas.create_image(3, 3, image=self.__imgList[value],
                                     anchor=N+W, tag='img%i' % value)

        self.__deckChipCounter = Label(self.__pageFrame)
        self.__deckChipCountVar.set("Cards remaining: " +
                                    (str(
                                        self.__game.getCardsRemainingInDeck()))
                                    + '\nChips on card: ' +
                                    (str(
                                        self.__game.getCurrentCard().getChips()
                                        )))

        self.__deckChipCounter.configure(textvariable=self.__deckChipCountVar)

        # revers the name list so the order is displayed correctly
        self.__playerOrder = self.__game.getPlayerNames()
        self.__playerOrder.reverse()

        # pack everything
        self.__playerTurnLabel.grid(sticky=W)
        for player in self.__playerOrder:
            self.__playerWidgets[player][RADIO].pack(side=LEFT)
            self.__playerWidgets[player][CARDS_LBL].pack(side=LEFT)
            self.__playerWidgets[player][CHIPS_LBL].pack(side=LEFT)
            self.__playerWidgets[player][FRAME].grid(sticky=N+S+E+W)

        # conficuration for resizing
        self.__pageFrame.rowconfigure(0, weight=1)
        self.__pageFrame.rowconfigure(1, weight=0)
        self.__pageFrame.rowconfigure(2, weight=0)
        self.__pageFrame.rowconfigure(3, weight=0)
        self.__pageFrame.columnconfigure(0, weight=1)
        self.__pageFrame.columnconfigure(1, weight=0)

        self.__turnFrame.grid(sticky=N+S+E+W)
        self.__deckChipCounter.grid(row=1, column=1, sticky=E)
        self.__takeCardButton.grid(row=2, columnspan=2, sticky=N+S+E+W)
        self.__addChipButton.grid(row=3, columnspan=2, sticky=N+S+E+W)
 #      self.__cardLabel.grid(row=0, column=1, sticky=E)
        self.canvas.grid(row=0, column=1, sticky=E)
        self.__pageFrame.pack(fill=BOTH, expand=Y)

        self.__takeCardButton.focus()

    def nextPlayerTurn(self):
        cardsInDeck = self.__game.getCardsRemainingInDeck()
        if cardsInDeck == -1:
            cardsInDeck = 0

        self.__deckChipCountVar.set("Cards remaining: " +
                                    str(cardsInDeck) +
                                    '\nChips on card: ' +
                                    str(
                                        self.__game.getCurrentCard().getChips()
                                        ))

        self.__playerWidgets[self.__game.getCurrentPlayerName()][
            CHIPS_VAR].set(self.__game.getCurrentPlayerChipsStr())

        self.__playerWidgets[self.__game.getCurrentPlayerName()][
            CARDS_VAR].set(self.__game.getCurrentPlayerCardsStr())

        if self.__game.cardsLeftInDeck() or self.__game.lastCardInDeck():
            self.__game.nextPlayer()
            self.__playerTurnVar.set(self.__game.getCurrentPlayerName())
        else:
            self.endGameDialog()

    # event handler for Take Card button
    #  animate card taken, take the card in the game object,
    #  and start next player turn
    # invoke animateCard
    # invoke Game.currentPlayerTakeCurrentCard()
    # invoke nextPlayerTurn()
    def currentPlayerTakeCard(self):
        self.animateCard()
        self.__game.currentPlayerTakeCurrentCard()

        # print(self.__game.getCurrentCardPath()) #debug
        # print(self.__game.getCurrentCard().getValue()) #debug
        # print(self.__imgList[self.__game.getCurrentCard().getValue()]) #debug
        self.nextPlayerTurn()

    # event handler for Add Chip button
    #  check if player has chips, allow addition of chip to card or
    #  show warning, and focus on Take Card button
    # invoke Game.currentPlayerAddChipToCurrentCard()
    # invoke nextPlayerTurn()
    # invoke Widget.focus()
    def currentPlayerAddChip(self):
        if self.__game.currentPlayerHasChips():
            self.__game.currentPlayerAddChipToCurrentCard()
            self.nextPlayerTurn()
        else:
            messagebox.showwarning("No Chips",
                                   "Current player has no more chips and must "
                                   "take the card.")
            self.__takeCardButton.focus()

    # event handler for showing end of game dialog
    #  show dialog box with winner, all player scores, and 5 (or 4) buttons
    #  with options to end game, start new, upload scores, or got to main menu
    def endGameDialog(self):
        text = "Winner is %s.\nScores:\n%s\nPlay Again?" %\
                    (self.__game.getWinnerName(),
                    "\n".join(self.__game.getPlayerScoreList()))
        choice = Dialog(self.__window, {'title': "End of Game",
                                        'text': text,
                                        'bitmap': messagebox.INFO,
                                        'default': SAME_PLAYERS,
                                        'strings': ("Yes, same players",
                                                    "Yes, new players",
                                                    "No, quit",
                                                    "Main menu",
                                                    "Upload Scores" if not self.dialogShown else None)})
        # go to pages based on user choice
        if choice.num == SAME_PLAYERS:
            self.goToPage3()
        elif choice.num == NEW_PLAYERS:
            self.goToPage1()
        elif choice.num == QUIT:
            self.__window.destroy()
        elif choice.num == MAIN_MENU:
            self.__pageFrame.pack_forget()
            del self.__pageFrame
            # don't allow window to be resized
            self.__window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
            # don't show 'resize arrows' on sides of window
            self.__window.resizable(0, 0)

            self.__picFrame.pack(side="top", fill="both")
            self.page1()
            self.goToPage0()
        elif choice.num == UPLOAD:
            self.addToHighScores()
            self.dialogShown = True
            self.endGameDialog()

    # method for animating card
    #  disables button at start to prevent user form clicking it multiple
    #  times while animation still happening (bug)
    def animateCard(self):
        self.__takeCardButton.config(state='disabled')
        # initialize loop count
        self.lopps = 0
#        print(self.__imgList[self.__game.getCurrentCard().getValue()]) #debug
        while self.lopps < 51:
            self.canvas.move("img%i" %
                             self.__game.getCurrentCard().getValue(), 2, 0)
            self.lopps += 1
            self.canvas.update()
        self.__takeCardButton.config(state='enabled')

    # method for adding player scores to high score database
    def addToHighScores(self):
        # base string for request url
        reqUrl = URL + '/update/'
        # initialize loop counter
        numLoops = 0
        scoreList = self.__game.getPlayerScoreList()
        for pair in scoreList:
            nameScore = pair.split(': ')
            player = nameScore[0]
            score = int(nameScore[1])
            # data to POST
            data = {'player_name': player,
                    'player_score': score}
            # convert dictionary to url format
            dataParsed = urllib.parse.urlencode(data)
            # covert to bytes
            dataEncoded = dataParsed.encode('utf-8')
            try:
                req = urllib.request.urlopen(reqUrl,
                                             data=dataEncoded)
                resp = req.read()
                # make sure the request was succsesfully completed, and only show it once
                if resp.decode('utf-8') == 'Done' and numLoops == (len(scoreList) - 1):
                    messagebox.showinfo(title='SUCCESS', message='High Scores posted!!')
                elif resp.decode('utf-8') != 'Done':
                    messagebox.showwarning(title='High Scores',
                                           message="%s's data wasn't posted." %
                                           (player))
            except Exception as err:
                # print(err)
                if numLoops == (len(scoreList) - 1):
                    messagebox.showwarning(title='High Scores',
                                           message="Error! Data wasn't posted.")
            numLoops += 1

    # method for showing player higscored in and info dialong
    def showHighScore(self):
        # base string for request url
        reqUrl = URL + '/show/'
        try:
            req = urllib.request.urlopen(reqUrl)
            resp = req.read()
            messagebox.showinfo(title="High Scores", message=resp)
        except Exception as err:
            # print(err)
            messagebox.showwarning(title='High Scores',
                                   message="Can't reach server")


MainWindow()
