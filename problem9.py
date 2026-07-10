import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "UserID":[1,2,3,4,5,6,7,8,9,10],
    "Variant":["Control","Control","Control","Control","Control",
               "Treatment","Treatment","Treatment","Treatment","Treatment"],
    "SessionDuration":[5,7,1,6,9,10,12,2,8,15],
    "Converted":[1,0,1,1,0,1,1,0,1,1]
})

df = df[df["SessionDuration"]>=2]

print("Conversion Rate")
print(df.groupby("Variant")["Converted"].mean())

print("\nAverage Session Duration")
print(df.groupby("Variant")["SessionDuration"].mean())


control=df[df["Variant"]=="Control"]["Converted"]
treat=df[df["Variant"]=="Treatment"]["Converted"]

p1=control.mean()
p2=treat.mean()

n1=len(control)
n2=len(treat)

pooled=(control.sum()+treat.sum())/(n1+n2)

se=np.sqrt(pooled*(1-pooled)*(1/n1+1/n2))

z=(p2-p1)/se

pvalue=2*(1-(0.5*(1+np.math.erf(abs(z)/np.sqrt(2)))))

print("\nPooled Standard Error =",se)
print("Z Score =",z)
print("P Value =",pvalue)


x=np.linspace(-4,4,200)
y=(1/np.sqrt(2*np.pi))*np.exp(-0.5*x*x)

plt.plot(x,y)

plt.fill_between(x,y,where=(x>1.96),color="red",alpha=0.4)
plt.fill_between(x,y,where=(x<-1.96),color="red",alpha=0.4)

plt.axvline(z,color="blue",linestyle="--",label="Observed Z")

plt.title("A/B Testing PDF")
plt.legend()
plt.show()