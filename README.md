# BEEI-STATUS
## Description
This tool is specifically designed to help students who want to publish on the BEEI (Bulletin of Electrical Engineering and Informatics) website by checking their journal review status instantly. By using this tool, you do not need to open a browser and enter credentials every time you want to get the latest information about the status of your publication on BEEI. **This tool only works for the BEEI website and cannot be used for other websites**.

## Features
- Check journal review status in one click.
- Retrieve information from journal websites using scraping techniques.
- Uses `.env` files to securely store credentials.
## Prerequisites
Before running this tool, make sure you have Python 3.x installed on your system.

## Installation  
1. **Clone this repository**:

```bash
git clone https://github.com/tarokeitaro/beei-status.git
cd beei-status
```

2. **Create Virtual Environment**:
	It is recommended that you use a virtual environment to manage the dependencies of this project. You can create a virtual environment with the following command:

```bash
python -m venv venv
```

3. **Enable Virtual Environment**:
- In Windows:

```bash
venv\Scripts\activate
```

- In macOS/Linux:

```bash
source venv/bin/activate
```

4. **Install Dependencies**:
	Once the virtual environment is active, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

5. **Create File** `.env`:
	Create a `.env` file in the root directory of your project and add your credentials:

```
USERNAME=your_username
PASSWORD=your_password
REMEMBER=1
TARGET_URL=https://beei.org/index.php/EEI/author/submission/00000
```

## Usage
After all the steps above are completed, you can run the script to check the journal review status:

```bash
python main.py
```
Sample output:
```bash
Status: In Review
Initiated: 2025-02-09
Last modified: 2025-02-10
```

## Contribute
If you would like to contribute to this project, please create a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License.