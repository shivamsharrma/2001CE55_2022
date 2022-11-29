
from datetime import datetime
start_time = datetime.now()
import streamlit as st
import pandas as pd


#Help
def proj_octant_gui():
	pass


	st.title("Gui version of tut 7")
	uploaded_file= st.file_uploader("Choose a file")
	# df=pd.read_excel(uploaded_file)
	number=st.number_input('Enter the mod values:')
	if st.button('Compute'):
		st.write("hello")
	else:
		st.write('Error')

	
###Code

# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
# 	print("Correct Version Installed")
# else:
# 	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


proj_octant_gui()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
