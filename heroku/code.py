import pandas as pd

from bokeh.io import output_file, show, output_notebook, save
from bokeh.models import ColumnDataSource, Select, DateRangeSlider
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, HoverTool, ColumnDataSource
from bokeh.layouts import column
from bokeh.palettes import Spectral6

#Nampilin File Output
output_file('Tubes_Visdat.html')

#Read CSV
df = pd.read_csv("datasettubes.csv")

Negara_list = list(df['Negara'].unique())

df['Tahun'] = pd.to_datetime(df['Tahun'])

cols1=df.loc[:, ['Negara','Tahun', 'Export']]
cols2 = cols1[cols1['Negara'] == 'Malaysia' ]

Overall = ColumnDataSource(data=cols1)
Curr=ColumnDataSource(data=cols2)

callback = CustomJS(
	args=dict(source=Overall, sc=Curr), 
	code="""
		var f = cb_obj.value
		sc.data['Tahun']=[]
		sc.data['Export']=[]
		for(var i = 0; i <= source.get_length(); i++){
			if (source.data['Negara'][i] == f){
				sc.data['Tahun'].push(source.data['Date'][i])
                sc.data['Export'].push(source.data['Export'][i])
               
			 }
		}   
		   
		sc.change.emit();
		"""
)

menu = Select(options=Negara_list,value='Malaysia', title = 'Negara')  # drop down menu
bokeh_p=figure(x_axis_label ='Tahun', y_axis_label = 'Total Export (Ton)', y_axis_type="linear",x_axis_type="datetime") #creating figure object 
bokeh_p.line(x='Tahun', y='Export', color='Red', legend_label="Total Export (Ton)",source=Curr)
bokeh_p.legend.location = "top_right"

bokeh_p.add_tools(HoverTool(
    tooltips=[
        ('Export (Ton)', '@{Export}'),
    ],

    mode='mouse'
))

menu.js_on_change('value', callback) 

date_range_slider = DateRangeSlider(value=(min(df['Tahun']), max(df['Tahun'])),start=min(df['Tahun']), end=max(df['Tahun']))

date_range_slider.js_link("value", bokeh_p.x_range, "start", attr_selector=0)
date_range_slider.js_link("value", bokeh_p.x_range, "end", attr_selector=1)
layout = column(menu, date_range_slider, bokeh_p)

show(layout)