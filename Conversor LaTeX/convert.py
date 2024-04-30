import matplotlib.pyplot as plt
import os
from matplotlib import rc
import matplotlib.transforms as transforms

# LaTeX configuration in matplotlib
rc('text', usetex=True)
rc('font', family='serif')

def render_equation(latex, escala, formato, save_folder):
    # Initial figure setup
    fig, ax = plt.subplots(figsize=(2, 2))  # Initial size
    ax.axis('off')  # Hide the axes
    ax.patch.set_alpha(0)  # Set transparent background

    # Render the LaTeX equation
    text = ax.text(0.5, 0.5, r'$' + latex + r'$', fontsize=12 * escala, ha='center', va='center')

    # Adjust the figure to the size of the text
    fig.canvas.draw()  # Draw the text to calculate the size
    bbox = text.get_window_extent(renderer=fig.canvas.get_renderer())
    bbox_data = bbox.transformed(ax.transData.inverted())
    fig.set_size_inches(bbox_data.width * 2, bbox_data.height * 2.2)

    # Save image
    save_path = os.path.join(save_folder, f"ecuacion.{formato}")
    plt.savefig(save_path, format=formato, transparent=True, dpi=300 * escala, bbox_inches='tight', pad_inches=0)
    plt.close()

    print(f"Ecuación guardada en {save_path}")

# Example
latex_input = r'X = \displaystyle\sum_{i=1}^{N} T_i \hspace{.1cm} o(h)'
escala = 3.0  # Size 300%
formato = 'png'  # You can change to 'jpg', 'svg', etc.
save_folder = 'images'

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

render_equation(latex_input, escala, formato, save_folder)