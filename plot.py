#!/usr/bin/env python

import plotly as py
import plotly.graph_objs as go

Xvals=[]; Yvals=[]
f = open('ENTER INPUT FILE NAME', 'r')

for line in f:
    a, b = line.split('\t', 1)
    Xvals.append(a)
    Yvals.append(int(b))

data = [go.Bar(
            x=Xvals,
            y=Yvals,
            text=Yvals,
            textposition = 'outside',
            opacity=0.8,
            marker=dict(
                color='rgb(RED_VAL,GREEN_VAL,BLUE_VAL)',
                )
    )]

layout = go.Layout(
        title='ENTER TITLE HERE',
        )

fig= go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='ENTER OUTPUT FILE NAME HERE')
