import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
def integral_approx(N,fn,a,b):

    fn_sum=0
    i_apx=[ ]
    for i in range(1,N+1):
        rand=np.random.uniform(low=a,high=b)
        fn_sum = fn_sum + fn(rand)*(b-a)
        i_apx.append(4*fn_sum/i)
    i_apx=pd.DataFrame(i_apx,columns=['Estimated'])

    return i_apx

def f(x):
    return np.sqrt(1-x**2)

I=integral_approx(1000000,f,0,1)

print(I.tail())

I['Real PI']=np.pi
I['Error']=np.pi-I['Estimated']

I[['Estimated','Real PI']].plot(logx=True)
plt.xlabel('N iterations', fontsize=13)
plt.ylabel(r'$ \pi_{est} $', fontsize=13)
plt.savefig("results/mc-int-pi-estimation.png", dpi=300, bbox_inches="tight")

I['N_scaling']=1/np.sqrt(np.arange(1,len(I)+1))
I['Error'].abs().plot(logy=True,logx=True)
I['N_scaling'].plot(logy=True,logx=True,c='r')
plt.text(1000,0.1,r'$\propto \frac{1}{\sqrt{N}}$',fontsize=13)
plt.ylabel('Error',fontsize=13)
plt.savefig("results/mc-int-pi-est-error.png", dpi=300, bbox_inches="tight")