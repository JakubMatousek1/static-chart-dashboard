#Seaborn
# %%

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

stats = pd.read_csv('C:\\Users\\jakub.matousek\\Desktop\\csat_python_project.csv')
stats

vis1 = sns.distplot(stats["score"], bins=20)
vis2 = sns.boxplot(data=stats,x="vendor",y="csat_cr")
vis3 = sns.lmplot(x='csat_cr', y='score', data=stats, \
                  fit_reg=False, hue='vendor', size =5, aspect=1 
                  )


    
#market size  
vis4 = sns.lmplot(x='csat_cr', y='score', data=stats, 
                  fit_reg=False, hue='vendor', size =10, aspect=1, 
                  scatter_kws={"s":100}
                  )


#Advanced Vizualizaitons
# %%

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

sns.set_style("darkgrid") #change background

stats = pd.read_csv('C:\\Users\\jakub.matousek\\Desktop\\csat_python_project.csv')
stats

#jointplots
j = sns.jointplot(data=stats,x='n_score',y='score',kind = 'hex')

#histograms
m1 = sns.distplot(stats["score"], bins=20) #seaborn histogram
m2 = sns.distplot(stats["csat_cr"], bins=20)
n1 = plt.hist(stats["score"], bins=20) #pyplot histogram
n1 = plt.hist(stats.score, bins=20) #pyplot histogram


#stacked histograms



#1 filter only market = de and show scores
stats[stats.market == 'de'].score 

h1 = plt.hist(stats[stats.market == 'de'].score)

#2 with this we put all histograms side by side..we need to stack it so let's go to step #3
plt.hist(stats[stats.market == 'de'].score) 
plt.hist(stats[stats.market == 'se'].score)

#3 stacked on top of each other
plt.hist([stats[stats.market == 'de'].score,stats[stats.market == 'se'].score], bins= 15, stacked=True)

#4 best option here is to create LOOP for the market so we don't need to add market manually
stats.info() #check if your dimension is category if not then change it
stats.market = stats.market.astype('category') #change type to category
stats.market.cat.categories #get a list of unique values

list1 = list() #create empty list for markets
mylabels = list() #create empty list for legend
for mkt in stats.market.cat.categories:
    list1.append(stats[stats.market == mkt].score) #to get markets in the loop
    mylabels.append(mkt) #adding a legend
    
h = plt.hist(list1, bins = 10, stacked = True, rwidth = 1, label=mylabels )
plt.legend()
plt.show()


#kernel density
k1 = sns.kdeplot(stats.score,stats.csat_cr)
k2 = sns.kdeplot(stats.score,stats.csat_cr,
                 shade=True, shade_lowest=False,
                 cmap='Reds')
k3 = sns.kdeplot(stats.score,stats.csat_cr,
                 cmap='Reds')

#Tip: RUn both k2+k3 to get smoother edges


#Working with Subplots
# %%


#one dimensional
f, axes = plt.subplots(1,2,figsize=(12,6)) #1row 2columns
k1 = sns.kdeplot(stats[stats.market == 'de'].score ,stats[stats.market == 'de'].csat_cr,ax=axes[0])
k1 = sns.kdeplot(stats[stats.market == 'se'].score ,stats[stats.market == 'se'].csat_cr,ax=axes[1])

#multiple dimensional
f, axes = plt.subplots(2,2,figsize=(12,6)) #2rows 2columns
k1 = sns.kdeplot(stats[stats.market == 'de'].score ,stats[stats.market == 'de'].csat_cr,ax=axes[1,0])
k1 = sns.kdeplot(stats[stats.market == 'se'].score ,stats[stats.market == 'se'].csat_cr,ax=axes[1,1])


#Violinplots vs Boxplots
# %%

filter_list = ['de', 'se', 'uk','fi']
stats[stats.market.isin(filter_list)]

#1) overview
w = sns.violinplot(data=stats[stats.market.isin(filter_list)],x='market',y='csat_cr')
z = sns.boxplot(data=stats[stats.market.isin(filter_list)],x='market',y='csat_cr')

