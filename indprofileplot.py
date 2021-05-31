#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fig = plt.figure()
ax = plt.subplot(111)
fig.suptitle('Individual profiles of country co2 emissions vs share of renewable energy')
plt.xlabel('renewables_share_energy')
plt.ylabel('ghg_per_capita')
plt.ylim([0,40])
for i in set(data0['country']):
    country_i = data0.loc[data0['country'] == i]
    x=country_i['renewables_share_energy']
    y=country_i['ghg_per_capita']
    order = np.argsort(x)
    xs = np.array(x)[order]
    ys = np.array(y)[order]
    ax.plot(xs, ys)
plt.show()
fig = plt.figure()
ax = plt.subplot(111)
fig.suptitle('Individual profiles of country co2 emissions vs share of nuclear energy')
plt.xlabel('nuclear_share_energy')
plt.ylabel('ghg_per_capita')
plt.ylim([0,40])
for i in set(data0['country']):
    country_i = data0.loc[data0['country'] == i]
    x=country_i['nuclear_share_energy']
    y=country_i['ghg_per_capita']
    order = np.argsort(x)
    xs = np.array(x)[order]
    ys = np.array(y)[order]
    ax.plot(xs, ys)
plt.show()
fig = plt.figure()
ax = plt.subplot(111)
fig.suptitle('Individual profiles of country co2 emissions vs share of fossil energy')
plt.xlabel('fossil_share_energy')
plt.ylabel('ghg_per_capita')
plt.ylim([0,40])
for i in set(data0['country']):
    country_i = data0.loc[data0['country'] == i]
    x=country_i['fossil_share_energy']
    y=country_i['ghg_per_capita']
    order = np.argsort(x)
    xs = np.array(x)[order]
    ys = np.array(y)[order]
    ax.plot(xs, ys)
plt.show()

