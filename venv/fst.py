a = dict({1: 'Web', 2: 'Java', 3: 'Database', 4: 'Ruby'})

for i, j in a.items():
    print(i, " ", j)

for i in a:
    print(i, a[i])
    dict1 = {'India': 'NewDelhi', 'UK':'London', 'Japan': 'Tokyo'}
    >> > print(dict1)  # Display the dictionary
    {'India': 'NewDelhi', 'UK': 'London', 'Japan':
        'Tokyo'}
    >> > series8 = pd.Series(dict1)
    >> > print(series8)  # Display the series
