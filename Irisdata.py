url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
col_name = ['sepal-lenght','sepal-width','petal-lenght','petal-width','class']
dataset = pd.read_csv(url, names = col_name)
