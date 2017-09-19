#Created by: Malcolm McCarthy
# Created on: Sept 2017
# Created for: ICS3U
# This program calculates area and perimeter of a 3x5 rectangle

import ui

def answer_touch_up_inside(sender):
	#displays answer for perimeter and area
	view['area_answer_label'].text = 'Area = ' + str(3*5) + ' cm^2'
	view['perimeter_answer_label'].text = 'Perimeter = ' + str(5+5+3+3) + ' cm'
	
view = ui.load_view()
view.present('sheet')
