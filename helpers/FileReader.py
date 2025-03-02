import pandas as pd

def read(
        path=None,
):

    """
    Function to read files.
    :param path:
    :return:
    """

    try:
        print('Trying Excel format\n')
        df = pd.read_excel(
            io=path
        )
        print('Excel File : Read\n')
        return df
    except:
        print('Excel format : Failed\n')
        try:
            print('Trying CSV format\n')
            df = pd.read_csv(path)
            print('CSV File : Read\n')
            return df
        except:
            print('CSV format : Failed\n')
            print("File format not compatible\n")
            return


