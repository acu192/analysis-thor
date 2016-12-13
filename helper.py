import matplotlib.image as image


def watermark_fig(fig, x=50, y=50):
    datafile = '/Users/ryan/Desktop/store/galvanize_logo/ATX Galvanize Data Science (small).png'
    im = image.imread(datafile)
    fig.figimage(im, x, y, zorder=10, alpha=1.0, origin='upper')
