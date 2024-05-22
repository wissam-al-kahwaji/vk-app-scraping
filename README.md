# Using Vk-App-Scraping

This document explains how to use the VkApp application for extracting comments from VK (VKontakte) posts.

## Prerequisites
- Python installed on your system.
- Chrome web browser.
- Chromedriver installed and added to your system's PATH.

### Install requirements
> Make sure to use virtualenv
```bash
pip install -r requirements.txt
```

## Usage
To use VkApp, follow these steps:

1. Ensure you have a CSV file containing VK post URLs. Each URL should be in a separate row under the column named 'urls'.

2. Modify the `urls.csv` file according to your VK post URLs.

3. Run the `main.py` script:
   ```bash
   python main.py
   ```
4. The script will iterate through the URLs in the `urls.csv` file, extract comments from each post, and save them to a CSV file named `dataset.csv` by default.

5. Optionally, you can specify input and output CSV filenames using the `file_input` and `file_output` parameters in the `run_get_csv` function.

## Example
```python
# main.py
import csv
from app import VkApp

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
```

## Using VkApp as a Class

You can utilize VkApp as a class within your Python projects. Here's a brief explanation of how to use it:

1. **Instantiate VkApp**: First, create an instance of the VkApp class.

2. **Call the `get` method**: Use the `get` method of VkApp to extract comments from VK posts. Pass the URL of the VK post as an argument to this method.

3. **Optional Parameters**: You can specify optional parameters such as `csv` (to save comments to a CSV file) and `filename` (to specify the output filename). In this case, if you set `csv` to `False`, the comments will not be saved to a CSV file.

4. **Usage Example**: Here's a simple example of how to use VkApp without saving to a CSV file:

    ```python
    from app import VkApp

    # Instantiate VkApp
    vk_app = VkApp()

    # Extract comments from a VK post without saving to a CSV file
    comments = vk_app.get(url="https://vk.com/wall-[id]")
    ```

5. **Processing Comments**: The `get` method returns a list of comments extracted from the VK post. You can then process these comments as needed within your application.

6. **Error Handling**: VkApp includes basic error handling to ensure that the provided URL is valid and that the necessary dependencies are installed.

By incorporating VkApp into your Python projects, you can easily extract comments from VK posts and integrate this functionality into your applications without saving to a CSV file.

## Additional Notes
- The default behavior is to return comments without saving to a CSV file. If you want to save comments to a CSV file, you can specify the `csv=True` parameter along with the `filename` parameter to set the output filename.
- Ensure that Chromedriver is compatible with your Chrome browser version.
