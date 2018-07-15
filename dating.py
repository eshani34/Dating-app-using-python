from tkinter import *
import mysql.connector

class Login:

    def __init__(self):
        self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='tinder3')
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title('Login')
        self.root.minsize(250,350)
        self.root.maxsize(250,350)
        self.email_label=Label(self.root,text='Enter email')
        self.email_label.pack()
        self.email_input=Entry(self.root)
        self.email_input.pack()
        self.password_label = Label(self.root, text='Enter password')
        self.password_label.pack()
        self.password_input = Entry(self.root)
        self.password_input.pack()

        self.button=Button(self.root,text='login',command=lambda :self.perform())
        self.button.pack()
        self.button_2= Button(self.root, text='Register', command=lambda : self.register())
        self.button_2.pack()
        self.result=Label(self.root,text='',fg='red')
        self.result.pack()

        self.root.mainloop()
    def perform(self):
        email=(self.email_input.get())
        password=(self.password_input.get())
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE'{}'""".format(email,password))
        user_list=self.mycursor.fetchall()
        counter=0
        counter = 0
        for i in user_list:
            counter = counter + 1
            current_user = i

        if counter>0:
            self.result.configure(text='welcome')
            self.current_user_id=current_user[0]
            self.button3=Button(self.root,text='menu',command=lambda :self.user_menu())
            self.button3.pack()
        else:
            self.result.configure(text='Incorrect creds')
            self.result2 = Label(self.root, text='NOT A MEMBER', fg='red')
            self.result2.pack()
    def register(self):
        self.root1 = Tk()
        self.root1.title('Register')
        self.root1.minsize(250,300)
        self.name_label_1 = Label(self.root1, text='Enter name')
        self.name_label_1.pack()
        self.name_input_1 = Entry(self.root1)
        self.name_input_1.pack()
        self.email_label_1 = Label(self.root1, text='Enter email')
        self.email_label_1.pack()
        self.email_input_1 = Entry(self.root1)
        self.email_input_1.pack()
        self.password_label_1 = Label(self.root1, text='Enter password')
        self.password_label_1.pack()
        self.password_input_1 = Entry(self.root1)
        self.password_input_1.pack()
        self.gender_label_1 = Label(self.root1, text='Enter gender')
        self.gender_label_1.pack()
        self.gender_input_1 = Entry(self.root1)
        self.gender_input_1.pack()
        self.age_label_1 = Label(self.root1, text='Enter age')
        self.age_label_1.pack()
        self.age_input_1 = Entry(self.root1)
        self.age_input_1.pack()
        self.city_label_1 = Label(self.root1, text='Enter city')
        self.city_label_1.pack()
        self.city_input_1 = Entry(self.root1)
        self.city_input_1.pack()
        self.button_3 = Button(self.root1, text='Insert', command=lambda: self.insert())
        self.button_3.pack()



        self.root1.mainloop()
    def insert(self):

        name = self.name_input_1.get()
        email = self.email_input_1.get()
        password = self.password_input_1.get()
        gender = self.gender_input_1.get()
        age = self.age_input_1.get()
        city = self.city_input_1.get()
        self.announce=Label(self.root1,text='',bg='red')
        self.announce.pack()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
        list_find=self.mycursor.fetchall()
        if len(list_find)==0:
            self.mycursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(
                name, email, password, gender, age, city))
            self.conn.commit()
            self.announce.configure(text='REGISTERED SUCCESSFULLY',fg='red')
        else:
            info=Label(self.root1,text='THIS EMAIL ALREADY EXISTS',bg='red')
            info.pack()

        self.__init__()
    def user_menu(self):
        self.root2=Tk()
        self.root2.minsize(250,300)
        self.button_view=Button(self.root2,text='view users',command=lambda :self.view_users())
        self.button_view.pack()

        self.button_proposals = Button(self.root2, text='view proposals', command=lambda: self.view_proposals())
        self.button_proposals.pack()

        self.button_requests = Button(self.root2, text='view requests', command=lambda: self.view_requests())
        self.button_requests.pack()

        self.button_matches = Button(self.root2, text='view matches', command=lambda: self.view_matches())
        self.button_matches.pack()

        self.button_logout = Button(self.root2, text='Logout', command=lambda: self.logout())
        self.button_logout.pack()
        self.root2.mainloop()

    def view_users(self):
        self.root3=Tk()

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))
        all_users_list = self.mycursor.fetchall()
        for i in all_users_list:
            label1=Label(self.root3,text=str(i[0]))
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[1])
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[4])
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[5])
            label1.pack(side=LEFT)
            #label1 = Label(self.root3, text=i[6])
            #label1.pack(side=LEFT)
            label1 = Label(self.root3, text="\n")
            label1.pack()

        #self.juliet_id_name = Label(self.root3,text='Enter the id of the user whom you want to propose')
        #self.juliet_id_name.pack(side= TOP)
       # self.juliet_id_input=Entry(self.root3)
       # self.juliet_id_input.pack(side= TOP)
       # juliet_id=self.juliet_id_input.get()
        self.submit_proposal=Button(self.root3,text='next',command=lambda :self.next())
        self.submit_proposal.pack()

        self.root3.mainloop()
    def propose(self,romeo_id):
        content = self.juliet.get()

        self.label3_post=Label(self.root4,text='',bg='red')
        self.label3_post.pack()
        self.mycursor.execute("""SELECT * FROM `proposals` WHERE `juliet_id` LIKE '{}'""".format(content))
        list_of_no_repeat=self.mycursor.fetchall()
        if len(list_of_no_repeat)==0:
            self.mycursor.execute(
                """INSERT INTO `proposals` (`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL,'{}','{}')""".format(
                    romeo_id, content))
            self.conn.commit()
            self.label3_post.configure(text='PROPOSAL SEND SUCCESSFULLY.FINGERS CROSSED')
        else:
            self.label3_post.configure(text='ALREADY PROPOSED')


    def next(self):
        self.root4=Tk()
        self.juliet_id_name = Label(self.root4, text='ENTER THE ID OF THE USER WHOM YOU WANT TO PROPOSE')
        self.juliet_id_name.pack()
        self.juliet=Entry(self.root4)
        self.juliet.pack()


        self.submit_proposal_1 = Button(self.root4, text="submit", command=lambda: self.propose(self.current_user_id))
        self.submit_proposal_1.pack()
        back = Button(self.root4, text='back', command=lambda: self.back())
        back.pack()
        self.root4.mainloop()
    def view_proposals(self):
        self.root3=Tk()
        self.proposed=Label(self.root3,text='THE USERS WHOM YOU PROPOSED....',bg='red')
        self.proposed.pack()
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE P.`romeo_id` LIKE '{}'""".format(self.current_user_id))
        proposed_user_list=self.mycursor.fetchall()
        for i in proposed_user_list:
            label1 = Label(self.root3, text=(i[4]))
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[5])
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[7])
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[8])
            label1.pack(side=LEFT)
            # label1 = Label(self.root3, text=i[6])
            # label1.pack(side=LEFT)
            label1 = Label(self.root3, text="\n")
            label1.pack()
        back = Button(self.root3, text='back', command=lambda: self.back())
        back.pack()
        self.root3.mainloop()

    def view_requests(self):
        self.root3=Tk()
        self.request=Label(self.root3,text='THE USERS WHO PROPOSED YOU!!OMG!!!',bg='red')
        self.request.pack()
        self.mycursor.execute(
            """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE P.`juliet_id` LIKE '{}'""".format(
                self.current_user_id))
        requested_user_list = self.mycursor.fetchall()
        for i in requested_user_list:
            label1 = Label(self.root3, text=(i[4]))
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[5])
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[7])
            label1.pack(side=LEFT)
            label1 = Label(self.root3, text=i[8])
            label1.pack(side=LEFT)
            # label1 = Label(self.root3, text=i[6])
            # label1.pack(side=LEFT)
            label1 = Label(self.root3, text="\n")
            label1.pack()
        back = Button(self.root3, text='back', command=lambda: self.back())
        back.pack()
        self.root3.mainloop()
    def view_matches(self):
        self.root3=Tk()
        self.match=Label(self.root3,text='YOUR MATCHES ::')
        self.match.pack()
        self.mycursor.execute("""SELECT `name`,`gender`,`city`,`age` FROM `users` WHERE `user_id` IN (SELECT `juliet_id` FROM `proposals` WHERE `juliet_id` IN (SELECT `romeo_id` FROM `proposals` WHERE `juliet_id` LIKE '{}') AND `romeo_id` LIKE '{}')""".format(self.current_user_id,self.current_user_id))
        matches_found=self.mycursor.fetchall()
        for i in matches_found:
            label1 = Label(self.root3, text=i)
            label1.pack(side=LEFT)
        back=Button(self.root3,text='back',command=lambda:self.back())
        back.pack()
        self.root3.mainloop()
    def back(self):
        self.user_menu()


    def logout(self):
        self.current_user_id= 'NULL'
        self.__init__()

user=Login()

