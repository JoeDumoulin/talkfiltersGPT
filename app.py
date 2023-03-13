# -*- coding: utf-8 -*-
# app.py -  a simple webpage for valspeakgtp

import os

from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import openai
import json

import lex
import valspeaklex
import piratelex

valspeak = valspeaklex.lex_patterns
piratespeak = piratelex.lex_patterns

openai.api_key = os.getenv("OPENAI_API_KEY")

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.I("Ask a question"),
        html.Br(),
        dcc.Input(id="query", type="text", placeholder="", style={'marginRight':'10px'}),
        html.Br(),
        html.Button("ok", id="ok", n_clicks=0),
        html.Div(id="answer"),
        html.Pre(id="jsonResponse")
    ]
)



@app.callback(
    Output("answer", "children"),
    Output("jsonResponse", "children"),
    Input("ok", "n_clicks"),
    State(component_id="query", component_property="value"),
)

def update_output(n_clicks, value):
    if value:
      instr = "Q: " + value + "\nA: "
    
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=instr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
      )

      return (u' {}'.format(lex.checkReplace(piratespeak, response["choices"][0]["text"])),
                json.dumps(response, indent=2))


if __name__ == "__main__":
    app.run_server(debug=True)

