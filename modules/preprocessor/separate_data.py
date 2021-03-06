# this module separates the data into train and test parts

from sklearn.model_selection import train_test_split


def data_separator(matrix, labels, test_percentage):

    # separating data into train and test parts
    x_train, x_test, y_train, y_test = train_test_split(matrix, labels, test_size=test_percentage / 100,
                                                        random_state=42)

    return x_train, x_test, y_train, y_test
