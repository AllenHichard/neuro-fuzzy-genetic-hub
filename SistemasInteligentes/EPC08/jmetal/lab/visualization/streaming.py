import logging
from typing import TypeVar, List

import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from jmetal.lab.visualization.plotting import Plot

LOGGER = logging.getLogger('jmetal')

S = TypeVar('S')

"""
.. module:: streaming
   :platform: Unix, Windows
   :synopsis: Classes for plotting solutions in real-time.

.. moduleauthor:: Antonio Benítez-Hidalgo <antonio.b@uma.es>
"""


class StreamingPlot:

    def __init__(self,
                 plot_title: str = 'Pareto front approximation',
                 reference_front: List[S] = None,
                 reference_point: list = None,
                 axis_labels: list = None):
        """
        :param plot_title: Title of the graph.
        :param axis_labels: List of axis labels.
        :param reference_point: Reference point (e.g., [0.4, 1.2]).
        :param reference_front: Reference Pareto front (if any) as solutions.
        """
        self.plot_title = plot_title
        self.axis_labels = axis_labels

        if reference_point and not isinstance(reference_point[0], list):
            reference_point = [reference_point]

        self.reference_point = reference_point
        self.reference_front = reference_front
        self.dimension = None

        import warnings
        warnings.filterwarnings("ignore", ".*GUI is implemented.*")

        self.fig, self.ax = plt.subplots(1,2)
        self.sc = None
        self.axis = None

    def plot(self, front):
        # Get data
        points, dimension = Plot.get_points(front)
        # Create an empty figure
        self.create_layout(dimension)

        # If any reference point, plot
        if self.reference_point:
            for point in self.reference_point:
                self.scp, = self.ax[0].plot(*[[p] for p in point], c='r', ls='None', marker='*', markersize=3)

        # If any reference front, plot
        if self.reference_front:
            rpoints, _ = Plot.get_points(self.reference_front)
            self.scf, = self.ax[0].plot(*[rpoints[column].tolist() for column in rpoints.columns.values],
                                     c='k', ls='None', marker='*', markersize=1)

        # Plot data
        self.sc, = self.ax[1].plot(*[points[column].tolist() for column in points.columns.values],
                                ls='None', marker='o', markersize=4)

        # Show plot
        plt.show(block=False)

    def update(self, front: List[S], reference_point: list = None) -> None:
        if self.sc is None:
            raise Exception('Figure is none')

        points, dimension = Plot.get_points(front)

        # Replace with new points
        self.sc.set_data(points[0], points[1])

        if dimension == 3:
            self.sc.set_3d_properties(points[2])

        # If any new reference point, plot
        if reference_point:
            self.scp.set_data([p[0] for p in reference_point], [p[1] for p in reference_point])

        # Re-align the axis
        self.ax[1].relim()
        self.ax[1].autoscale_view(True, True, True)

        try:
            # self.fig.canvas.draw()
            self.fig.canvas.flush_events()
        except KeyboardInterrupt:
            pass

        pause(0.01)

    def create_layout(self, dimension: int) -> None:
        self.fig.canvas.set_window_title(self.plot_title)
        self.fig.suptitle(self.plot_title, fontsize=16)

        if dimension == 2:
            # Stylize axis
            self.ax[1].spines['top'].set_visible(False)
            self.ax[1].spines['right'].set_visible(False)
            self.ax[1].get_xaxis().tick_bottom()
            self.ax[1].get_yaxis().tick_left()
        elif dimension == 3:
            self.ax[1] = Axes3D(self.fig)
            self.ax[1].autoscale(enable=True, axis='both')
        else:
            raise Exception('Dimension must be either 2 or 3')

        self.ax[1].set_autoscale_on(True)
        self.ax[1].autoscale_view(True, True, True)

        # Style options
        self.ax[1].grid(color='#f0f0f5', linestyle='-', linewidth=0.5, alpha=0.5)


def pause(interval: float):
    backend = plt.rcParams['backend']

    if backend in matplotlib.rcsetup.interactive_bk:
        figManager = matplotlib._pylab_helpers.Gcf.get_active()
        if figManager is not None:
            canvas = figManager.canvas
            if canvas.figure.stale:
                canvas.draw()
            canvas.start_event_loop(interval)
            return
