import plotly.express as px
from shiny.express import input, ui
from shiny import render
from shinywidgets import render_plotly
import palmerpenguins
import seaborn

penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Caleb Sellinger - Module 2: Palmer Penguins Data", fillable=True)
with ui.layout_columns():

    @render.data_frame
    def plot1():
        return render.DataGrid(penguins_df,summary=True)

    @render.data_frame
    def plot2():
        return render.DataTable(penguins_df)
    
with ui.layout_columns():

    @render.plot(alt="Seaborn histogram plot")
    def plot3():
        return seaborn.histplot(data=penguins_df,x="species",y="body_mass_g")
    
    @render_plotly
    def plot4():
        return px.histogram(data_frame=penguins_df,x="species",y="body_mass_g")
    
with ui.card(full_screen=True):
    ui.card_header("Plotly Scatterplot: Species")
    @render_plotly
    def plot5():
        return px.scatter(penguins_df,x="flipper_length_mm",y="body_mass_g",color="species",title="Body Mass vs Flipper Length",labels={"body_mass_g":"Body Mass (g)","flipper_length_mm":"Flipper Length (mm)","species":"Species"})
    

with ui.sidebar(open="open",bg="#99ccff",fillable=True):
    ui.input_dark_mode(mode="light")
    ui.h2("Sidebar")
    ui.input_selectize(id="selected_attribute",label="Select Something",choices=["Purple","Red","Blue","Yellow"])
    ui.input_numeric(id="selected_numeric",label="Numeric Input",value=10)
    ui.input_slider("seaborn_bin_count","Seaborn Slider",0,3,2)
    ui.input_checkbox_group("selected_species_list","Checkboox",choices=["Table","Chair","Stool"],selected=["Chair","Stool"],inline=False)
    ui.hr()
    ui.a("Link HERE",href="https://github.com/crsellinger/cintel-02-data",target="_blank")
