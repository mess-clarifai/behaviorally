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
