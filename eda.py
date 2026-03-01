"""
Exploratory Data Analysis for House Price Prediction
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load data
df = pd.read_csv('data/house_prices.csv')

print("=" * 50)
print("HOUSE PRICE DATASET - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Basic info
print("\n1. Dataset Overview:")
print(f"Shape: {df.shape}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")

# Statistical summary
print("\n2. Statistical Summary:")
print(df.describe())

# Correlation analysis
print("\n3. Correlation with Price:")
correlations = df.corr()['price'].sort_values(ascending=False)
print(correlations)

# Create visualizations
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('House Price Dataset - Exploratory Data Analysis', fontsize=16, y=1.00)

# 1. Price distribution
axes[0, 0].hist(df['price'], bins=50, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Price Distribution')
axes[0, 0].set_xlabel('Price ($)')
axes[0, 0].set_ylabel('Frequency')

# 2. Area vs Price
axes[0, 1].scatter(df['area'], df['price'], alpha=0.5, color='coral')
axes[0, 1].set_title('Area vs Price')
axes[0, 1].set_xlabel('Area (sq ft)')
axes[0, 1].set_ylabel('Price ($)')

# 3. Bedrooms vs Price
axes[0, 2].boxplot([df[df['bedrooms']==i]['price'] for i in range(1, 6)])
axes[0, 2].set_title('Price by Bedrooms')
axes[0, 2].set_xlabel('Number of Bedrooms')
axes[0, 2].set_ylabel('Price ($)')

# 4. Age vs Price
axes[1, 0].scatter(df['age'], df['price'], alpha=0.5, color='green')
axes[1, 0].set_title('Age vs Price')
axes[1, 0].set_xlabel('Age (years)')
axes[1, 0].set_ylabel('Price ($)')

# 5. Location Score vs Price
axes[1, 1].scatter(df['location_score'], df['price'], alpha=0.5, color='purple')
axes[1, 1].set_title('Location Score vs Price')
axes[1, 1].set_xlabel('Location Score')
axes[1, 1].set_ylabel('Price ($)')

# 6. Correlation heatmap
corr_matrix = df.corr()
im = axes[1, 2].imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
axes[1, 2].set_xticks(range(len(corr_matrix.columns)))
axes[1, 2].set_yticks(range(len(corr_matrix.columns)))
axes[1, 2].set_xticklabels(corr_matrix.columns, rotation=45, ha='right', fontsize=8)
axes[1, 2].set_yticklabels(corr_matrix.columns, fontsize=8)
axes[1, 2].set_title('Correlation Heatmap')
plt.colorbar(im, ax=axes[1, 2])

# 7. Pool impact
pool_data = df.groupby('has_pool')['price'].mean()
axes[2, 0].bar(['No Pool', 'Has Pool'], pool_data, color=['lightblue', 'darkblue'])
axes[2, 0].set_title('Average Price by Pool')
axes[2, 0].set_ylabel('Average Price ($)')

# 8. Garage impact
garage_data = df.groupby('garage')['price'].mean()
axes[2, 1].bar(range(len(garage_data)), garage_data, color='orange')
axes[2, 1].set_title('Average Price by Garage Size')
axes[2, 1].set_xlabel('Number of Garage Spaces')
axes[2, 1].set_ylabel('Average Price ($)')

# 9. Bathrooms vs Price
bathroom_data = df.groupby('bathrooms')['price'].mean()
axes[2, 2].bar(range(len(bathroom_data)), bathroom_data, color='lightgreen')
axes[2, 2].set_title('Average Price by Bathrooms')
axes[2, 2].set_xlabel('Number of Bathrooms')
axes[2, 2].set_ylabel('Average Price ($)')

plt.tight_layout()
plt.savefig('data/eda_visualization.png', dpi=300, bbox_inches='tight')
print("\n4. Visualization saved as 'data/eda_visualization.png'")

plt.show()

# Feature insights
print("\n5. Key Insights:")
print(f"   - Average Price: ${df['price'].mean():,.2f}")
print(f"   - Price Range: ${df['price'].min():,.2f} - ${df['price'].max():,.2f}")
print(f"   - Most correlated feature: {correlations.index[1]} ({correlations.iloc[1]:.3f})")
print(f"   - Average price with pool: ${df[df['has_pool']==1]['price'].mean():,.2f}")
print(f"   - Average price without pool: ${df[df['has_pool']==0]['price'].mean():,.2f}")
