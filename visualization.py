"""
Visualization utilities
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Visualizer:
    """Create visualizations for data analysis and model evaluation"""
    
    def __init__(self):
        sns.set_style("whitegrid")
        self.colors = sns.color_palette("husl", 8)
    
    def plot_correlation_matrix(self, df, save_path='notebooks/correlation_matrix.png'):
        """Plot correlation matrix"""
        plt.figure(figsize=(10, 8))
        correlation = df.corr()
        sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, 
                    fmt='.2f', square=True, linewidths=1)
        plt.title('Feature Correlation Matrix', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Correlation matrix saved to {save_path}")
    
    def plot_feature_distributions(self, df, save_path='notebooks/feature_distributions.png'):
        """Plot distribution of all features"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        n_cols = len(numeric_cols)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, n_rows * 4))
        axes = axes.flatten()
        
        for idx, col in enumerate(numeric_cols):
            axes[idx].hist(df[col], bins=30, color=self.colors[idx % len(self.colors)], 
                          edgecolor='black', alpha=0.7)
            axes[idx].set_title(f'Distribution of {col}', fontweight='bold')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frequency')
            axes[idx].grid(True, alpha=0.3)
        
        # Hide extra subplots
        for idx in range(n_cols, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Feature distributions saved to {save_path}")
    
    def plot_predictions(self, y_true, y_pred, save_path='notebooks/predictions_plot.png'):
        """Plot actual vs predicted values"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Scatter plot
        ax1.scatter(y_true, y_pred, alpha=0.5, color='blue', edgecolor='black')
        ax1.plot([y_true.min(), y_true.max()], 
                [y_true.min(), y_true.max()], 
                'r--', lw=2, label='Perfect Prediction')
        ax1.set_xlabel('Actual Price ($)', fontsize=12)
        ax1.set_ylabel('Predicted Price ($)', fontsize=12)
        ax1.set_title('Actual vs Predicted Prices', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Residual plot
        residuals = y_true - y_pred
        ax2.scatter(y_pred, residuals, alpha=0.5, color='green', edgecolor='black')
        ax2.axhline(y=0, color='r', linestyle='--', lw=2)
        ax2.set_xlabel('Predicted Price ($)', fontsize=12)
        ax2.set_ylabel('Residuals ($)', fontsize=12)
        ax2.set_title('Residual Plot', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Predictions plot saved to {save_path}")
    
    def plot_feature_importance(self, coefficients_df, save_path='notebooks/feature_importance.png'):
        """Plot feature importance (coefficients)"""
        plt.figure(figsize=(10, 6))
        colors = ['green' if x > 0 else 'red' for x in coefficients_df['Coefficient']]
        plt.barh(coefficients_df['Feature'], coefficients_df['Coefficient'], color=colors, alpha=0.7)
        plt.xlabel('Coefficient Value', fontsize=12)
        plt.ylabel('Features', fontsize=12)
        plt.title('Feature Importance (Linear Regression Coefficients)', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Feature importance plot saved to {save_path}")
