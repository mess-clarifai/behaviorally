import os

import seaborn as sns
from matplotlib import pyplot as plt

import tools


def coef_dist_plot(coefs, tag=None, force=False):
    stats = tools.desc_stats(coefs)

    if not tag or tag == '0':  # HACK this is more hardcoded than an ameoba
        output_dir = os.path.join('outputs')
    else:
        output_dir = os.path.join('outputs', 'reports', f"report_{tag}")

    os.makedirs(output_dir, exist_ok=True)

    fname = f"{tag + '_' if tag else ''}distribution-of-correlation-coefficients.png"

    output_path = os.path.join(output_dir, fname)

    if os.path.exists(output_path) or not force:
        # don't plotsta if you don't gotsta ya dingus!
        return

    msg = f"N={len(coefs)}, min={stats['min']:.2f}, med={stats['median']:.2f}, mean={stats['mean']:.2f}, max={stats['max']:.2f}"

    ax = sns.displot(coefs, kind='kde')
    plt.title(f'{"Report " + tag + ":" if tag else ""} Distribution of Correlation Coefficients ($R$)\n' + msg)
    plt.xlabel('Cooeficient of Correlation ($R$)')
    plt.tight_layout()


    plt.savefig(output_path)

    plt.clf()


def plot_series(data, x, y, title=None, period_length=13):
    g = sns.lineplot(
        x=x,
        y=y,
        hue='Image ID', # hue='Brand Name', # hue="Image Name",  # hue="Product",
        data=data,
        legend=True
    )

    plt.title(title)
    plt.xlim((0,156))  # for the items not just in single periods
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    g.set_xticks(range(data['report_dates'].nunique())) # <--- set the ticks first
    g.set_xticklabels([t.strftime('%b %d, %Y') for t in data['report_dates'].unique()])

    for i, label in enumerate(g.xaxis.get_ticklabels()):
        if ((i+1) % period_length) == 0:
            label.set_visible(True)
        else:
            label.set_visible(False)

    plt.xticks(rotation=45)

    plt.show()
