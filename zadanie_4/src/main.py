import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS

decision_matrix = np.array([
    [250, 80, 10],
    [200, 90, 15],
    [300, 85, 7],
    [275, 88, 12]
])

weights = np.array([0.4, 0.4, 0.2])

# kryteria: -1 = minimalizować, 1 = maksymalizować
criteria_types = [-1, 1, -1]

bounds = np.array([
    [np.min(decision_matrix[:, i]), np.max(decision_matrix[:, i])]
    for i in range(decision_matrix.shape[1])
])

topsis = TOPSIS()
spotis = SPOTIS(bounds=bounds)

topsis_ranking = topsis(decision_matrix, weights, criteria_types)
spotis_ranking = spotis(decision_matrix, weights, criteria_types)

results = pd.DataFrame({
    'Alternatywa': ['A1', 'A2', 'A3', 'A4'],
    'TOPSIS': topsis_ranking,
    'SPOTIS': spotis_ranking
})

print("Ranking wg TOPSIS:")
print(results.sort_values(by='TOPSIS').reset_index(drop=True))

print("\nRanking wg SPOTIS:")
print(results.sort_values(by='SPOTIS').reset_index(drop=True))
