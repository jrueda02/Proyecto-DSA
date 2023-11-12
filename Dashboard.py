#!/usr/bin/env python
# coding: utf-8

# In[42]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px



app = dash.Dash(__name__)


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

# Normal Weight
normal_weight_recommendation = """
Recomendaciones:
- Mantén tus hábitos saludables. Sigue evitando el consumo frecuente de alimentos altos en calorías (FAVC) y continúa consumiendo una cantidad adecuada de agua (CH20).
- Asegúrate de mantener una buena condición física. Continúa monitoreando tu ingesta calórica (SCC) y mantén la frecuencia de actividad física (FAF).
- Sigue haciendo elecciones inteligentes en tus hábitos alimenticios y mantén un estilo de vida activo.
"""

# Overweight Level I
overweight_level_i_recommendation = """
Recomendaciones:
- Reduce el consumo de alimentos altos en calorías (FAVC) y trata de aumentar la frecuencia de consumo de verduras (FCVC).
- Aumenta la actividad física (FAF) y disminuye el tiempo frente a dispositivos tecnológicos (TUE).
- Establece un límite en el consumo de alcohol (CALC) y evita el consumo de alimentos entre comidas (CAEC).
- Consulta a un dietista o nutricionista para recibir orientación sobre tu plan de dieta y pérdida de peso.
"""

# Overweight Level II
overweight_level_ii_recommendation = """
Recomendaciones:
- Haz cambios significativos en tus hábitos alimenticios, incluyendo una mayor ingesta de verduras (FCVC) y la reducción de alimentos altos en calorías (FAVC).
- Comprométete con un programa de ejercicio regular (FAF) y disminuye drásticamente el tiempo frente a dispositivos tecnológicos (TUE).
- Evita el consumo de alcohol (CALC) y alimentos entre comidas (CAEC).
- Busca orientación médica y apoyo profesional para la pérdida de peso.
"""

# Obesity Type I
obesity_type_i_recommendation = """
Recomendaciones:
- Busca un enfoque multidisciplinario con un médico, dietista y entrenador personal para abordar tu obesidad.
- Adquiere el hábito de monitorear tu ingesta calórica (SCC) y establece un plan de dieta personalizado.
- Comprométete con un programa de actividad física bajo supervisión médica y una reducción significativa del tiempo en dispositivos tecnológicos (TUE).
- Evita el consumo de alcohol (CALC) y alimentos entre comidas (CAEC).
"""

# Insufficient Weight
insufficient_weight_recommendation = """
Recomendaciones:
- Aumenta la ingesta calórica y nutricional de manera saludable. Consume más alimentos ricos en nutrientes.
- Realiza un seguimiento constante de tu consumo de calorías (SCC) para asegurarte de que estás ingiriendo suficientes calorías.
- Consulta a un médico para abordar las posibles causas de la falta de peso y busca apoyo nutricional.
"""

# Obesity Type II
obesity_type_ii_recommendation = """
Recomendaciones:
- Busca apoyo médico para abordar tu obesidad de manera seria. Consulta a un especialista en obesidad.
- Sigue un plan de tratamiento médico, incluyendo una dieta controlada y un programa de ejercicio supervisado por un profesional de la salud.
- Mantén un registro constante de tus hábitos alimenticios (FAVC, FCVC, CALC, CAEC) y actividades físicas (FAF).
- Evita el consumo de alcohol y busca apoyo emocional.
"""

# Obesity Type III
obesity_type_iii_recommendation = """
Recomendaciones:
- La obesidad de tipo III requiere una atención médica inmediata y posiblemente intervención quirúrgica.
- Consulta a un cirujano bariátrico y sigue un plan de tratamiento médico riguroso.
- Sigue una dieta muy controlada, actividad física supervisada y un monitoreo constante de tus hábitos alimenticios (FAVC, FCVC, CALC, CAEC).
- Busca apoyo emocional y psicológico para enfrentar este desafío de salud significativo.
"""

#=================================================== Lista de opciones para los cuadros de selección =============================================================

opciones1 = [
    {'label': 'Si', 'value': '1'},
    {'label': 'No', 'value': '0'}
]

opciones2 = [
    {'label': 'No bebo', 'value': '1'},
    {'label': 'Aveces', 'value': '2'},
    {'label': 'Frecuentemente', 'value': '3'},
    {'label': 'Todo el tiempo', 'value': '4'}
    
]


opciones7 = [{'label': str(i), 'value': str(i)} for i in range(100, 200)]

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

opciones4 = [
    {'label': 'Menos de 1 Litro', 'value': '1'},
    {'label': 'Entre 1 y 2 Litros', 'value': '2'},
    {'label': 'Más de 2 Litros', 'value': '3'}
]

opciones5 = [
    {'label': 'No Hago', 'value': '1'},
    {'label': 'Entre 1 o 2 días', 'value': '2'},
    {'label': 'Entre 2 o 4 días', 'value': '3'},
    {'label': 'Entre 4 o 5 días', 'value': '4'}
]


opciones6 = [
    {'label': '0 - 2 Horas', 'value': '1'},
    {'label': '3 - 5 Horas', 'value': '2'},
    {'label': 'Más de 5 Horas', 'value': '3'}
]


