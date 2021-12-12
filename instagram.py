from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from bs4 import BeautifulSoup as bs
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import time
from selenium.webdriver.common.action_chains import ActionChains

# IGBot commands using Selenium
class IGBot:

    username = 'username'
    password = 'password'

    numOfComments = 13
    comments = [
        'Awesome work',
        'Great job',
        'Love it',
        'Really good work',
        'Love this piece',
        'Excellent work',
        'Great work',
        'Nice',
        'Well done',
        'Love the colors',
        'Looks amazing',
        'Outstanding work',
        'Wow'
    ]

    numOfEmojis = 9
    emojis = [
        '😍',
        '😮',
        '👍',
        '👌',
        '👏',
        '🔥',
        '',
        '',
        ''
    ]

    numOfPunc = 3
    punc = [
        '!',
        '!!',
        ''
    ]

    numOfHashtags = 24
    hashtags = [
        'octanerender',
        'dailyrender',
        'cinema4d',
        'c4d',
        'nftart',
        'renderzone',
        '3d',
        '3drender',
        'maxon',
        'otoy',
        'cgsociety',
        'digitalart',
        'ultrarenders',
        'mgcollective',
        'mdcommunity',
        'rsa_graphics',
        'artfeature3d',
        'renderscapes',
        'thegraphicspr0ject',
        'fa_hypnotic',
        '3dart',
        'blenderrender',
        'blender3d',
        'blendercommunity',

    ]

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    # logs into provided profile
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login')
        time.sleep(2)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(5)

    # opens the provided profile
    def profile(self, username):
        bot = self.bot
        time.sleep(1)
        bot.get('https://instagram.com/' + username)

    # searches for the provided hashtag
    def findHashtag(self, hashtag = hashtags[randint(0,6)]):
        bot = self.bot
        time.sleep(1)
        bot.get('https://www.instagram.com/explore/tags/' + hashtag)

    # clicks on the first picture in the photo
    def firstPhoto(self):
        bot = self.bot
        time.sleep(1)
        bot.find_element_by_class_name('v1Nh3').click()

    # moves to the next photo
    def nextPicture(self):
        bot = self.bot
        time.sleep(1)
        #arrow = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
        #arrow.click()
        bot.find_element_by_css_selector('body').send_keys(Keys.RIGHT)

    # likes the photo
    def like(self):
        bot = self.bot
        time.sleep(1)
        likeButton = bot.find_element_by_class_name('fr66n')
        heart = bs(likeButton.get_attribute('innerHTML'),'html.parser')
        if(heart.find('svg')['aria-label'] == 'Like'):
            likeButton.click()

    # comments on photo
    def comment(self):
        bot = self.bot
        time.sleep(1)
        bot.find_element_by_class_name('RxpZH').click()
        time.sleep(1)
        bot.find_element_by_class_name('Ypffh').send_keys(myBot.curComments() + Keys.RETURN)
        #bot.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(myBot.curComments() + Keys.RETURN)

    # follows profile of the photo
    def follow(self, min, max):
        bot = self.bot
        time.sleep(1)
        profileButton = bot.find_element_by_class_name('RqtMr')
        #profileButton.click()
        ActionChains(bot).key_down(Keys.CONTROL).click(profileButton).perform()
        time.sleep(1)
        bot.switch_to.window(bot.window_handles[1])
        time.sleep(3)
        
        element = bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span')
        followers = element.get_attribute("title")
        followers = int(followers.replace(",", ""))
        print(followers)
        time.sleep(1)
        if (followers >= min) & (followers <= max):
            print('Within Follower Threshold')
            try:
                followButton = bot.find_element_by_xpath("//*[text()='Follow']")
                followButton.click()
                print('Now Following')
            except:
                print('Already Following')
        else:
            print('Outside Follower Threshold')

        time.sleep(1)
        bot.close()
        bot.switch_to.window(bot.window_handles[0])
        bot.find_element_by_xpath("//html").click()

    # likes *amt* photos
    def likeOnly(self, amt):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.like()
            self.nextPicture()

    # comments on *amt* photos
    def commOnly(self, amt):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.comment()
            self.nextPicture()

    # follows *amt* of profiles
    def followOnly(self, amt, min, max):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.follow(min, max)
            self.nextPicture()

    # likes, comms on *amt* photos
    def likeComm(self, amt):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.like()
            self.comment()
            self.nextPicture()

    # likes, follows on *amt* photos
    def likeFollow(self, amt, min, max):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.like()
            self.follow(min, max)
            self.nextPicture()

    # comms, follows on *amt* photos
    def commFollow(self, amt, min, max):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.comment()
            self.follow(min, max)
            self.nextPicture() 

    # likes, comms, follows on *amt* photos
    def likeCommFollow(self, amt, min, max):
        self.firstPhoto()

        i = 0
        for i in range (0, amt):
            self.like()
            self.comment()
            self.follow(min, max)
            self.nextPicture()

