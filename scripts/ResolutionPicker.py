from tkinter import Tk, StringVar, OptionMenu, Button
run = True

def window(min_res, max_res):
	"""
	min_res = minimum resolution to choose from
	max_res = maximum resolution to choose from
	"""

	root = Tk()
	root.title("Select Resolution")
	#  root.geometry('700x500')
	 

	resolutions_list = ["640 × 360",
						"720 × 480",
						"800 × 600",
						"1024 × 768"
						"1280 × 720",
						"1366 ×	768",
						"1600 ×	900",
						"1920 × 1080"]

	value_inside = StringVar(root)
	
	value_inside.set("Select an Option")
	
	question_menu = OptionMenu(root, value_inside, *options_list)
	question_menu.pack()
	  
	submit_button = Button(root, text='Submit', command=exit)
	submit_button.pack()
	  
	if run:
		root.mainloop()

	else:
		return value_inside.get()


def exit():
	run = False