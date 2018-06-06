#!/usr/bin/env python

import plotly as py
import plotly.graph_objs as go

Xvals=[]; Yvals=[]
f = open('./Task_2.txt', 'r')

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
                color='rgb(75,203,242)',
                )
    )]

layout = go.Layout(
        title='Wordcount of swedish pronouns',
        font=dict(color = "black", size = 16),
        )

fig= go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='output_bar_task_2')
