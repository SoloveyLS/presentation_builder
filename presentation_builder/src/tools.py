import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib
from io import BytesIO
from pptx.util import Inches
from pptx.slide import Slide

def add_latex_formulas_as_images(
    slide:Slide, 
    slide_data:dict, 
    y_offset:Inches, 
    text_width:float,
    fonstize:int=16,
):
    """
    Parses LaTeX formulas from slide_data and adds them as images to the slide.

    Args:
        slide: The slide object to add the formulas to.
        slide_data: A dictionary containing slide data, including a "formulas" list.
        y_offset: The vertical offset from the top of the slide for the first formula.
        text_width: The width of the area for the formulas.
    """
    if slide_data["formulas"]:
        matplotlib.rcParams["mathtext.fontset"] = "cm"
        for formula in slide_data["formulas"]:
            fig = plt.figure(constrained_layout=True)
            gs = GridSpec(1, 1, figure=fig) # getting rid of useless warnings
            
            ax = fig.add_subplot(gs[0, 0])
            ax.axis('off')

            # Render the LaTeX formula
            text = ax.text(0.5, 0.5, f" ${formula}$", fontsize=fonstize, ha='center', va='center', transform=ax.transAxes)

            # Get tight bounding box of the text
            fig.canvas.draw()
            renderer = fig.canvas.get_renderer()
            bbox = text.get_window_extent(renderer=renderer)
            bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())

            aspect_ratio = bbox_inches.height / bbox_inches.width

            # Determine image dimensions for PowerPoint
            if bbox_inches.width > text_width:
                width = Inches(text_width)
                height = Inches(text_width * aspect_ratio)
            else:
                width = Inches(bbox_inches.width)
                height = Inches(bbox_inches.height)

            fig.set_size_inches(bbox_inches.width, bbox_inches.height)
            img_buffer = BytesIO()
            plt.savefig(img_buffer, format='png', dpi=300, transparent=True)
            plt.close(fig)

            # Add the image to the slide
            left = Inches(0.5)
            top = y_offset
            slide.shapes.add_picture(img_buffer, left, top, width=width, height=height)

            y_offset += height + Inches(.2)

    return y_offset