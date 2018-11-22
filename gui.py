import tkinter

top = tkinter.Tk()
top.title("ChatterBox")

messages_frame = tkinter.Frame(top)
my_msg= tkinter.StringVar()

my_msg.set("Type your message ..")
scrollbar = tkinter.Scrollbar(messages_frame)


msg_queue = tkinter.Listbox(messages_frame,height=30,width=50,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_queue.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_queue.pack()
messages_frame.pack()


entry_field = tkinter.Entry(top,textvariable=my_msg)
entry_field.bind()
entry_field.pack()


send_button = tkinter.Button(top,text="Send" , command=send_message) #add command to this
send_button.pack()

#top.protocol("WM_DELETE_WINDOW",on_closing)


tkinter.mainloop()
