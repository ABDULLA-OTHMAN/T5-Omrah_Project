# عنوان
plt.title('نسك')
matplotlib.pyplot.hist(x, bins=None, range=None, density=False,
                       histtype='bar',align='mid', orientation='vertical',
                       color=None, label=None, stacked=False,
                       data=None, **kwargs)
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
#    
sns.displot(data=df, x='Life_Expectancy', color=sns.color_palette("Set2")[2], edgecolor='white', linewidth=2)
N_points = 984
n_bins = 15
# 
x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(984) + 25
legend = ['distribution']
#
fig, axs = plt.subplots(1, 1,
						figsize =(10, 7),
						tight_layout = True)
#ticks حذف
axs.xaxis.set_ticks_position('none')
spending_average=df.groupby(['Country'])['Spending_USD'].mean()
spending_average
axs.yaxis.set_ticks_position('none')
year_spending_average=df.groupby(['Year'])['Spending_USD'].mean()
sns.displot(data=df, x='Life_Expectancy', color=sns.color_palette("Set2")[2])
# إضافة شبكة إلى الخلفية
axs.grid(b = True, color ='grey',
		linestyle ='-.', linewidth = 0.5,
		alpha = 0.6)
# إضافة نص 
fig.text(0.9, 0.15, '',
		fontsize = 13,color ='red',ha ='right',
		va ='top',alpha = 0.7)
spending_average=df.groupby(['Country'])['Spending_USD'].mean()
spending_average
# plot حذف خطوط حاويةال 
for s in ['top', 'bottom', 'left', 'right']:
	axs.spines[s].set_visible(False)
#وضع مسافة بين التسميات وبين المحاور
axs.xaxis.set_tick_params(pad = 4)
axs.yaxis.set_tick_params(pad = 8)
# 
N, bins, patches = axs.hist(x, bins = n_bins)
spending_average=df.groupby(['Country'])['Spending_USD'].mean()
spending_average
# تحديد الألوان
fracs = ((N**(9)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
	color = plt.cm.viridis(norm(thisfrac))
	thispatch.set_facecolor(color)
# تسمية للمحاور
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('Sin(Time)')
plt.title('Sine wave plot - Shamrablog.com')
plt.plot(x,y,x,y2)
plt.xlabel('Time')
plt.ylabel('Sin(Time), Cos(Time)')
plt.legend(['sin(Time)','cos(Time)'],loc='upper right')
plt.title('sin(Time) and cos(Time) from 0 to 8pi -Shamrablog.com')
spending_average=df.groupby(['Country'])['Spending_USD'].mean()
spending_average
