import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('advertising.csv')
x=data[['TV','radio','newspaper']]
y=data[['sales']]

# plt.figure(figsize=(9,12))
# plt.subplot(311)
# plt.plot(data['TV'], y, 'ro')
# plt.title('tv')
# plt.grid()
# plt.subplot(312)
# plt.plot(data['radio'], y, 'g^')
# plt.title('radio')
# plt.grid()
# plt.subplot(313)
# plt.plot(data['newspaper'], y, 'b*')
# plt.title('newspaper')
# plt.grid()
# plt.tight_layout()
# plt.show()

feature_cols=['TV','radio','newspaper']
x=data[feature_cols]
y=data['sales']
print(x.head())
print(type(x))
print(x.shape)

