#!/usr/bin/env python
# coding: utf-8

# In[ ]:


df = [
"biofuel_share_energy","coal_share_energy","gas_share_energy","hydro_share_energy","oil_share_energy","other_renewables_share_energy","solar_share_energy","wind_share_energy"
]

for item in df :
    item_std = item+"_std"
    data0[item_std] = (data0[item] - data0[item].mean()) / data0[item].std()
datapca = data0[[
"biofuel_share_energy_std","coal_share_energy_std","gas_share_energy_std","hydro_share_energy_std","oil_share_energy_std","other_renewables_share_energy_std","solar_share_energy_std","wind_share_energy_std"
]]
values = datapca.values
pca = PCA()
pca.fit(values)
fig,ax = plt.subplots(1,1,figsize=(15,5))
ax.plot(np.arange(0,len(datapca.columns)),100*np.cumsum(pca.explained_variance_ratio_));
ax.set_ylabel('% Variance Explained')
ax.set_xlabel('EigenVectors considered');
pca.components_.T
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7','PC8'], index=[
"biofuel_share_energy","coal_share_energy","gas_share_energy","hydro_share_energy","oil_share_energy","other_renewables_share_energy","solar_share_energy","wind_share_energy"
])
display(loadings)

Index= ["biofuel_share_energy","coal_share_energy","gas_share_energy","hydro_share_energy","oil_share_energy","other_renewables_share_energy","solar_share_energy","wind_share_energy"]
Cols = ['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7','PC8']
df = pd.DataFrame(loadings, index=Index, columns=Cols)
plt.figure()

sns.heatmap(df, annot=True)

