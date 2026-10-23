from DataCollector import DataCollector
from FileWriter import FileWriter

class Main:

    def main(self) -> None:
        """ This is the main class that controls the random file generation.
        A random data is created in using DataCollector.
        After data creation the data is written from the memory to the disk. 
        """

        data_collector = DataCollector()
        file_writer = FileWriter()
    
        data = data_collector.collect_data()
        file_writer.write(data)

if __name__ == "__main__":
    Main().main()