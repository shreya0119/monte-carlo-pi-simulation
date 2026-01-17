import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate


def PI_approx(N):
    np.random.seed(0)
    inside=0
    PI_vals=[]
    rand=[]
    rand2=[]

    snapshots=[10,100,1000,10000]

    fig, axes = plt.subplots(1, len(snapshots),figsize=(18, 6))
    plot_index = 0

    for i in range(1,N+1):
        r=np.random.uniform(low=-1,high=1)
        rand.append(r)
        r2=np.random.uniform(low=-1,high=1)
        rand2.append(r2)
        if(r*r + r2*r2 <1):
            inside=inside+1
        PI_vals.append(4*inside/i)

        if i in snapshots:
            ax = axes[plot_index]

            color = (np.array(rand) ** 2 + np.array(rand2) ** 2) < 1
            ax.scatter(rand, rand2, c=color, cmap='bwr', alpha=0.5, s=6)

            circle1 = plt.Circle((0, 0), 1, color='black',
                                 fill=False, linewidth=2, alpha=0.7)
            ax.add_patch(circle1)

            ax.set_title(r'$N=%s,\ \pi \approx %.4f$' % (i, 4 * inside / i), fontsize=13)
            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)
            ax.set_aspect('equal')
            ax.set_xlabel('x')
            ax.set_ylabel('y')

            plot_index += 1

    PI_approx_df=pd.DataFrame(PI_vals,columns=['Estimated PI'])
    PI_approx_df['Real PI']=np.pi
    PI_approx_df['Error']=np.pi - PI_approx_df['Estimated PI']

    plt.tight_layout()
    plt.savefig("results/scatter_snapshots.png", dpi=300, bbox_inches="tight")
    plt.show()

    return PI_approx_df

df=PI_approx(1000000)
print(df.tail())

plt.figure(figsize=(8,5))
plt.plot(df.index + 1, df['Estimated PI'], label='Estimated π')
plt.axhline(np.pi, linestyle='--', label='Real π')
plt.xlabel("Sample size (N)")
plt.ylabel("π value")
plt.title("Monte Carlo estimation of π")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("results/pi_convergence.png", dpi=300, bbox_inches="tight")
plt.show()

N = df.index + 1
inv_sqrt_N = 1 / np.sqrt(N)

plt.figure(figsize=(8,5))
plt.plot(N, np.abs(df['Error']), label='|Error|')
plt.plot(N, inv_sqrt_N, linestyle='--', label='1 / √N')
plt.xlabel("Sample size (N)")
plt.ylabel("Value")
plt.title("Monte Carlo error decay")
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.grid(alpha=0.3, which="both")
plt.savefig("results/error_scaling.png", dpi=300, bbox_inches="tight")
plt.show()



