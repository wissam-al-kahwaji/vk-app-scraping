import csv
from app import VkApp

"""
    # django
    app = VkApp().get(url="https://vk.com/wall-[id]")

    #save in csv file
    app = VkApp().get(url="https://vk.com/wall-[id]", csv=True, filename="dataset.csv")
    
    default:
        csv = False
        filename="dataset.csv"
"""


def run_get_csv(file_input: str | None = None, file_output: str | None = None):
    try:
        with open(file_input, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'urls' in row:
                    VkApp().get(url=row['urls'],
                                csv=True, filename=file_output)
                    print(f"Done: {row['urls']}")
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    run_get_csv("urls.csv", "dataset.csv")
