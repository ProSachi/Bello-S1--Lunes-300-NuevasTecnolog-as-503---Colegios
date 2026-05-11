import seaborn as sns
import pandas as pd

# Todos los gráficos en Seaborn siguen esta misma estructura exacta:
df = pd.DataFrame({
    'categoria': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'valor': [320, 450, 280, 510, 390] })
col_categoria = ['blue', 'red', 'green']

sns.boxplot(
    data=df,       # 1. Le pasas el DataFrame COMPLETO (no necesitas agruparlo antes)
    x='categoria',       # 2. Qué va en el eje horizontal
    y='valor',       # 3. Qué va en el eje vertical
)
sns.show()
