#!/usr/bin/env python
# coding: utf-8

# In[50]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import requests
import json
from loguru import logger
import os

#=========================================================== Configuración API ================================================================

app = dash.Dash(__name__)
server = app.server

api_url = os.getenv('API_URL')  # Intentar obtener la URL de la variable de entorno

if not api_url:  # Si la variable de entorno no está definida, usar una URL predeterminada
    api_url = "http://3.95.194.91:5000/predict"


background_color = 'rgb(77, 151, 137)'
text_color = 'white'
font_family = 'Arial, sans-serif'

cuadro_texto_estilo = {
    'font-family': font_family,
    'font-size': '12px',
    'border-radius': '10px',
    'background-color': 'white',
    'padding': '10px',
    'width': '660px',  # Ajusta el ancho del cuadro
    'height': '130px'  # Ajusta el alto del cuadro
}

cuadro_texto_estilo2 = {
    'font-family': font_family,
    'font-size': '12px',
    'border-radius': '10px',
    'background-color': 'white',
    'padding': '10px',
    'width': '660px',  # Ajusta el ancho del cuadro
    'height': '300px'  # Ajusta el alto del cuadro
}

cuadro_texto_estilo3 = {
    'font-family': font_family,
    'font-size': '25px',
    'font-weight': 'bold',  # Pone el texto en negrita
    'text-align': 'center',  # Centra el texto
    'border-radius': '10px',
    'background-color': 'white',
    'padding': '10px',
    'width': '660px',  # Ajusta el ancho del cuadro
    'height': '75px'  # Ajusta el alto del cuadro
}


#=========================================================== Lista de Recomendaciones ================================================================


lista_recomendaciones = {'Normal_Weight': """
Recomendaciones:
- Mantén tus hábitos saludables. Sigue evitando el consumo frecuente de alimentos altos en calorías (FAVC) y continúa consumiendo una cantidad adecuada de agua (CH20).
- Asegúrate de mantener una buena condición física. Continúa monitoreando tu ingesta calórica (SCC) y mantén la frecuencia de actividad física (FAF).
- Sigue haciendo elecciones inteligentes en tus hábitos alimenticios y mantén un estilo de vida activo.
""", 'Overweight_Level_I': """
Recomendaciones:
- Reduce el consumo de alimentos altos en calorías (FAVC) y trata de aumentar la frecuencia de consumo de verduras (FCVC).
- Aumenta la actividad física (FAF) y disminuye el tiempo frente a dispositivos tecnológicos (TUE).
- Establece un límite en el consumo de alcohol (CALC) y evita el consumo de alimentos entre comidas (CAEC).
- Consulta a un dietista o nutricionista para recibir orientación sobre tu plan de dieta y pérdida de peso.
""", 'Overweight_Level_II': """
Recomendaciones:
- Haz cambios significativos en tus hábitos alimenticios, incluyendo una mayor ingesta de verduras (FCVC) y la reducción de alimentos altos en calorías (FAVC).
- Comprométete con un programa de ejercicio regular (FAF) y disminuye drásticamente el tiempo frente a dispositivos tecnológicos (TUE).
- Evita el consumo de alcohol (CALC) y alimentos entre comidas (CAEC).
- Busca orientación médica y apoyo profesional para la pérdida de peso.
""", 'Obesity_Type_I': """
Recomendaciones:
- Busca un enfoque multidisciplinario con un médico, dietista y entrenador personal para abordar tu obesidad.
- Adquiere el hábito de monitorear tu ingesta calórica (SCC) y establece un plan de dieta personalizado.
- Comprométete con un programa de actividad física bajo supervisión médica y una reducción significativa del tiempo en dispositivos tecnológicos (TUE).
- Evita el consumo de alcohol (CALC) y alimentos entre comidas (CAEC).
""", 'Insufficient_Weight': """
Recomendaciones:
- Aumenta la ingesta calórica y nutricional de manera saludable. Consume más alimentos ricos en nutrientes.
- Realiza un seguimiento constante de tu consumo de calorías (SCC) para asegurarte de que estás ingiriendo suficientes calorías.
- Consulta a un médico para abordar las posibles causas de la falta de peso y busca apoyo nutricional.
""", 'Obesity_Type_II': """
Recomendaciones:
- Busca apoyo médico para abordar tu obesidad de manera seria. Consulta a un especialista en obesidad.
- Sigue un plan de tratamiento médico, incluyendo una dieta controlada y un programa de ejercicio supervisado por un profesional de la salud.
- Mantén un registro constante de tus hábitos alimenticios (FAVC, FCVC, CALC, CAEC) y actividades físicas (FAF).
- Evita el consumo de alcohol y busca apoyo emocional.
""", 'Obesity_Type_III': """
Recomendaciones:
- La obesidad de tipo III requiere una atención médica inmediata y posiblemente intervención quirúrgica.
- Consulta a un cirujano bariátrico y sigue un plan de tratamiento médico riguroso.
- Sigue una dieta muy controlada, actividad física supervisada y un monitoreo constante de tus hábitos alimenticios (FAVC, FCVC, CALC, CAEC).
- Busca apoyo emocional y psicológico para enfrentar este desafío de salud significativo.
"""}

