import plotly.graph_objects as go
import PrettyUglyPlot_BarChart
#import PrettyPlot as pp

# Citation: https://plotly.com/python/gauge-charts/

##### Pretty Plot - starts here #####
'''
This part of the program will spit out the Pretty version of the average wind speed in the respective seasons. 

It will still answer all the questions but it will show one of the potential version of how not to make a Dial Chart.

'''

#for Winter - Blue

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgWinter,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 30}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 2, 'tickcolor': "darkblue",'tickfont':{'size':50}},
        'bar': {'color': "white"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 2], 'color': '#CCE5FF'},
            {'range': [2, 4], 'color': '#96C8FA'},
            {'range': [4, 6], 'color': '#66B2FF'},
            {'range': [6, 8], 'color': '#3399FF'},
            {'range': [8, 10], 'color': '#0080FF'},
            {'range': [10, 12], 'color': '#0066CC'},
            {'range': [12, 14], 'color': '#004C99'},
            {'range': [14, 16], 'color': '#003366'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1,'value': 8
            }}))

fig.add_annotation(x=0.50,y=-0.02, text='MPH', font={'size': 25}, showarrow=False)

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()

# For Spring - Green

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgSpring,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 40}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 1, 'tickcolor': "darkblue",'tickfont':{'size':50}},
        'bar': {'color': "white"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 2], 'color': '#CCFFCC'},
            {'range': [2, 4], 'color': '#99FF99'},
            {'range': [4, 6], 'color': '#66FF66'},
            {'range': [6, 8], 'color': '#00FF00'},
            {'range': [8, 10], 'color': '#30F030'},
            {'range': [10, 12], 'color': '#00CC00'},
            {'range': [12, 14], 'color': '#009900'},
            {'range': [14, 16], 'color': '#006600'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1,'value': 8
            }}))

fig.add_annotation(x=0.50,y=-0.02, text='MPH', font={'size': 25}, showarrow=False)

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()

# for summer - Red

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgSummer,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 40}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 1, 'tickcolor': "darkblue",'tickfont':{'size':50}},
        'bar': {'color': "white"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 2], 'color': '#FFDCDC'},
            {'range': [2, 4], 'color': '#FFCCCC'},
            {'range': [4, 6], 'color': '#FF9999'},
            {'range': [6, 8], 'color': '#FF3333'},
            {'range': [8, 10], 'color': '#FF0000'},
            {'range': [10, 12], 'color': '#CC0000'},
            {'range': [12, 14], 'color': '#990000'},
            {'range': [14, 16], 'color': '#660000'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1,'value': 8
            }}))

fig.add_annotation(x=0.50,y=-0.02, text='MPH', font={'size': 25}, showarrow=False)

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()

#for Fall - Orange

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgFall,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 40}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 1, 'tickcolor': "darkblue",'tickfont':{'size':50}},
        'bar': {'color': "white"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 2], 'color': '#FFDCB9'},
            {'range': [2, 4], 'color': '#FFCC99'},
            {'range': [4, 6], 'color': '#FFB266'},
            {'range': [6, 8], 'color': '#FF9933'},
            {'range': [8, 10], 'color': '#FF8000'},
            {'range': [10, 12], 'color': '#CC6600'},
            {'range': [12, 14], 'color': '#994C00'},
            {'range': [14, 16], 'color': '#663300'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1,'value': 8
            }}))

fig.add_annotation(x=0.50,y=-0.02, text='MPH', font={'size': 25}, showarrow=False)

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()
####### Pretty Plot - Ends here #####

####### Ugly Plot - Starts here #########

'''
This part of the program will spit out the ugly version of the average wind speed in the respective seasons. 
It will still answer all the questions but it will show one of the potential version of how not to make a Dial Chart.
'''


#for Winter - Blue

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgWinter,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 14}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 2, 'tickcolor': "darkblue",'tickfont':{'size':20}},
        'bar': {'color': "#003333"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 16], 'color': '#001933'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1
            }}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()


#For Spring - Green

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgSpring,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 14}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 2, 'tickcolor': "darkblue",'tickfont':{'size':20}},
        'bar': {'color': "#003333"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 16], 'color': '#001933'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1,
            }}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()


# for summer - Red

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgSummer,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 14}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 2, 'tickcolor': "darkblue",'tickfont':{'size':20}},
        'bar': {'color': "#003333"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 16], 'color': '#001933'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1
            }}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()


#for Fall - Orange

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avgFall,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "", 'font': {'size': 14}},
    delta = {'reference': 20, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 16], 'tickwidth': 2, 'tickcolor': "darkblue",'tickfont':{'size':20}},
        'bar': {'color': "#003333"},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 16], 'color': '#001933'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 1
            }}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

fig.show()
