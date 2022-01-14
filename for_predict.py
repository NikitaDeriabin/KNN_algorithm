from main import dataset, num_neighbors, predict_classification

rows = [
    [6.6, 3.2, 5.6, 2.2, None],
    [6.1, 3.1, 4.7, 1.7, None],
    [5.3, 3.3, 1.6, 0.3, None],
]

for row in rows:
    print("[%s] => %d" % (row, predict_classification(dataset, row, num_neighbors)))