#=================================================== Lista de opciones para los cuadros de selección =============================================================

opciones1 = [
    {'label': 'Si', 'value': 'yes'},
    {'label': 'No', 'value': 'no'}
]

opciones2 = [
    {'label': 'No bebo', 'value': 'no'},
    {'label': 'Aveces', 'value': 'Sometimes'},
    {'label': 'Frecuentemente', 'value': 'Frequently'},
    {'label': 'Todo el tiempo', 'value': 'Always'}
    
]

opciones4 = [{'label': str(i/2), 'value': str(i/2)} for i in range(2, 12)]

opciones8 = [
    {'label': 'Si', 'value': '1'},
    {'label': 'No', 'value': '0'}
]

opciones3 = [
    {'label': '1 Comida', 'value': '1'},
    {'label': '2 Comidas', 'value': '2'},
    {'label': '3 Comidas', 'value': '3'},
    {'label': '4 Comidas', 'value': '4'}
]


opciones5 = [{'label': str(i/10), 'value': str(i/10)} for i in range(0, 11)]


opciones6 = [
    {'label': '0 - 2 Horas', 'value': '1'},
    {'label': '3 - 5 Horas', 'value': '2'},
    {'label': 'Más de 5 Horas', 'value': '3'}
]


opciones7 = [
    {'label': 'Automóvil', 'value': 'Automobile'},
    {'label': 'Moto', 'value': 'Motorbike'},
    {'label': 'Bicicleta', 'value': 'Bike'},
    {'label': 'Transporte Público', 'value': 'Public_Transportation'},
    {'label': 'A pie', 'value': 'Walking'}
]

opciones8 = [{'label': str(i), 'value': str(i)} for i in range(0,4)]

opciones9 = [
    {'label': 'Si', 'value': 'yes'},
    {'label': 'No', 'value': 'no'}
]

#============================================================= Estilos de titulos y textos ======================================================================

