from tkinter import Tk, StringVar, OptionMenu, Button, Label
run = True


class ResolutionPicker:
	def __init__(self):
		self.run = True

	def window(self, min_res=0, max_res=0):
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
							"1024 × 768",
							"1280 × 720",
							"1366 × 768",
							"1600 × 900",
							"1920 × 1080"]

		value_inside = StringVar(root)
		
		value_inside.set("Select an Option")

		label = Label(root, text="Select Screen Resolution")
		label.pack()
		
		question_menu = OptionMenu(root, value_inside, *resolutions_list)
		question_menu.pack()

		submit_button = Button(root, text='Submit', command=self.exit)
		submit_button.pack()

		print(self.run)

		if run:
			root.mainloop()

		else:
			return value_inside.get()


	// TODO returnúť value_inside a destroynúť res window 

	def exit(self):
		self.run = False


if __name__ == '__main__':
	win = ResolutionPicker().window()
	print(win)