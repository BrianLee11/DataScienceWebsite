def plot2DGraph(simpleData2D, show_plot=False):
    import numpy as np
    import matplotlib.pyplot as plt
    import io

    # Convert to numpy array
    data = np.array(simpleData2D)
    x = data[:, 0]
    y = data[:, 1]

    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y, color='blue', label='Data Points')
    ax.set_title("Simple 2D Scatter Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()

    # Optionally show the plot (for debugging / dev)
    if show_plot:
        plt.show()

    # Save the figure to a BytesIO buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    return buf