opciones7 = [
    {'label': 'Automóvil', 'value': '1'},
    {'label': 'Moto', 'value': '2'},
    {'label': 'Bicicleta', 'value': '3'},
     {'label': 'Transporte Público', 'value': '4'},
    {'label': 'A pie', 'value': '5'},
    {'label': 'otro', 'value': '6'}
]

opciones8 = [
    {'label': 'Nunca', 'value': '1'},
    {'label': 'A veces', 'value': '2'},
    {'label': 'Always', 'value': '3'}
]

#============================================================= Estilos de titulos y textos ======================================================================

titulo_estilo = {'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '20px'}
titulo_estilo2 = {'color': 'white', 'font-family': 'Arial, sans-serif', 'font-size': '10px'}



#=============================================================== Graficos Interactivos =========================================================================

df = pd.DataFrame({
    "estados": ["Insufficient_Weight", "Normal_Weight", "Overweight_Level_I", "Overweight_Level_II", "Obesity_Type_I", "Obesity_Type_II", "Obesity_Type_III"],
    "Probabilidad": [0, 0.15, 0.05, 0.15, 0.5, 0.1, 0.05],  # Longitud igual a "estados"
    "Referencia": [1, 1, 1, 1, 1, 1, 1],  # Longitud igual a "estados"
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Probabilidad", y="estados", barmode="group", orientation='h', color_discrete_sequence=["#C6D500", "black"])

fig.update_layout(
    annotations=[
        dict(
            x=probabilidad,
            y=estado,
            text=f"{probabilidad * 100:.1f}%",  # Texto de la etiqueta con formato de porcentaje
            showarrow=False,
            font=dict(size=10, color='black'),
            xanchor='left' if probabilidad < 0.5 else 'right'  # Ajusta la posición de la etiqueta según el valor
        )
        for estado, probabilidad in zip(df['estados'], df['Probabilidad'])
    ],
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo del gráfico transparente
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Área alrededor del gráfico transparente
    xaxis_showgrid=False,  # Oculta las líneas de la cuadrícula en el eje x
    xaxis_visible=False   # Oculta el eje x
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
            id='cuadro-seleccion-1',
            options=opciones1,
            value='opcion1',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Qué tan frecuente bebe alcohol?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold', 'margin-bottom': '20px'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-2',
            options=opciones2,
            value='a',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('Número de Comidas al Día', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-3',
            options=opciones3,
            value=1,  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Cuantos litro de agua bebe al día?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-4',
            options=opciones4,
            value='a',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Que tan seguido se ejercita?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-5',
            options=opciones5,
            value='a',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Cuánto tiempo utilizas dispositivos tecnológicos?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-6',
            options=opciones6,
            value='a',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Qué medio de transporte utiliza habitualmente?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-7',
            options=opciones7,
            value='a',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        html.Label('¿Suele comer verduras en sus comidas?', style={**titulo_estilo, 'margin-left': '50px', 'font-weight': 'bold'}),  # Título de la segunda lista desplegable
        dcc.Dropdown(
            id='cuadro-seleccion-8',
            options=opciones8,
            value='a',  # Valor predeterminado
            style={'width': '500px', 'font-size': '14px', 'left': '50px', 'margin-top': '5px', 'margin-bottom': '20px'}
        ),
        
        
        
#=================================================== Cuadros de texto y otros accesorios ========================================================== 
        
        html.Div([
            html.Div('Autores: Laura Peralta Rivera; Juan David Roldán; Jairo Rueda; Diego García Montaño.', style={**titulo_estilo2,'font-weight': 'bold', 'font-family': font_family, 'font-size': '12px'}),

        ], style={**titulo_estilo2,'position': 'absolute', 'bottom': '3px', 'left': '650px'}),
        
        html.Div([
            dcc.Markdown(
                normal_weight_recommendation,
                style= cuadro_texto_estilo #{'font-family': font_family, 'font-size': '10px', 'border-radius': '10px', 'background-color': 'white', 'padding': '10px'}
            )
        ], style={'position': 'absolute', 'bottom': '20px', 'left': '650px'}),
        
        html.Div([
            dcc.Markdown(
                "Predicción: Obesity_Type_I",
                style= cuadro_texto_estilo3 #{'font-family': font_family, 'font-size': '10px', 'border-radius': '10px', 'background-color': 'white', 'padding': '10px'}
            )
        ], style={'position': 'absolute', 'bottom': '550px', 'left': '650px'}),
        
        
        html.Div([
            dcc.Markdown(
                "",
                style= cuadro_texto_estilo2 #{'font-family': font_family, 'font-size': '10px', 'border-radius': '10px', 'background-color': 'white', 'padding': '10px'}
            )
        ], style={'position': 'absolute', 'bottom': '200px', 'left': '650px'}),
        
        html.Button('PUSH', id='push-button', style={'background-color': '#C6D500', 'color': 'white', 'border': 'none', 'padding': '10px', 'margin-top': '10px', 'cursor': 'pointer','position': 'absolute', 'bottom': '2%', 'left': '575px'}),
                         

    
        html.Div([
            dcc.Graph(
                id='example-graph',
                figure=fig  # Asegúrate de tener definida tu figura 'fig'
            )
        ], style={'position': 'absolute', 'left': '1050px', 'top': '180px', 'transform': 'translate(-50%, 0%)', 'width': '680px', 'height': '100px','border-radius': '10px'})
    ]
    )


if __name__ == '__main__':
    app.run_server(debug=True, port="8053")


# In[ ]:




