from flask import Flask
from scripts import data_ingestion, data_processing, data_analysis_microservice
print("import succeed")

def main():
    data_ingestion.ingest_data()
    print("data_ingestion succeed")

    data_processing.data_processor()
    print("data_processing succeed")

    data_analysis_microservice.run()
    print("data_analysis_microservice succeed")

if __name__ == "__main__":
    main()