#2) deep dive on UK
w1 = sns.violinplot(data=stats[stats.market == 'uk'],x='vendor',y='csat_cr')
z1 = sns.boxplot(data=stats[stats.market.isin(filter_list)],x='market',y='csat_cr')


#Facet Grid
# %%


from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

sns.set_style("darkgrid") #change background

stats = pd.read_csv('C:\\Users\\jakub.matousek\\Desktop\\csat_python_project.csv')
stats

filter_market = ['de', 'se','uk']
stats2 = stats[stats.market.isin(filter_market)]
stats2 = pd.DataFrame(stats[stats.market.isin(filter_market)]) ##create a new DF with DE and SE only

#scatter plot
g = sns.FacetGrid(stats2,row='market',col='vendor', hue='market')
g = g.map(plt.scatter,'score','csat_cr')

#histogram
h = sns.FacetGrid(stats2,row='market',col='vendor', hue='market')
h = h.map(plt.hist,'n_csat_cr')


#scatter plot improved -- NOTE: people read from left to right, not from top to bottom
g = sns.FacetGrid(stats2,row='vendor',col='market', hue='vendor')
kws = dict(s=50,linewidth=0.5,edgecolor='black')
g = g.map(plt.scatter,'score','csat_cr',**kws)


#Coordinates and Diagonals
# %%


g = sns.FacetGrid(stats2,row='vendor',col='market', hue='vendor')
kws = dict(s=50,linewidth=0.5,edgecolor='black')
g = g.map(plt.scatter,'score','csat_cr',**kws)
g.set(xlim=(0.5,1),ylim=(0.5,1)) ##size of x axis and y axis
for ax in g.axes.flat:
    ax.plot((0,1),(0,1),c="gray",ls="--") #add the dash line



#Dashboard
# %%


from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os


stats = pd.read_csv('C:\\Users\\jakub.matousek\\Desktop\\csat_python_project.csv')
stats

filter_market = ['de', 'se','uk']
stats2 = stats[stats.market.isin(filter_market)]
stats2 = pd.DataFrame(stats[stats.market.isin(filter_market)]) ##create a new DF with DE and SE only


sns.set_style("darkgrid") #change background

f, axes = plt.subplots(2,2, figsize=(15,15))
k1 = sns.kdeplot(stats.score,stats.csat_cr,
                 ax=axes[0,0])
k2 = sns.kdeplot(stats.score,stats.csat_cr,
                 shade=True, shade_lowest=False,
                 cmap='Reds',ax=axes[0,1])
k3 = sns.violinplot(data=stats[stats.market == 'uk'],x='vendor',y='csat_cr',
                    ax=axes[1,0])
axes[1,1].hist(stats.score,bins=15) #non seaborn chart

k1.set(xlim=(0.6,1))
k2.set(xlim=(0.6,1))
k3.set(ylim=(0.4,0.85))




#Styling
# %%

sns.set_style("dark",{"axes.facecolor":"black"}) #change background

f, axes = plt.subplots(2,2, figsize=(13,13))
#Plot [0,0]
k1 = sns.kdeplot(stats.score,stats.csat_cr,
                 shade=True, shade_lowest=True, cmap='inferno',
                 ax=axes[0,0])
#k1b = sns.kdeplot(stats.score,stats.csat_cr,
#                 cmap='cool',
#                 ax=axes[0,0])

#Plot [0,1]
k2 = sns.kdeplot(stats.score,stats.csat_cr,
                 shade=True, shade_lowest=False,
                 cmap='inferno',ax=axes[0,1])
#Plot [1,0]
k3 = sns.violinplot(data=stats[stats.market == 'uk'],x='vendor',y='csat_cr',
                    ax=axes[1,0],palette='YlOrRd')
#Plot [1,1]
axes[1,1].hist(stats.score,bins=15) #non seaborn chart

k1.set(xlim=(0.6,1))
k2.set(xlim=(0.6,1))
k3.set(ylim=(0.4,0.85))



