print(1)
from scripts import data_ingestion, data_processing, data_analysis_microservice
print(2)
import os
from dotenv import load_dotenv
print(3)
print("import succeed")
print(4)
# load environment variables
load_dotenv()

def main():
    data_ingestion.ingest_data()
    print("data_ingestion succeed")

    data_processing.data_processor()
    print("data_processing succeed")

    data_analysis_microservice.run()
    print("data_analysis_microservice succeed")
print(5)

if __name__ == "__main__":
    main()
    print("!!!")

