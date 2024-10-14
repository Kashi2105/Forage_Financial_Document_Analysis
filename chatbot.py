#Import all the necessary packages

import pandas as pd
import numpy as np
df= pd.read_excel("Manually_Extracted_data.xlsx")

#This is going to be a hard coded chatbot with a fewer number of responses
#we are giving some basic queries such as finding totals and etcs and their responses as nested if else statements

def response(query):
    if query=="What is the percent change in the Revenue of Microsoft for the year 2022":
        return f"The percent change in the Revenue of Microsoft for the year 2022 is {((df['Total Revenue ($ millions)'][1]-df['Total Revenue ($ millions)'][2])/df['Total Revenue ($ millions)'][2])*100: .2f} %"
    
    elif query=="What is the percent change in the Revenue of Microsoft for the year 2023":
        return f"The percent change in the Revenue of Microsoft for the year 2023 is {((df['Total Revenue ($ millions)'][0]-df['Total Revenue ($ millions)'][1])/df['Total Revenue ($ millions)'][1])*100: .2f} %"
    
    elif query=="What is the percent change in the Revenue of Tesla for the year 2022":
        return f"The percent change in the Revenue of Tesla for the year 2022 is {((df['Total Revenue ($ millions)'][4]-df['Total Revenue ($ millions)'][5])/df['Total Revenue ($ millions)'][5])*100: .2f} %"
    
    elif query=="What is the percent change in the Revenue of Tesla for the year 2023":
        return f"The percent change in the Revenue of Tesla for the year 2023 is {((df['Total Revenue ($ millions)'][3]-df['Total Revenue ($ millions)'][4])/df['Total Revenue ($ millions)'][4])*100: .2f} %"
    
    elif query=="What is the percent change in the Revenue of Apple for the year 2022":
        return f"The percent change in the Revenue of Apple for the year 2022 is {((df['Total Revenue ($ millions)'][7]-df['Total Revenue ($ millions)'][8])/df['Total Revenue ($ millions)'][8])*100: .2f} %"
    
    elif query=="What is the percent change in the Revenue of Apple for the year 2023":
        return f"The percent change in the Revenue of Apple for the year 2023 is {((df['Total Revenue ($ millions)'][6]-df['Total Revenue ($ millions)'][7])/df['Total Revenue ($ millions)'][7])*100: .2f} %"
    
    elif query=="What is the percent change in the Net Income of Microsoft for the year 2022":
        return f"The percent change in the Net Income of Microsoft for the year 2022 is {((df['Net Income'][1]-df['Net Income'][2])/df['Net Income'][2])*100: .2f} %"
    
    elif query=="What is the percent change in the Net Income of Microsoft for the year 2023":
        return f"The percent change in the Net Income of Microsoft for the year 2023 is {((df['Net Income'][0]-df['Net Income'][1])/df['Net Income'][1])*100: .2f} %"
    
    elif query=="What is the percent change in the Net Income of Tesla for the year 2022":
        return f"The percent change in the Net Income of Tesla for the year 2022 is {((df['Net Income'][4]-df['Net Income'][5])/df['Net Income'][5])*100: .2f} %"
    
    elif query=="What is the percent change in the Net Income of Tesla for the year 2023":
        return f"The percent change in the Net Income of Tesla for the year 2023 is {((df['Net Income'][3]-df['Net Income'][4])/df['Net Income'][4])*100: .2f} %"
    
    elif query=="What is the percent change in the Net Income of Apple for the year 2022":
        return f"The percent change in the Net Income of Apple for the year 2022 is {((df['Net Income'][7]-df['Net Income'][8])/df['Net Income'][8])*100: .2f} %"
    
    elif query=="What is the percent change in the Net Income of Apple for the year 2023":
        return f"The percent change in the Net Income of Apple for the year 2023 is {((df['Net Income'][6]-df['Net Income'][7])/df['Net Income'][7])*100: .2f} %"
    
    elif query == "What is the Net Income of Tesla for the year 2023":
        return f"The Net Income of Tesla for the year 2023 is ${df['Net Income'][3]} million."

    elif query == "What are the Total Assets of Microsoft for the year 2021":
        return f"The Total Assets of Microsoft for the year 2021 are ${df['Total Assets'][2]} million."

    elif query == "What is the Cash Flow from Operating Activities of Tesla for the year 2022":
        return f"The Cash Flow from Operating Activities of Tesla for the year 2022 is ${df['Cash Flow from Operating Activities'][4]} million."

    elif query == "What is the Total Liability of Microsoft for the year 2023":
        return f"The Total Liability of Microsoft for the year 2023 is ${df['Total Liabilities'][0]} million."
    else:
        return "I am sorry, I am not programmed to answer that question"
    
print(response("What is the percent change in the Revenue of Microsoft for the year 2023"))
print(response("What is the percent change in the Revenue of Tesla for the year 2023"))
print(response("What is the percent change in the Revenue of Apple for the year 2023"))
print(response("What is the percent change in the Net Income of Microsoft for the year 2023"))
print(response("What is the percent change in the Net Income of Tesla for the year 2023"))
print(response("What is the percent change in the Net Income of Apple for the year 2023"))