titulo_estilo = {'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '20px'}
titulo_estilo2 = {'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '10px'}



#=============================================================== Graficos Interactivos =========================================================================

df = pd.DataFrame({
    'Country': ['TWN','PHL','MHL','GUF','KIR','NGA','NZL','PLW','SEN','THA','LAO','COD','CAF','CIV','COG','TZA','SDN','MKD','COM','NLD','DOM','ESP','GBR','MDA','VEN','ENG','IRN','WAL','BOL','NIR','ARE','GIB','MNP','RUS','SCO','PSE','VGB','CYM','FSM','USA','BHS','ABW','AFG','AGO','AIA','ALB','AND','ARG','ARM','ATG','AUS','AUT','AZE','BEL','BEN','BFA','BGD','BGR','BHR','BIH','BLR','BLZ','BMU','BRA','BRB','BRN','BTN','BWA','CAN','CHE','CHL','CHN','CMR','COL','CPV','CRI','CUB','CYP','CZE','DEU','DMA','DNK','DZA','ECU','EGY','ERI','EST','ETH','FIN','FJI','FRA','GAB','GEO','GHA','GLP','GNQ','GRC','GRD','GRL','GUY','HKG','HRV','HUN','IMN','IND','IRL','IRQ','ISL','ISR','ITA','JAM','JEY','JOR','JPN','KAZ','KEN','KGZ','KHM','KNA','KWT','LBN','LBR','LBY','LCA','LKA','LSO','LTU','LUX','LVA','MAR','MDV','MEX','MLT','MNG','MOZ','MRT','MTQ','MUS','MWI','MYS','MYT','NAM','NCL','NIC','NIU','NOR','NPL','NRU','OMN','PAK','PAN','PER','PNG','POL','PRT','PRY','PYF','QAT','ROU','RWA','SAU','SGP','SLB','SLE','SLV','SRB','STP','SVK','SVN','SWE','SWZ','SYC','SYR','TCD','TGO','TJK','TKM','TLS','TTO','TUR','UGA','UKR','URY','UZB','VCT','VNM','VUT','WSM','ZAF','ZMB','ZWE'], 
    'obesity': [6.2,6.9,31.6,17.9,45.6,7.8,30.9,38,6.4,11.6,5.6,5.8,7.2,8.5,8.6,8.7,10.3,10.5,13.5,15.5,16.6,17.14,20.1,22.7,24.6,24.7,25,26,26.2,27.3,27.8,28.9,29.2,30.3,30.4,31.6,35.5,36.6,37.1,42.7,43.7,40.8,17,6.8,38.5,21.3,13.6,32.4,19.5,43.1,31.3,17.1,20.6,16.3,7.4,4.5,5.4,13.3,36.9,22.3,18.9,33.8,34.4,25.9,33.8,28.2,11.4,11.8,24.3,11,34.4,6.51,13,21.3,14.3,25.1,15.8,14.6,19.8,19,20.2,16.5,21.8,23.38,35.7,3.4,21.8,1,20.9,31.7,17,16.2,33.2,15,22.9,8.3,16.4,25.2,28,23.6,6.9,23,23.8,29,5.5,21,33.5,22.3,17,10.4,28.6,18,32.7,4.5,23.5,10.8,23.1,1.9,45,43.75,27,4.9,42.4,31.9,9.6,11.5,18.9,16.5,22.3,20,18.1,36.7,28.7,18.5,9.1,20.9,21.9,19.1,7.6,19.7,31,8.4,38.4,22,61,14,7.2,58.1,30.7,14.9,36.3,26,6.8,19,16.9,23.2,40.4,41.4,10.9,4.3,20.2,11.6,13.1,3.3,27.3,20.8,11.7,19.1,19.9,16,20.5,30.3,18.9,13.7,6.2,13.5,15,1.1,25.7,20.2,4.6,24.8,23.7,20.2,26.9,1.7,14.9,55.8,26.2,7.5,7.7]
})


fig = px.choropleth(df, 
                    locations="Country",  # Usa el código ISO-Alpha-3 para cada país
                    color="obesity",  # Define el color basado en los niveles de obesidad
                    hover_name="Country",  # Información a mostrar al pasar el cursor
                    color_continuous_scale=px.colors.sequential.Reds  # Escala de colores
                    )

fig.update_geos(
    showcountries=True,  # Mostrar contornos de países
    bgcolor='rgba(0,0,0,0)',
)

#================================================================ Titulos del Dashboard =========================================================================
app.layout = html.Div(style={'backgroundColor': background_color, 'position': 'relative','overflowY': 'auto','maxWidth': '2000px', 'borderRadius': '10px'},
    children=[
        html.H1('Perfil Alimenticio', style={'color': text_color, 'font-family': font_family, 'margin-left': '170px',  'top': '-1px', 'right':'-1px'}),
        html.Hr(style={'position': 'absolute',  'height': '80%', 'border-color': 'white', 'left': '600px', 'margin-left': '-1px','border-width': '5px'}),
        
        html.Div([
        html.H1('Predicción de Bienestar', style={'color': text_color, 'font-family': font_family, 'margin-left': '15%'}),
        ], style={'position': 'absolute', 'left': '680px', 'top': '-1px', 'right':'-1px'}),
        
        
        
#=================================================== Listas desplegables y subtitulos de las selecciones ==========================================================        
        html.Label('¿Ustéd Fuma?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold', 'margin-top': '20px'}),  # Título de la primera lista desplegable
        dcc.Dropdown(
            id='op1',
            options=opciones1,
            value='no',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Qué tan frecuente bebe alcohol?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold', 'margin-bottom': '20px'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op2',
            options=opciones2,
            value='no',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('Número de Comidas al Día', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op3',
            options=opciones3,
            value=3,  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Cuantos litro de agua bebe al día?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op4',
            options=opciones4,
            value='3.0',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Cuánto tiempo utilizas dispositivos tecnológicos?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op5',
            options=opciones5,
            value=0.5,  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Qué medio de transporte utiliza habitualmente?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op6',
            options=opciones7,
            value='Automobile',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
         
        
        html.Label('¿Suele comer verduras en sus comidas?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op7',
            options=opciones8,
            value=3,  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        
        
        html.Label('¿Consume Comidas Rapidas?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='op8',
            options=opciones9,
            value='yes',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        

#=================================================== Cuadros de texto y otros accesorios ========================================================== 
        
        html.Div([
            html.Div('Autores: Laura Peralta Rivera; Juan David Roldán; Jairo Rueda; Diego García Montaño.', style={**titulo_estilo2,'font-weight': 'bold', 'font-family': font_family, 'font-size': '12px'}),

        ], style={**titulo_estilo2,'position': 'absolute', 'bottom': '3px', 'left': '650px'}),

        html.Div([
            dcc.Graph(
                id='example-graph',
                figure=fig  
            )
        ], style={'position': 'absolute', 'left': '990px', 'top': '180px', 'transform': 'translate(-50%, -20%)', 'width': '680px', 'height': '50px','border-radius': '10px'}),
        
        html.Div([
            dcc.Markdown(
                id = "resultado2",
                style= cuadro_texto_estilo 
            )
        ], style={'position': 'absolute', 'bottom': '20px', 'left': '650px'}),
        
        html.Div([
            dcc.Markdown(
                id= "resultado",
                style= cuadro_texto_estilo3 
            )
        ], style={'position': 'absolute', 'bottom': '550px', 'left': '650px'}),
        
        
        

        ]
    )


#======================================================== Method to update prediction ========================================================== 

@app.callback(
    Output(component_id='resultado', component_property='children'),
    Output(component_id='resultado2', component_property='children'),
    [Input(component_id='op1', component_property='value'), 
     Input(component_id='op2', component_property='value'), 
     Input(component_id='op3', component_property='value'), 
     Input(component_id='op4', component_property='value'),
     Input(component_id='op5', component_property='value'), 
     Input(component_id='op6', component_property='value'), 
     Input(component_id='op7', component_property='value'), 
     Input(component_id='op8', component_property='value')
    ]
)
def update_output_div(op1,op2,op3,op4,op5,op6,op7,op8):
    myreq = {
        "SMOKE": op1,
        "CALC": op2,
        "NCP": float(op3),
        "CH2O": float(op4),
        "TUE": float(op5),
        "MTRANS": op6,
        "FCVC": float(op7),
        "FAVC": op8
            }
    
    myreq_json = json.dumps(myreq)
    
    headers =  {"Content-Type":"application/json", "accept": "application/json"}

    # POST call to the API
    response = requests.post(api_url, data=myreq_json, headers=headers)
    data = response.json()
    logger.info("Response: {}".format(data))

    # Pick result to return from json format
    
    resultado = "Predicción: " + str(data)
    resultado2 = lista_recomendaciones[data[0]]
    
    return resultado, resultado2

#Reall

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)



# In[ ]:




