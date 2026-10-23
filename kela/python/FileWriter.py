import pandas as pd

class FileWriter():

    def __init__(self):
        pass

    def write(self, data: list[dict]) -> int:
        """Writes the random data to a file.
        
        Args:
            data: List of dicts that contain the data.
            filetype: A string that contains the type of the file. Values are csv, json, xlsx and parquet.
            
        Returns: 0 if everything went well. 1 if there was an exception.
        """

        self.df = pd.DataFrame(data)

        try:

            self.write_csv()

        except Exception as e:
            print(f"Writing file failed because of {e}")
            return 1

        return 0

    def write_csv(self) -> None:
        self.df.to_csv("./random_data/palvelu.csv", index=False)