# IGBot UI using Tkinter
class IGBotUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.loginFlag = 0
        self.optionsFlag = 0
        self.amtFlag = 0
        self.hashtagFlag = 0
        self.minmaxFlag = 0
        self.resizable(width=False, height=False)
        self.title('Instagram Bot')
        self.geometry('350x450')

        # login entry
        self.loginLabelFrame = ttk.LabelFrame(self, text = 'Login *', padding = (10, 10, 10, 10))
        self.loginLabelFrame.place(x = 2, y = 2)

        self.defUsername = StringVar(self, IGBot.username)
        self.usernameField = ttk.Entry(self.loginLabelFrame, textvariable = self.defUsername)
        self.usernameField.pack(padx = 10, pady = 4)

        self.defPassword = StringVar(self, IGBot.password)
        self.passwordField = ttk.Entry(self.loginLabelFrame, show = '*', textvariable = self.defPassword)
        self.passwordField.pack(padx = 10, pady = 4)

        # run bot button
        self.startButton = ttk.Button(self.loginLabelFrame, text = "Run", command = self.perform)
        self.startButton.pack(padx = 10, pady = 4)

        # amount entry
        self.amtLabelFrame = ttk.LabelFrame(self, text = 'Number of Posts *', padding = (10, 10, 10, 10))
        self.amtLabelFrame.place(x = 177, y = 2)

        self.defAmt = IntVar(self, 10)
        self.amtField = ttk.Entry(self.amtLabelFrame, textvariable = self.defAmt)
        self.amtField.pack(padx = 10, pady = 4)

        # hashtag entry
        self.hashtagLabelFrame = ttk.LabelFrame(self, text = 'Hashtag *', padding = (10, 10, 10, 10))
        self.hashtagLabelFrame.place(x = 177, y = 90)

        self.genHashtagButton = ttk.Button(self.hashtagLabelFrame, text = "Generate Hashtag", command = lambda:self.genHashtag())
        self.genHashtagButton.pack(padx = 10, pady = 4)

        self.hashtag = StringVar(self, value = IGBot.hashtags[randint(0,IGBot.numOfHashtags - 1)])
        self.hashtagField = ttk.Entry(self.hashtagLabelFrame, textvariable = self.hashtag)
        self.hashtagField.pack(padx = 10, pady = 4)

        # comment entry
        self.commentLabelFrame = ttk.LabelFrame(self, text = 'Comments', padding = (10, 10, 10, 10))
        self.commentLabelFrame.place(x = 177, y = 220)

        self.genCommentsButton = ttk.Button(self.commentLabelFrame, text = "Generate Comments", command = lambda:self.genComments())
        self.genCommentsButton.pack(padx = 10, pady = 4)

        self.comments = [
            StringVar(self, value = (IGBot.comments[randint(0,IGBot.numOfComments - 1)]) + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            StringVar(self, value = (IGBot.comments[randint(0,IGBot.numOfComments - 1)]) + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            StringVar(self, value = (IGBot.comments[randint(0,IGBot.numOfComments - 1)]) + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            StringVar(self, value = (IGBot.comments[randint(0,IGBot.numOfComments - 1)]) + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            StringVar(self, value = (IGBot.comments[randint(0,IGBot.numOfComments - 1)]) + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
        ]

        self.commentField0 = ttk.Entry(self.commentLabelFrame, textvariable = self.comments[0])
        self.commentField0.pack(padx = 10, pady = 4)
        self.commentField1 = ttk.Entry(self.commentLabelFrame, textvariable = self.comments[1])
        self.commentField1.pack(padx = 10, pady = 4)
        self.commentField2 = ttk.Entry(self.commentLabelFrame, textvariable = self.comments[2])
        self.commentField2.pack(padx = 10, pady = 4)
        self.commentField3 = ttk.Entry(self.commentLabelFrame, textvariable = self.comments[3])
        self.commentField3.pack(padx = 10, pady = 4)
        self.commentField4 = ttk.Entry(self.commentLabelFrame, textvariable = self.comments[4])
        self.commentField4.pack(padx = 10, pady = 4)

        # min/max follower entries
        self.minmaxLabelFrame = ttk.LabelFrame(self, text = 'Min/Max Followers *', padding = (10, 10, 10, 10))
        self.minmaxLabelFrame.place(x = 2, y = 320)

        self.min = IntVar(self, value = 20)
        self.max = IntVar(self, value = 400)

        self.minFollowers = ttk.Entry(self.minmaxLabelFrame, textvariable = self.min)
        self.minFollowers.pack(padx = 10, pady = 4)
        
        self.maxFollowers = ttk.Entry(self.minmaxLabelFrame, textvariable = self.max)
        self.maxFollowers.pack(padx = 10, pady = 4)

        # comment/follow checkboxes
        self.optionsLabelFrame = ttk.LabelFrame(self, text = 'Options *', padding = (32, 10, 37, 10))
        self.optionsLabelFrame.place(x = 2, y = 160)

        self.likeVar = tk.IntVar()
        self.commVar = tk.IntVar()
        self.followVar = tk.IntVar()

        self.likeCheck = ttk.Checkbutton(self.optionsLabelFrame, text = 'Like', variable = self.likeVar, offvalue = 0, onvalue = 1)
        self.likeCheck.pack(padx = 10, pady = 4)

        self.commCheck = ttk.Checkbutton(self.optionsLabelFrame, text = 'Comment', variable = self.commVar, offvalue = 0, onvalue = 1, command = lambda:self.enableDisableComments())
        self.commCheck.pack(padx = 10, pady = 4)
        self.enableDisableComments()

        self.followCheck = ttk.Checkbutton(self.optionsLabelFrame, text = 'Follow', variable = self.followVar, offvalue = 0, onvalue = 1, command = lambda:self.enableDisableFollowers())
        self.followCheck.pack(padx = 10, pady = 4)
        self.enableDisableFollowers()

    # disables comment section if 'Comment' checkbutton not checked
    def enableDisableComments(self):
        enabled = self.commVar.get()
        if enabled == True:
            for child in self.commentLabelFrame.winfo_children():
                child.configure(state = 'enable')
        else:
            for child in self.commentLabelFrame.winfo_children():
                child.configure(state = 'disable')

    def enableDisableFollowers(self):
        enabled = self.followVar.get()
        if enabled == True:
            for child in self.minmaxLabelFrame.winfo_children():
                child.configure(state = 'enable')
        else:
            for child in self.minmaxLabelFrame.winfo_children():
                child.configure(state = 'disable')

    # generates new comments
    def genComments(self):
        self.comments = [
            (IGBot.comments[randint(0,IGBot.numOfComments - 1)] + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            (IGBot.comments[randint(0,IGBot.numOfComments - 1)] + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            (IGBot.comments[randint(0,IGBot.numOfComments - 1)] + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            (IGBot.comments[randint(0,IGBot.numOfComments - 1)] + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)]),
            (IGBot.comments[randint(0,IGBot.numOfComments - 1)] + IGBot.punc[randint(0,IGBot.numOfPunc - 1)] + IGBot.emojis[randint(0,IGBot.numOfEmojis - 1)])
        ]
        self.commentField0.delete(0, 'end')
        self.commentField0.insert(0, self.comments[0])
        self.commentField1.delete(0, 'end')
        self.commentField1.insert(0, self.comments[1]) 
        self.commentField2.delete(0, 'end')
        self.commentField2.insert(0, self.comments[2])
        self.commentField3.delete(0, 'end')
        self.commentField3.insert(0, self.comments[3])
        self.commentField4.delete(0, 'end')
        self.commentField4.insert(0, self.comments[4])

    # returns a random comment of the 5 selected
    def curComments(self):
        commentOptions = [
            self.commentField0.get(),
            self.commentField1.get(),
            self.commentField2.get(),
            self.commentField3.get(),
            self.commentField4.get()
        ]
        return commentOptions[randint(0,4)]

    # generates a new hashtag
    def genHashtag(self):
        self.hashtag = IGBot.hashtags[randint(0,IGBot.numOfHashtags - 1)]
        self.hashtagField.delete(0, 'end')
        self.hashtagField.insert(0, self.hashtag)

    # checks required entry fields
    def required(self):
        # check login entry for input
        if ((len(self.usernameField.get()) == 0) | (len(self.passwordField.get()) == 0)) & (self.loginFlag < 1):
            print('Please enter valid login credentials')
            self.errUNLabel = Label(self.loginLabelFrame, text = 'Please enter valid login credentials', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 3, fg = 'red')
            self.errUNLabel.config(font = ('Typograph', 6, 'italic'))
            self.errUNLabel.pack(padx = 0, pady = 0)
            self.loginFlag += 1
            self.errUNLabel.after(5000, self.errUNLabel.destroy)
        elif ((len(self.usernameField.get()) == 0) | (len(self.passwordField.get()) == 0)) & (self.loginFlag > 0):
            self.errUNLabel.destroy()
            print('Please enter valid login credentials')
            self.errUNLabel = Label(self.loginLabelFrame, text = 'Please enter valid login credentials', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 3, fg = 'red')
            self.errUNLabel.config(font = ('Typograph', 6, 'italic'))
            self.errUNLabel.pack(padx = 0, pady = 0)
            self.loginFlag += 1
            self.errUNLabel.after(5000, self.errUNLabel.destroy)
        else:
            self.loginFlag = 0

        # check hashtag entry for input
        if (len(self.hashtagField.get()) == 0) & (self.hashtagFlag < 1):
            print('Please enter a hashtag')
            self.errHTLabel = Label(self.hashtagLabelFrame, text = 'Please enter a hashtag', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 3, fg = 'red')
            self.errHTLabel.config(font = ('Typograph', 6, 'italic'))
            self.errHTLabel.pack(padx = 0, pady = 0)
            self.hashtagFlag += 1
            self.errHTLabel.after(5000, self.errHTLabel.destroy)
        elif (len(self.hashtagField.get()) == 0) & (self.hashtagFlag > 0):
            self.errHTLabel.destroy()
            print('Please enter a hashtag')
            self.errHTLabel = Label(self.hashtagLabelFrame, text = 'Please enter a hashtag', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 3, fg = 'red')
            self.errHTLabel.config(font = ('Typograph', 6, 'italic'))
            self.errHTLabel.pack(padx = 0, pady = 0)
            self.hashtagFlag += 1
            self.errHTLabel.after(5000, self.errHTLabel.destroy)
        else:
            self.hashtagFlag = 0

        # check options checkbuttons for at least one checkbox
        if ((self.likeVar.get() == 0) & (self.commVar.get() == 0) & (self.followVar.get() == 0)) & (self.optionsFlag < 1):
            print('Please select a command')
            self.errOpLabel = Label(self.optionsLabelFrame, text = 'Please select a command', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 3, fg = 'red')
            self.errOpLabel.config(font = ('Typograph', 6, 'italic'))
            self.errOpLabel.pack(padx = 0, pady = 0, side = BOTTOM)
            self.optionsFlag += 1
            self.errOpLabel.after(5000, self.errOpLabel.destroy)
        elif ((self.likeVar.get() == 0) & (self.commVar.get() == 0) & (self.followVar.get() == 0)) & (self.optionsFlag > 0):
            self.errOpLabel.destroy()
            print('Please select a command')
            self.errOpLabel = Label(self.optionsLabelFrame, text = 'Please select a command', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 3, fg = 'red')
            self.errOpLabel.config(font = ('Typograph', 6, 'italic'))
            self.errOpLabel.pack(padx = 0, pady = 0)
            self.optionsFlag += 1
            self.errOpLabel.after(5000, self.errOpLabel.destroy)
        else:
            self.optionsFlag = 0   

        # check amount entry for integer input
        try:
            i = int(self.amtField.get())
            self.amtFlag = 0
        except ValueError:
            if self.amtFlag < 1:
                print('Please enter an integer')
                self.errAmtLabel = Label(self.amtLabelFrame, text = 'Please enter an integer', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 0, fg = 'red')
                self.errAmtLabel.config(font = ('Typograph', 6, 'italic'))
                self.errAmtLabel.pack(padx = 0, pady = 0)
                self.amtFlag += 1
                self.errAmtLabel.after(5000, self.errAmtLabel.destroy)
            elif self.amtFlag > 0:
                self.errAmtLabel.destroy()
                print('Please enter an integer')
                self.errAmtLabel = Label(self.amtLabelFrame, text = 'Please enter an integer', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 0, fg = 'red')
                self.errAmtLabel.config(font = ('Typograph', 6, 'italic'))
                self.errAmtLabel.pack(padx = 0, pady = 0)
                self.amtFlag += 1
                self.errAmtLabel.after(5000, self.errAmtLabel.destroy)

        # check min/max entry for integer input
        try:
            i = int(self.minFollowers.get())
            j = int(self.maxFollowers.get())
            self.minmaxFlag = 0
        except ValueError:
            if (self.minmaxFlag < 1) & (self.followVar.get() == 1):
                print('Please enter integers')
                self.errMinMaxLabel = Label(self.minmaxLabelFrame, text = 'Please enter an integer', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 0, fg = 'red')
                self.errMinMaxLabel.config(font = ('Typograph', 6, 'italic'))
                self.errMinMaxLabel.pack(padx = 0, pady = 0, side = BOTTOM)
                self.minmaxFlag += 1
                self.errMinMaxLabel.after(5000, self.errMinMaxLabel.destroy)
            elif (self.minmaxFlag > 0) & (self.followVar.get() == 1):
                self.errMinMaxLabel.destroy()
                print('Please enter integers')
                self.errMinMaxLabel = Label(self.minmaxLabelFrame, text = 'Please enter an integer', relief = tk.FLAT, justify = tk.CENTER, borderwidth = 0, fg = 'red')
                self.errMinMaxLabel.config(font = ('Typograph', 6, 'italic'))
                self.errMinMaxLabel.pack(padx = 0, pady = 0, side = BOTTOM)
                self.minmaxFlag += 1
                self.errMinMaxLabel.after(5000, self.errMinMaxLabel.destroy)

        # if follow checkbutton is disabled, set minmax flag to 0 (no longer required)
        if (self.followVar.get() == 0):
            self.minmaxFlag = 0

        # return 0 if error was found, else return 1
        if (self.loginFlag > 0) | (self.amtFlag > 0) | (self.optionsFlag > 0) | (self.minmaxFlag > 0):
            return 0
        else:
            return 1    

    # dialogue box for user confirmation to run bot
    def confirm(self):
        answer = askyesno(title = 'Confirmation', message = 'Are you sure you want to run the bot?')
        if answer:
            return 1
        else:
            return 0

    # run bot
    def perform(self):
        # check required fields
        if self.required() == 0:
            return

        # confirmation dialogue box
        if self.confirm() == 0:
            return
        
        # login
        username = self.usernameField.get()
        password = self.passwordField.get()
        bot = IGBot(username, password)
        bot.login()
        bot.profile(username)

        # grab amount, grab min/max, search hashtag
        amt = int(self.amtField.get())
        min = int(self.min.get())
        max = int(self.max.get())
        if len(self.hashtagField.get()) != 0:
            hashtag = self.hashtagField.get()
            bot.findHashtag(hashtag)
        else:
            bot.findHashtag()

        # like, comm, follow combinations based on checkbuttons
        # like, comm, follow
        if ((self.likeVar.get() == 1) & (self.commVar.get() == 1) & (self.followVar.get() == 1)):
            print('likeCommFollow')
            bot.likeCommFollow(amt, min, max)
        # like, comm
        elif ((self.likeVar.get() == 1) & (self.commVar.get() == 1) & (self.followVar.get() == 0)):
            print('likeComm')
            bot.likeComm(amt)
        # like, follow
        elif ((self.likeVar.get() == 1) & (self.commVar.get() == 0) & (self.followVar.get() == 1)):
            print('likeFollow')
            bot.likeFollow(amt, min, max)
        # comm, follow
        elif ((self.likeVar.get() == 0) & (self.commVar.get() == 1) & (self.followVar.get() == 1)):
            print('commFollow')
            bot.commFollow(amt, min, max)
        # like
        elif ((self.likeVar.get() == 1) & (self.commVar.get() == 0) & (self.followVar.get() == 0)):
            print('likeOnly')
            bot.likeOnly(amt)
        # comm
        elif ((self.likeVar.get() == 0) & (self.commVar.get() == 1) & (self.followVar.get() == 0)):
            print('commOnly')
            bot.commOnly(amt)
        # follow
        elif ((self.likeVar.get() == 0) & (self.commVar.get() == 0) & (self.followVar.get() == 1)):
            print('followOnly')
            bot.followOnly(amt, min, max)

        # return to profile
        bot.profile(username)

if __name__ == '__main__':
    myBot = IGBotUI()
    mainloop()
